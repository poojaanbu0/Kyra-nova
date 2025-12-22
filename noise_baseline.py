import pyaudio
import audioop
import time

# Use the settings that worked for your WASAPI test
MIC_ID = 9  
RATE = 48000
CHANNELS = 2
CHUNK = 2048

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=MIC_ID,
                frames_per_buffer=CHUNK)

print("🤫 Ambient Noise Test: Stay silent for 10 seconds...")
print("Reading background levels...")

max_noise = 0
start_time = time.time()

try:
    while time.time() - start_time < 10:
        data = stream.read(CHUNK)
        # audioop.rms calculates the energy level of the audio chunk
        rms = audioop.rms(data, 2) 
        if rms > max_noise:
            max_noise = rms
        print(f"Current Level: {rms}", end='\r')

    print(f"\n\n✅ Baseline Test Complete!")
    print(f"Your maximum background noise level is: {max_noise}")
    
    if max_noise < 100:
        print("Recommendation: Your room is very quiet. High sensitivity is fine.")
    elif max_noise < 500:
        print("Recommendation: Typical room. Moderate sensitivity is best.")
    else:
        print("Recommendation: High background noise! You'll need lower sensitivity.")

except Exception as e:
    print(f"Error: {e}")

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()