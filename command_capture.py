import whisper
import sounddevice as sd
import scipy.io.wavfile as wav
import os

# Load the "base" model you already tested
print("🧠 Loading Kyra's STT engine...")
model = whisper.load_model("base")

def get_command(duration=5, fs=16000):
    """Records for a fixed duration and returns the text."""
    temp_file = "command.wav"
    
    print(f"🎤 Kyra is recording your command for {duration} seconds...")
    # Whisper works best at 16000Hz mono
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()  # Wait for recording to finish
    
    # Save temporarily to disk for Whisper
    wav.write(temp_file, fs, recording)
    
    print("📝 Thinking...")
    # fp16=False is used if you are running on a standard CPU
    result = model.transcribe(temp_file, fp16=False)
    
    # Clean up the file after use
    if os.path.exists(temp_file):
        os.remove(temp_file)
        
    return result['text'].strip()

# Run a quick test
if __name__ == "__main__":
    text = get_command()
    print(f"✅ Kyra heard: '{text}'")