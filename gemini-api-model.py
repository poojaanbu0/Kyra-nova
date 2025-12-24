import os
import google.genai as genai
from dotenv import load_dotenv

# 1. Setup
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 2. List Models
print("Available Gemini Models for Content Generation:")
for model in genai.list_models():
    # Only list models that support 'generateContent'
    if 'generateContent' in model.supported_generation_methods:
        print(f"- {model.name} (Display Name: {model.display_name})")