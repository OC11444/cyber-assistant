# ====imports =========
import os
import platform
import typer
import re
import subprocess
import sys
from dotenv import load_dotenv
# from assistant.core import run_assistant
from assistant.ai_adapter import AIAdapter
from adapters.text_adapter import get_text_input
from adapters.voice_adapter import listen_for_command
from nova_voice.nova import speak_greeting
from shell_interface import execute_shell_command, explain_command

# === Setup ===
load_dotenv()
app = typer.Typer(help="Parrot-GPT: Your Cybersecurity Assistant for Parrot OS")

# ✅ Allow --demo to pass silently to sys.argv use python main.py --demo
@app.callback(invoke_without_command=True)
def main_callback(ctx: typer.Context):
    ctx.allow_extra_args = True
    ctx.ignore_unknown_options = True

# ✅ DEMO mode detection (clean from sys.argv before typer sees it)
DEMO_MODE = "--demo" in sys.argv or not any(
    os.getenv(key) for key in ["OPENAI_API_KEY", "GEMINI_API_KEY"]
)
if "--demo" in sys.argv:
    sys.argv.remove("--demo")
    print("[🧪 DEMO] AIAdapter initialized in DEMO mode.")

os.environ["DEMO_MODE"] = "true" if DEMO_MODE else "false"

# ✅ Instantiate AIAdapter here
ai_adapter = AIAdapter(demo_mode=DEMO_MODE)

# Track if greeting has already been given
greeting_done = False

# === Audio Playback ===
def play_audio(file_path):
    """
    Plays an audio file depending on the OS.
    """
    system = platform.system()
    if system == "Darwin":
        os.system(f"afplay '{file_path}'")
    elif system == "Linux":
        os.system(f"mpg123 '{file_path}'")
    elif system == "Windows":
        os.system(f'start /min wmplayer "{file_path}"')


# === LLM Prompting ===
def ask_gpt(prompt):
    """
    Sends a prompt to the LLM and returns the response.

    Args:
        prompt (str): The user input to send to the LLM.

    Returns:
        str: The LLM's reply as a formatted string.
    """
    if DEMO_MODE:
        # 🧪 Tool-specific mock behavior
        p = prompt.lower()
        if any(word in p for word in ["nmap", "scan", "ports"]):
            return (
                "1. echo 'Scanning mock ports...'\n"
                "2. echo 'Simulated Nmap scan on 192.168.1.0/24'\n"
                "3. echo 'Mock: netstat -tuln'"
            )
        elif any(word in p for word in ["hydra", "brute", "ssh"]):
            return (
                "1. echo 'Running mock Hydra brute-force on SSH port'\n"
                "2. echo 'Trying username/password combinations'\n"
                "3. echo 'Logging attempt results'"
            )
        elif any(word in p for word in ["john", "crack", "hash"]):
            return (
                "1. echo 'Mock John cracking password hashes...'\n"
                "2. echo 'Simulating hash loading'\n"
                "3. echo 'Emulated cracking progress'"
            )
        elif any(word in p for word in ["metasploit", "exploit", "payload"]):
            return (
                "1. echo 'Launching simulated Metasploit payload'\n"
                "2. echo 'Mock: msfconsole -x use exploit/windows/smb/ms17_010_eternalblue'\n"
                "3. echo 'Pretending to open reverse shell'"
            )
        elif any(word in p for word in ["encrypt", "cipher", "gpg"]):
            return (
                "1. echo 'Mock encrypting file with AES-256'\n"
                "2. echo 'Simulating gpg file.gpg'\n"
                "3. echo 'Emulated encryption success message'"
            )
        else:
            return (
                "1. echo 'Running general mock command A'\n"
                "2. echo 'Mock B: touch demo.txt'\n"
                "3. echo 'Demo: ls -la /root'"
            )

    # 🔐 Real prompt to LLM
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
    """
    Extracts numbered command lines from GPT's response.

    Args:
        response (str): LLM response.

    Returns:
        list[str]: List of commands extracted.
    """
    commands = []
    for line in response.splitlines():
        if line.strip().startswith(tuple(str(i) + "." for i in range(1, 10))):
            parts = line.split(".", 1)
            if len(parts) > 1:
                commands.append(parts[1].strip())
    return commands


