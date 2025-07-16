#====imports =======
import os
import platform
import typer
import re
import subprocess
from dotenv import load_dotenv
from assistant.core import run_assistant
from assistant.ai_adapter import AIAdapter
from adapters.text_adapter import get_text_input
from adapters.voice_adapter import listen_for_command
from nova_voice.nova import speak_greeting
from shell_interface import execute_shell_command, explain_command

# === Setup ===
load_dotenv()
app = typer.Typer(help="Parrot-GPT: Your Cybersecurity Assistant for Parrot OS")
ai_adapter = AIAdapter()

# === Audio Playback ===
def play_audio(file_path):
    system = platform.system()
    if system == "Darwin":
        os.system(f"afplay '{file_path}'")
    elif system == "Linux":
        os.system(f"mpg123 '{file_path}'")
    elif system == "Windows":
        os.system(f'start /min wmplayer \"{file_path}\"')

# === LLM Prompting ===
def ask_gpt(prompt):
    messages = [
        {
            "role": "system",
            "content": (
                "You are Nova, a cybersecurity AI assistant on Parrot OS.\n"
                "For each user prompt, return a list of up to 3 Linux commands.\n"
                "Number them like:\n"
                "1. command\n2. command\n3. command\n"
                "Don't use code blocks or explain yet."
            )
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    return ai_adapter.chat_completion(messages)

# === Extract Numbered Commands ===
def extract_command_list(response: str) -> list[str]:
    commands = []
    for line in response.splitlines():
        if line.strip().startswith(tuple(str(i) + "." for i in range(1, 10))):
            parts = line.split(".", 1)
            if len(parts) > 1:
                commands.append(parts[1].strip())
    return commands

# === Execute Command ===
def execute_shell(command: str) -> str:
    typer.secho(f"\n[💻] Running: {command}", fg=typer.colors.CYAN)
    try:
        result = subprocess.run(["sudo"] + command.split(), capture_output=True, text=True)
        return result.stdout or result.stderr
    except Exception as e:
        return f"[❌] Execution failed: {str(e)}"

# === CLI Entry ===
@app.command()
def start():
    typer.echo("🧠 Welcome to Parrot-GPT!")
    mode = typer.prompt("Choose input mode (text/voice) [default: text]").strip().lower()
    if not mode:
        mode = "text"
    if mode not in ("text", "voice"):
        typer.echo("[❌] Invalid mode. Choose 'text' or 'voice'.")
        raise typer.Exit()

    query = get_text_input() if mode == "text" else listen_for_command()
    if not query:
        typer.echo("[⚠️] No input received.")
        raise typer.Exit()

    typer.secho(f"\n[📨] Sending to GPT:\n{query}", fg=typer.colors.BLUE)

    response = ask_gpt(query)
    typer.secho(f"\n🤖 GPT Suggestions:\n{response}", fg=typer.colors.CYAN)

    commands = extract_command_list(response)
    if not commands:
        typer.secho("[⚠️] No commands detected in response.", fg=typer.colors.RED)
        raise typer.Exit()

    # Show numbered commands
    typer.echo("\n🤖 Choose 1 to run, or another number:")
    for i, cmd in enumerate(commands, 1):
        typer.echo(f"  {i}. {cmd}")

    selected = typer.prompt("\nEnter command number to run", default="1")
    try:
        command = commands[int(selected.strip()) - 1]
    except (IndexError, ValueError):
        typer.secho("[❌] Invalid selection.", fg=typer.colors.RED)
        raise typer.Exit()

    # Execute and explain
    output = execute_shell(command)
    explanation_prompt = f"The command `{command}` returned:\n\n{output}\n\nExplain this clearly."
    explanation = ask_gpt(explanation_prompt)
    typer.secho(f"\n📘 GPT Explains:\n{explanation}", fg=typer.colors.GREEN)

# === Launch Fallback ===
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        audio_path = speak_greeting()
        play_audio(audio_path)
        run_assistant()
        start()
    else:
        app()
