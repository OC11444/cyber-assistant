import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
load_dotenv()

from assistant.gemini_handler import get_gemini_response
import os

prompt = "What is the difference between TCP and UDP in computer networking?"
print("✅ GEMINI_API_KEY:", os.getenv("GEMINI_API_KEY"))
print("🧠 Prompting Gemini...")

response = get_gemini_response(prompt)
print("[Gemini Response]\n", response)
