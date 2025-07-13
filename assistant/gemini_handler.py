# gemini_handler.py

import os
import google.generativeai as genai 


def get_gemini_response(prompt:str) ->str:
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model=genai.GenerativeModel("gemini-pro")
        response=model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[Gemini Error] {str(e)}"    