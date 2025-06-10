from gtts import gTTS
import os
from nova_voice.greetings import get_greeting

def speak_greeting():
    text = get_greeting()
    print(f"[Nova] Speaking: {text}")
    tts = gTTS(text=text, lang='en', tld='co.uk')
    output_dir = os.path.expanduser("~/Desktop/parrot-gpt-assistant/sounds")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "startup.mp3")
    tts.save(output_path)
    return output_path
