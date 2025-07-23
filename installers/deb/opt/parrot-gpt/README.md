# 🧠 Parrot-GPT Assistant

Parrot-GPT is a **cybersecurity-focused voice & text assistant** built for Parrot OS. It blends **ethical hacking** capabilities with **AI intelligence** — powered by OpenAI and Gemini — all within a terminal-friendly experience. Whether you're a CTF hacker, student, or ethical pentester, this assistant is designed to **educate, automate, and elevate** your terminal workflows.  

---

## 🗂️ Project Structure

```bash
.
├── adapters/           # 🧩 Input methods (text/voice)
├── assistant/          # 🧠 AI adapters and logic
├── nova_voice/         # 🎤 Voice recognition via Vosk
├── tools/              # 🛠️ Hacking utilities
├── scripts/            # ⚙️ Automation scripts (coming soon)
├── requirements/       # 📦 Dependencies per OS
├── installers/         # 🧰 Cross-platform launchers
├── docs/               # 📚 Guides, docs, and architecture
├── tests/              # ✅ Unit tests
├── guides/             # 🔐 Cybersecurity usage how-tos
├── main.py             # 🚀 Entry point
└── README.md           # 📖 This file

🚀 Core Features

✨ Clean Terminal UI with Numbered Options
🧠 Multi-AI Support (Gemini + OpenAI)
🎙️ Vosk-Powered Voice Input
🧪 DEMO Mode — No API Key Needed
💬 Shell Command Suggestions
📘 AI Explains the Output
🔐 Built-in Ethical Tools:

    Password cracking

    SQL Injection

    Info gathering

    Malware analysis

🧪 DEMO Mode (For Judges & Offline Use)

🔍 No API Key Required. Everything is simulated.

    Copy the example config:

cp .env.example .env

    Set DEMO mode in your .env:

DEMO_MODE=true

    Run the assistant:

python3 main.py

✅ You will enter interactive simulation mode — no network access, but full voice/text input and mocked results for testing.

📸 Insert screenshot of demo mode startup
📸 Insert screenshot of command suggestion & mock explanation
🤖 LIVE AI Mode (Real GPT + Gemini)

Enable real-time AI command generation using LLMs:

    Add your keys in .env:

GEMINI_API_KEY=your_key
OPENAI_API_KEY=your_key
DEMO_MODE=false

    Run:

python3 main.py

💡 Choose between text or voice input dynamically.

📸 Insert screenshot of live LLM output and explanation
💬 Sample Prompts (Work in Both Modes)

Prompt:

    scan open ports on 127.0.0.1

Response:

🤖 Choose one to run:
1. nmap -sV 127.0.0.1
2. sudo nmap -A 127.0.0.1
3. rustscan -a 127.0.0.1 -- -sV -sC

Prompt:

    crack password hash using john

Response:

🤖 Choose one to run:
1. john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
2. john --incremental --format=raw-md5 hashes.txt

Prompt:

    enumerate SQL injection using sqlmap

Response:

🤖 Choose one:
1. sqlmap -u "http://target.com/index.php?id=1" --dbs
2. sqlmap -r request.txt --batch --risk=3 --level=5

📘 Mock explanations are simple, clear, and technical enough for judges & users.
🌈 Coming Soon — UI/UX Customizations

🎨 Terminal Themes
🌀 Shell Animations
⚙️ Command History Replays
🧩 Plugin Tool Support (Wireshark, Metasploit, etc.)
🌐 Language Packs & Accessibility Options
🔐 Ethical Use Policy

🚨 Parrot-GPT is built for legal, educational, and ethical testing only.

Using this on unauthorized systems is illegal and violates Parrot-GPT’s terms of use.
Always ensure you have explicit permission when conducting tests.
📈 Scalability Vision

✅ Fully containerizable (Docker, Podman)
✅ .deb packaging (coming soon)
✅ Cross-platform installers for Linux, Debian, Mac
🔧 Auto-detects voice/text input mode
📡 Works offline in Demo Mode — perfect for isolated VMs
📸 Screenshots (To Be Added)

✅ DEMO Mode: Welcome + command options

✅ DEMO Mode: Mocked output & explanation

✅ LIVE Mode: Real GPT response

✅ Voice Input Interaction

    ✅ Text Input Flow

📁 Place screenshots in the /docs/screenshots/ folder and link them here.
🧪 Testing

Run all tests using:

pytest tests/

🧰 Built With

❤️ Parrot OS Security Edition
🤖 OpenAI + Gemini
🎤 Vosk STT
🐍 Python 3.11+
🖼️ Terminal Art + Typer + Shell
📄 License

MIT — see LICENSE
