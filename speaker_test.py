import pyttsx3

engine = pyttsx3.init()

# Optional: List available voices
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id) # Index 1 is often a female voice

print("* Kyra is attempting to speak...")
engine.say("Hardware verification successful. My ears and voice are now online.")
engine.runAndWait()

print("* If you heard that, your speakers are working perfectly.")