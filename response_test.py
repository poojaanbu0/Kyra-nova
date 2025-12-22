import pyttsx3
import time

def kura_responds():
    # Visual Cue
    print("\n[V] Kyra: Wake word detected!")
    print("👂 Kyra: Listening for command...")
    
    # Audio Cue using your verified TTS engine
    engine = pyttsx3.init()
    # Get the list of available voices from your system
    voices = engine.getProperty('voices')

    # Set the voice to Index 1 (Microsoft Zira - Female)
    engine.setProperty('voice', voices[1].id)
    # Speed her up slightly so the response feels snappy (Default is ~200)
    engine.setProperty('rate', 200) 
    
    # Short, clear confirmation
    engine.say("Yes?how can I assist you?") 
    engine.runAndWait()

# Simulate the moment she hears you
print("... (Kyra is in standby) ...")
time.sleep(2) # Simulating a wait
kura_responds()