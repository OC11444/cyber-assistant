
import speech_recognition as sr
import json
from vosk import Model, KaldiRecognizer
import os

MODEL_PATH = "vosk-model-small-en-us-0.15"

def listen_for_command():
    """
    Listens for voice, vosk for speech recognition.
    """
    if not os.path.exists(MODEL_PATH):
        print("Error: Vosk model not found.")
        print(f"Please download the model and place it in the '{MODEL_PATH}' directory.")
        return None

    r = sr.Recognizer()
    model = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model, 16000)

    with sr.Microphone() as source:
        print("Listening for a command...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        audio_data = audio.get_raw_data(convert_rate=16000, convert_width=2)
        
        if recognizer.AcceptWaveform(audio_data):
            result = json.loads(recognizer.Result())
            return result['text']
        else:
            result = json.loads(recognizer.PartialResult())
            return result.get('partial', '')

    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None
