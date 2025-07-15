import os
import typer
from shell_interface import execute_shell_command, explain_command
from dotenv import load_dotenv
from nova_voice.nova import speak_greeting
import platform
from assistant.ai_adapter import AIAdapter

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

from assistant.core import run_assistant

load_dotenv()
app = typer.Typer()
ai_adapter = AIAdapter()

def ask_gpt(prompt):
    messages = [
        {"role": "system", "content": "You're a cybersecurity assistant for Parrot OS. Help convert questions into Linux commands, recommend tools, and explain securely."},
        {"role": "user", "content": prompt}
    ]
    return ai_adapter.chat_completion(messages, model="gpt-4")


@app.command()
def ask(question: str):
    typer.echo(f"🧠 Asking Parrot Assistant: {question}")
    response = ask_gpt(question)
    typer.echo(f"\n🔍 GPT Suggestion:\n{response}")

    confirm = typer.confirm("\n⚠️ Do you want to run this command?")
    if confirm:
        execute_shell_command(response)
        explain_command(response)


if __name__ == "__main__":
    audio_path = speak_greeting()
    play_audio(audio_path)
    run_assistant()
    app()

