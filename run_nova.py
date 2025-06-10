from nova_voice.nova import speak_greeting
import os
import platform

def play_audio(file_path):
    system = platform.system()
    if system == "Darwin":  # macOS
        os.system(f"afplay '{file_path}'")
    elif system == "Linux":
        os.system(f"mpg123 '{file_path}'")
    elif system == "Windows":
        os.system(f'start /min wmplayer "{file_path}"')
    else:
        print("Audio playback not supported on this OS.")

if __name__ == "__main__":
    audio_path = speak_greeting()
    play_audio(audio_path)
