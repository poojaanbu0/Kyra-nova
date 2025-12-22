import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Setup
load_dotenv()

# The new client automatically picks up GEMINI_API_KEY from your .env
client = genai.Client() #

def get_ai_response(user_input):
    """Sends user text to Gemini and returns a concise, grounded response"""
    
    # Configure the search tool and model settings
    config = types.GenerateContentConfig(
        tools=[types.Tool(google_search=types.GoogleSearch())], # Enables real-time web grounding
        system_instruction="You are Kyra Nova, a helpful and witty AI assistant. Keep responses very brief (1-2 sentences)."
    )

    try:
        # Using gemini-2.5-flash-lite for the best balance of speed and search capability
        response = client.models.generate_content(
            model='gemini-2.5-flash-lite',
            contents=user_input,
            config=config
        )
        return response.text
    except Exception as e:
        return f"I'm having trouble thinking right now. Error: {e}"