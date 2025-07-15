import os
import openai
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class AIAdapter:
    def __init__(self):
        self.provider = os.getenv("AI_PROVIDER", "openai").lower()
        if self.provider == "openai":
            openai.api_key = os.getenv("OPENAI_API_KEY")
            if not openai.api_key:
                raise ValueError("OPENAI_API_KEY not found in .env for OpenAI provider.")
        elif self.provider == "gemini":
            gemini_api_key = os.getenv("GEMINI_API_KEY")
            if not gemini_api_key:
                raise ValueError("GEMINI_API_KEY not found in .env for Gemini provider.")
            genai.configure(api_key=gemini_api_key)
        else:
            raise ValueError("Invalid AI_PROVIDER. Must be 'openai' or 'gemini'.")

    def chat_completion(self, messages, model=None, temperature=0.3, max_tokens=400):
        if self.provider == "openai":
            if model is None:
                model = "gpt-4"
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response['choices'][0]['message']['content'].strip()
        elif self.provider == "gemini":
            if model is None:
                model = "models/gemini-2.5-pro"
            gemini_messages = []
            for msg in messages:
                role = "user" if msg["role"] == "user" else "model"
                gemini_messages.append({"role": role, "parts": [msg["content"]]})

            model_instance = genai.GenerativeModel(model)
            response = model_instance.generate_content(
                gemini_messages,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    max_output_tokens=10000
                )
            )
            return response.text

    def list_models(self):
        if self.provider == "gemini":
            print("Attempting to list Gemini models...")
            for m in genai.list_models():
                print(f"  Name: {m.name}, Supported Generation Methods: {m.supported_generation_methods}")
        else:
            print("Model listing is only implemented for Gemini provider.")
