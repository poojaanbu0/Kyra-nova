import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()
HISTORY_FILE = "chat_history.json"

def load_history():
    """Loads chat history from a local JSON file"""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                # Convert the saved JSON back into Gemini's history format
                return json.load(f)
            except:
                return []
    return []

def save_history(history):
    """Saves the current chat history to a JSON file"""
    serializable_history = []
    for message in history:
        # Convert model objects to a simple dictionary for saving
        serializable_history.append({
            "role": message.role,
            "parts": [{"text": part.text} for part in message.parts]
        })
    with open(HISTORY_FILE, "w") as f:
        json.dump(serializable_history, f)

# 1. Initialize session with existing history
chat_session = client.chats.create(
    model='gemini-2.5-flash-lite',
    history=load_history(),
    config=types.GenerateContentConfig(
        tools=[types.Tool(google_search=types.GoogleSearch())],
        system_instruction="You are Kyra Nova, a witty AI assistant. Keep responses brief (1-2 sentences)."
    )
)

def get_ai_response(user_input):
    """Sends input to Gemini and updates the permanent file"""
    try:
        response = chat_session.send_message(user_input)
        
        # Save updated history after every response
        save_history(chat_session.get_history()) 
        
        return response.text
    except Exception as e:
        return f"Memory storage error: {e}"