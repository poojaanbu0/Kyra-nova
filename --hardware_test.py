import pyaudio

# SETTINGS BASED ON YOUR list_devices.py OUTPUT
MIC_ID = 20      # Microphone Array 3 (16kHz native)
SPEAKER_ID = 3   # Speaker (Realtek Audio)
RATE = 16000     # Matches your Mic ID 20
CHUNK = 1024     # Size of audio data blocks

p = pyaudio.PyAudio()

# Open the "Ears" and "Voice" bridge
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE,
                input=True, input_device_index=MIC_ID,
                output=True, output_device_index=SPEAKER_ID,
                frames_per_buffer=CHUNK)

print(f"* BRIDGE ACTIVE: Speak into Mic Array 3 (ID {MIC_ID}).")
print("* You should hear yourself in your Speakers (ID {SPEAKER_ID}).")
print("* Press Ctrl+C to stop.")

try:
    while True:
        data = stream.read(CHUNK)
        stream.write(data)
except KeyboardInterrupt:
    print("\n* Stopping hardware test.")

stream.stop_stream()
stream.close()
p.terminate()