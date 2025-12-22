import pyaudio

p = pyaudio.PyAudio()

# 1. Identify the WASAPI Host API
wasapi_info = None
for i in range(p.get_host_api_count()):
    api_info = p.get_host_api_info_by_index(i)
    if "WASAPI" in api_info.get('name').upper():
        wasapi_info = api_info
        break

if wasapi_info is None:
    print("Error: WASAPI driver not found. Ensure you are on Windows.")
else:
    # 2. MATCHING YOUR SETTINGS: 48000Hz and 2 Channels
    # We will use the same Mic ID (9) that you identified previously
    MIC_ID = 9  
    RATE = 48000  
    CHANNELS = 2  
    CHUNK = 2048  # Increased buffer for stability

    print(f"Testing WASAPI Mic (ID {MIC_ID})")
    print(f"Settings: {RATE}Hz, {CHANNELS} Channels")
    
    try:
        # 3. Opening the stream with precise hardware matching
        stream = p.open(format=pyaudio.paInt16, 
                        channels=CHANNELS, 
                        rate=RATE,
                        input=True, 
                        input_device_index=MIC_ID,
                        frames_per_buffer=CHUNK)
        
        print("\n🎉 SUCCESS: Connection established!")
        print("Your Python environment is now successfully communicating with your hardware.")
        
        stream.stop_stream()
        stream.close()
    except Exception as e:
        print(f"\n❌ FAILED: {e}")
        print("Possible fix: Double-check that no other app (like Zoom/Sound Recorder) is using the mic.")

p.terminate()