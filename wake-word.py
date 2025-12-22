import os
import struct
import pyaudio
import pvporcupine
import pyttsx3
from dotenv import load_dotenv
from command_capture import get_command
from ai_brain import get_ai_response

# 1. Initialization
load_dotenv()
PICOVOICE_ACCESS_KEY = os.getenv("PICOVOICE_ACCESS_KEY")

# Set the exact name of your .ppn file here
KEYWORD_PATH = "Kyra-nova_en_windows_v4_0_0.ppn" 

def kyra_responds():
    """Triggered when the wake word is heard"""
    """Re-initializes engine each time to fix the 'silent response' bug"""
    print("\n✨ Kyra: Wake word detected!")
    
    # FRESH START: Create a new engine instance for THIS response
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # Microsoft Zira (Female)
    engine.setProperty('rate', 200)
    
    engine.say("Yes? How can I assist you?")
    engine.runAndWait() #
    
    # Properly shut down this engine instance
    engine.stop() 
    print("👂 Kyra: Listening for your command...")

# 2. Setup Porcupine with Custom Keyword
try:
    porcupine = pvporcupine.create(
        access_key=PICOVOICE_ACCESS_KEY,
        keyword_paths=[KEYWORD_PATH],
        sensitivities=[0.5] # Balanced sensitivity for your 397 noise floor
    )
except Exception as e:
    print(f"Error initializing Porcupine: {e}")
    exit()

# 3. Setup Audio Stream
pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

print(f"👂 Kyra is standby. Say 'Kyra nova' to wake her up...")

# 4. Main Loop
try:
    while True:
        # Read audio chunk
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        # Process audio for wake word
        result = porcupine.process(pcm)

        if result >= 0:
            # Step 2: Stop listening for wake word to free the mic
            audio_stream.stop_stream()

            # Step 3: Respond and Capture Command
            kyra_responds()
            user_text = get_command() # Calling Phase 2 Logic
            # PHASE 2 WILL GO HERE: Transcription logic

            print(f"💬 Kyra Understood: '{user_text}'")
            
            # Step 4: Resume Standby
            audio_stream.start_stream()
            print("\n👂 Returning to standby...")
            
except KeyboardInterrupt:
    print("\nStopping Kyra...")
finally:
    # 5. Resource Cleanup
    audio_stream.close()
    pa.terminate()
    porcupine.delete()