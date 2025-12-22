import pyaudio
import wave

# SETTINGS FOR YOUR MIC
MIC_ID = 20
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "mic_test.wav"

p = pyaudio.PyAudio()

# Open ONLY Input
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE,
                input=True, input_device_index=MIC_ID,
                frames_per_buffer=CHUNK)

print(f"* Recording from Mic ID {MIC_ID} for 5 seconds...")

frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* Finished recording.")

# Stop and close
stream.stop_stream()
stream.close()
p.terminate()

# Save as a .wav file so you can listen to it manually
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print(f"* File saved as: {WAVE_OUTPUT_FILENAME}")