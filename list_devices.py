import pyaudio

# Initialize PyAudio
p = pyaudio.PyAudio()

print("\n--- Detected Audio Devices ---")
print(f"Total devices found: {p.get_device_count()}\n")

# Iterate through all available audio I/O devices
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    
    # Determine if it's an Input, Output, or Both
    is_input = info.get('maxInputChannels') > 0
    is_output = info.get('maxOutputChannels') > 0
    
    device_type = ""
    if is_input and is_output:
        device_type = "INPUT/OUTPUT"
    elif is_input:
        device_type = "INPUT (Microphone)"
    elif is_output:
        device_type = "OUTPUT (Speaker)"
    
    print(f"ID {i}: {info.get('name')}")
    print(f"   - Type: {device_type}")
    print(f"   - Channels: {info.get('maxInputChannels')} in / {info.get('maxOutputChannels')} out")
    print(f"   - Default Sample Rate: {info.get('defaultSampleRate')} Hz")
    print("-" * 30)

# Identify system defaults for reference
try:
    default_input = p.get_default_input_device_info()
    print(f"Default Input Device: ID {default_input['index']} - {default_input['name']}")
    
    default_output = p.get_default_output_device_info()
    print(f"Default Output Device: ID {default_output['index']} - {default_output['name']}")
except IOError:
    print("Warning: No default devices found. Check your system sound settings.")

p.terminate()