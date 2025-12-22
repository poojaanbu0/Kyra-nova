import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model - using Gemini 1.5 Flash for speed
model = genai.GenerativeModel('gemini-1.5-flash')

def get_ai_response(user_input):
    """Sends user text to Gemini and returns a concise response"""
    prompt = f"You are Kyra Nova, a helpful and witty AI assistant. Keep your responses brief (1-2 sentences) for voice conversation. User says: {user_input}"
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"I'm having trouble thinking right now. Error: {e}"