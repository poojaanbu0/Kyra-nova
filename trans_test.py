import whisper
import os

# This will download the 'base' model (about 140MB) the first time you run it
print("🧠 Kyra is loading her brain (Whisper Model)...")
model = whisper.load_model("base")

def transcribe_audio(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found. Run a recording first!")
        return

    print("📝 Transcribing...")
    result = model.transcribe(file_path)
    print(f"✅ Kyra heard: '{result['text']}'")

# For this test, we need a .wav file. 
# Do you have one, or should we create the recording script next?