# === Execute Command ===
def execute_shell(command: str) -> str:
    """
    Executes a command with sudo and returns its output.

    Args:
        command (str): Shell command to execute.

    Returns:
        str: Output from the shell command.
    """
    typer.secho(f"\n[💻] Running: {command}", fg=typer.colors.CYAN)
    if DEMO_MODE:
        return f"[DEMO MODE] Pretending to run: {command}"
    try:
        result = subprocess.run(
            ["sudo"] + command.split(), capture_output=True, text=True
        )
        return result.stdout or result.stderr
    except Exception as e:
        return f"[❌] Execution failed: {str(e)}"


# === Safe Prompt (CI fallback) ===
def safe_prompt(prompt_text: str, default: str = "text") -> str:
    try:
        if not sys.stdin.isatty():
            typer.secho(f"[⚠️  No TTY] Defaulting to '{default}' mode.", fg=typer.colors.YELLOW)
            return default
        return typer.prompt(prompt_text).strip().lower()
    except (EOFError, typer.Abort):
        return default


# === CLI Entry ===
@app.command()
def start():
    """
    Main assistant command. Handles mode selection and prompt execution.
    """
    global greeting_done

    if not greeting_done:
        audio_path = speak_greeting()
        play_audio(audio_path)
        greeting_done = True

    typer.echo("\n🧠 Welcome to Parrot-GPT! Your AI Cybersecurity Assistant 🛡️")

    while True:
        mode = safe_prompt("🎙️ Choose input mode (text/voice) [default: text]", default="text")
        if not mode:
            mode = "text"
        if mode not in ("text", "voice"):
            typer.echo("[❌] Invalid mode. Choose 'text' or 'voice'.")
            continue

        query = get_text_input() if mode == "text" else listen_for_command()
        if not query:
            typer.echo("[⚠️] No input received.")
            continue

        if query.strip().lower() in ("exit", "quit"):
            typer.secho("\n👋 Exiting Parrot-GPT. Goodbye!", fg=typer.colors.YELLOW)
            break

        typer.secho(f"\n[📨] Sending this to GPT:\n{query}", fg=typer.colors.BLUE)

        response = ask_gpt(query)
        typer.secho(f"\n🤖 GPT Suggestions:\n{response}", fg=typer.colors.CYAN)

        commands = extract_command_list(response)
        if not commands:
            typer.secho("[⚠️] No commands detected in response.", fg=typer.colors.RED)
            continue

        # Show numbered commands
        typer.echo("\n🔢 Choose a command to run:")
        for i, cmd in enumerate(commands, 1):
            typer.echo(f"  {i}. {cmd}")

        if not sys.stdin.isatty():
            selected = "1"
        else:
            selected = typer.prompt("\n▶️ Enter command number to run", default="1")

        try:
            command = commands[int(selected.strip()) - 1]
        except (IndexError, ValueError):
            typer.secho("[❌] Invalid selection.", fg=typer.colors.RED)
            continue

        # Execute and explain
        output = execute_shell(command)
        explanation_prompt = (
            f"The command `{command}` returned:\n\n{output}\n\nExplain this clearly."
        )

        if DEMO_MODE:
            explanation = (
                f"The command `{command}` was simulated.\n\n"
                "It represents a typical step in a cybersecurity workflow:\n"
                "- 🔍 **Port scanning** checks for open services\n"
                "- 🔐 **Brute-force attacks** test credentials\n"
                "- 🔄 **Payloads** emulate exploits\n"
                "- 🔒 **Encryption** secures files\n\n"
                "No real actions were taken — this is safe to run in any environment."
            )
        else:
            explanation = ask_gpt(explanation_prompt)

        typer.secho(f"\n📘 GPT Explains:\n{explanation}", fg=typer.colors.GREEN)


# === Launch Fallback ===
if __name__ == "__main__":
    if len(sys.argv) == 1:
        if not greeting_done:
            audio_path = speak_greeting()
            play_audio(audio_path)
            greeting_done = True
        start()
    else:
        app()
