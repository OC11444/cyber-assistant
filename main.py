import os
import typer
from shell_interface import execute_shell_command, explain_command
from dotenv import load_dotenv
import openai
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

api_key = os.getenv("OPENAI_API_KEY")


load_dotenv()
app = typer.Typer()

# Load your OpenAI API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")


def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You're a cybersecurity assistant for Parrot OS. Help convert questions into Linux commands, recommend tools, and explain securely."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=400
    )
    return response['choices'][0]['message']['content'].strip()


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
    app()

