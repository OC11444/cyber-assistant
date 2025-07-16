# voice_input.py

import contextlib
from vosk import Model, KaldiRecognizer
import json
import speech_recognition as sr
import dotenv
from assistant.gemini_handler import get_gemini_response
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
dotenv.load_dotenv()

# vosk model path
MODEL_PATH = "vosk-model-small-en-us-0.15"


def listen_for_command():
    """
    Listens for voice using Vosk and SpeechRecognition.
    """
    print("[Nova Voice] 🔍 Checking for model...")

    if not os.path.exists(MODEL_PATH):
        print("[❌] Vosk model not found at:", MODEL_PATH)
        return None

    print("[Nova Voice] ✅ Model found. Initializing...")
    with suppress_stderr():
        model = Model(MODEL_PATH)
        recognizer = KaldiRecognizer(model, 16000)
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("[🎙️] Calibrating mic for ambient noise...")
            r.adjust_for_ambient_noise(source, duration=1)
            print(f"[⚙️] Energy threshold set to: {r.energy_threshold}")

            print("[🎤] Listening... Speak clearly now.")
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("[📡] Captured audio. Processing...")

            audio_data = audio.get_raw_data(
                convert_rate=16000, convert_width=2)

            if recognizer.AcceptWaveform(audio_data):
                result = json.loads(recognizer.Result())
                print("[✅] Final result:", result)
                return result['text']
            else:
                result = json.loads(recognizer.PartialResult())
                print("[⚠️] Partial result:", result)
                return result.get('partial', '')

    except sr.UnknownValueError:
        print("[❌] Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"[❌] Could not request results; {e}")
        return None
    except Exception as e:
        print(f"[💥] Unknown error: {str(e)}")
        return None


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # TensorFlow (if ever used)
os.environ["PYTHONWARNINGS"] = "ignore"  # Hide warnings


@contextlib.contextmanager
def suppress_stderr():
    with open(os.devnull, 'w') as devnull:
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stderr = old_stderr


# Manual test entry point for group development
if __name__ == "__main__":
    print("🧪 Running standalone voice test...")
    text = listen_for_command()
    print(f"[🗣️] You said: {text}")

    if text:
        print("🤖 Sending to Gemini...")
        gemini_reply = get_gemini_response(text)
        print(f"[Gemini 🧠] {gemini_reply}")
    else:
        print("❌ No valid text received.")
