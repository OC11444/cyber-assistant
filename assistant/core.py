import os
from dotenv import load_dotenv
import openai
from assistant.shell_tools import run_shell_command
from nova_voice.voice_input import listen_for_command

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def run_assistant():
    print("🔒 Welcome to Parrot-GPT Assistant")
    while True:
        user_input = input("You (type 'voice' to use voice input): ")
        if user_input.lower() == 'voice':
            user_input = listen_for_command()
            if user_input:
                print(f"You (voice): {user_input}")
            else:
                continue

        if user_input.lower() in ["exit", "quit"]:
            break
        if user_input.startswith("!"):
            output = run_shell_command(user_input[1:])
            print(f"Shell: {output}")
            continue
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a shell-savvy cybersecurity assistant on Parrot OS."},
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response['choices'][0]['message']['content']
            print(f"🤖 Parrot-GPT: {reply}")
        except Exception as e:
            print(f"Error: {e}")
