# 🎙️ Kyra Nova: Personal AI Voice Assistant
Kyra Nova is a local voice assistant that uses Picovoice for wake-word detection, OpenAI Whisper for transcription, and Google Gemini for intelligent responses.

## ⚙️ Prerequisites
- **Python**: 3.10 or higher
- **FFmpeg**: Must be installed and added to your system PATH.
- **Microphone**: Required for voice input.

## 🚀 Getting Started

### 1. Clone the Repository
```
git clone [https://github.com/yourusername/kyra-nova.git](https://github.com/yourusername/kyra-nova.git)
cd kyra-nova
```

### 2. Install Dependencies
```
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a file named .env in the root directory and add your API keys:
```
PICOVOICE_ACCESS_KEY=your_key_here
GEMINI_API_KEY=your_key_here
```


### 🧠 Usage

Run the main script to start Kyra:
Bash
```
python wake_word.py
```

1. Wait for: 👂 Kyra is standby. Say 'Kyra nova'...
2. Say "Kyra nova".
3. When she responds "Yes?", ask your question.


### Project Structure

-wake_word.py: The main loop and wake-word listener.

-ai_brain.py: Handles Gemini API, memory, and reflection logic.

-command_capture.py: Records audio and processes Whisper transcription.

-chat_history.json: Stores session memory.

-kyra_persona.json: Stores the evolved personality profile.
