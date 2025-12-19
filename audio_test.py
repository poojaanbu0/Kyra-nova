import pyaudio

p = pyaudio.PyAudio()

print("--- Detected Audio Devices ---")
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    device_type = "INPUT" if info['maxInputChannels'] > 0 else "OUTPUT"
    print(f"ID {i}: {info['name']} | Type: {device_type} | Channels: {info['maxInputChannels']} in / {info['maxOutputChannels']} out")

# Show the system default for easy reference
default_input = p.get_default_input_device_info()
print(f"\nDefault Input Device: ID {default_input['index']} - {default_input['name']}")

p.terminate() 