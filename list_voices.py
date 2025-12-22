import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Get the list of all available voices
voices = engine.getProperty('voices')

print(f"--- Found {len(voices)} Voices ---")

# Loop through the list of voices
for index, voice in enumerate(voices):
    print(f"Index: {index}")
    print(f" - Name: {voice.name}")
    print(f" - ID: {voice.id}")
    print(f" - Gender: {voice.gender}")
    print("-" * 30)
    
    # Optional: Uncomment the lines below to hear each voice speak its own name
    # engine.setProperty('voice', voice.id)
    # engine.say(f"I am {voice.name}")
    # engine.runAndWait()