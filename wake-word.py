import os
import struct
import pyaudio
import pvporcupine
import pyttsx3
from dotenv import load_dotenv
from command_capture import get_command
from ai_brain import get_ai_response  # <--- This connects your Gemini brain

# 1. Initialization
load_dotenv()
PICOVOICE_ACCESS_KEY = os.getenv("PICOVOICE_ACCESS_KEY")
KEYWORD_PATH = "Kyra-nova_en_windows_v4_0_0.ppn" 

def kyra_speaks(text):
    """Makes Kyra speak any text using a fresh engine instance to avoid bugs"""
    print(f"🤖 Kyra: {text}")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # Microsoft Zira (Female)
    engine.setProperty('rate', 200)
    
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# 2. Setup Porcupine Wake Word Engine
try:
    porcupine = pvporcupine.create(
        access_key=PICOVOICE_ACCESS_KEY,
        keyword_paths=[KEYWORD_PATH],
        sensitivities=[0.5]
    )
except Exception as e:
    print(f"Error initializing Porcupine: {e}")
    exit()

# 3. Setup Audio Stream for Wake Word
pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

print(f"👂 Kyra is standby. Say 'Kyra nova' to wake her up...")

# 4. Main Integrated Loop
try:
    while True:
        # Listen for the wake word
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        result = porcupine.process(pcm)

        if result >= 0:
            # STEP A: Stop the wake-word listener to free the microphone
            audio_stream.stop_stream()

            # STEP B: Acknowledge the user
            kyra_speaks("Yes? How can I assist you?")
            
            # STEP C: Record and Transcribe the user's command (Whisper)
            user_text = get_command() 
            print(f"💬 You said: '{user_text}'")

            if user_text:
                # STEP D: Get a smart response from Gemini (Brain)
                print("🧠 Thinking...")
                ai_answer = get_ai_response(user_text)
                
                # STEP E: Kyra speaks the smart answer back
                kyra_speaks(ai_answer)
            
            # STEP F: Restart the wake-word listener
            audio_stream.start_stream()
            print("\n👂 Returning to standby...")
            
except KeyboardInterrupt:
    print("\nStopping Kyra...")
finally:
    # Cleanup
    audio_stream.close()
    pa.terminate()
    porcupine.delete()