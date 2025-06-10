# 🛡️ Parrot-GPT Assistant

A GPT-powered assistant designed for Parrot OS with shell access support. Securely interact with GPT and your system from the terminal.

## 🚀 Features

- Ask GPT questions about cybersecurity, Linux tools, networking, and more
- Run shell commands directly from the assistant using `!` prefix
- Easily extendable with your own tools

## 🔧 Setup

```bash
# 1. Clone the repo
git clone git@github.com:OC11444/parrot-gpt-assistant.git
cd parrot-gpt-assistant

# 2. Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your OpenAI API key
echo "OPENAI_API_KEY=your-key-here" > .env

# 5. Run the assistant
python main.py

