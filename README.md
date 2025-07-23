

# 🧠 LLM Shell Assistant

A **cybersecurity-focused voice & text assistant** designed for ethical hacking, learning, and automation — combining **AI intelligence** (OpenAI + Gemini) with built-in terminal tools. Ideal for CTFs, pen-testing labs, and offline environments.

---

## ⚙️ CI/CD Workflows

[![🧪 Syntax & Unit Tests](https://github.com/OC11444/parrot-gpt-assistant/actions/workflows/python-ci.yml/badge.svg)](https://github.com/OC11444/parrot-gpt-assistant/actions/workflows/python-ci.yml)
[![🧪 Demo Mode Test](https://github.com/OC11444/parrot-gpt-assistant/actions/workflows/demo-check.yml/badge.svg)](https://github.com/OC11444/parrot-gpt-assistant/actions/workflows/demo-check.yml)
[![🧪 Live Mode Test](https://github.com/OC11444/parrot-gpt-assistant/actions/workflows/live-mode-test.yml/badge.svg)](https://github.com/OC11444/parrot-gpt-assistant/actions/workflows/live-mode-test.yml)

| Workflow         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| Syntax & Unit    | Runs `flake8` checks and test cases to validate syntax and behavior         |
| Demo Mode        | Ensures offline/demo-mode CLI works with mocked AI responses                |
| Live Mode        | Runs a real command with actual API keys to verify LLM integration works    |

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

    ✨ Terminal UI with Numbered Options

    🧠 Multi-AI Support (Gemini + OpenAI)

    🎙️ Voice Input via Vosk

    🧪 Demo Mode — No API Key Required

    💬 Shell Command Suggestions + LLM Explanations

    🔐 Built-in Ethical Tools:

        Password Cracking

        SQL Injection

        Info Gathering

        Malware Analysis

🧪 DEMO Mode (Offline for Judges)

    No API key required. Works in restricted/air-gapped systems.

# Copy example environment
cp .env.example .env

# Enable demo mode
DEMO_MODE=true

# Start assistant
python3 main.py

    ✅ No network access needed

    ✅ Simulated AI + tool output

    ✅ Works with voice or text input

📸 Screenshots to be added:

    Demo Mode Welcome

    Simulated Command Suggestions

    Mock Output + Explanations

🤖 LIVE Mode (Real AI Output)

    Run actual LLM-based command suggestions using OpenAI/Gemini.

# In .env
DEMO_MODE=false
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key

# Run assistant
python3 main.py

💡 Supports both voice and text input.

📸 Screenshots to be added:

    Real GPT/Gemini Output

    Voice Interaction Sample

    Tool Selection via Numbered UI

💬 Example Prompts (Both Modes)

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

🖼️ Screenshots

Please place all screenshots in:

/docs/screenshots/

Screenshot	Description
demo-startup.png	Demo Mode welcome + banner
demo-suggestions.png	Simulated options UI
demo-explanation.png	Mock LLM explanation
live-response.png	Actual GPT/Gemini reply
voice-mode.png	Live voice input interaction
🌈 Coming Soon

    🎨 Terminal Themes

    🌀 Shell Animations

    ⚙️ Command History Replays

    🧩 Tool Plugins (e.g. Metasploit, Wireshark)

    🌐 Language Packs & Accessibility

🔐 Ethical Use

    ⚠️ Use this tool only in legal and ethical contexts.

This project is strictly for:

    Educational use

    CTFs and ethical hacking labs

    Pentesting with permission

Unauthorized use may violate laws and terms of use.
📈 Scalability Goals

    ✅ Works Offline in Demo Mode

    ✅ Cross-Platform: Debian, Parrot, Kali

    ✅ Auto-detects Input Type (Text/Voice)

    ✅ Docker & .deb Packaging Coming Soon

🧪 Running Tests

pytest tests/

🧰 Built With

    ❤️ Parrot OS Security Edition

    🤖 OpenAI & Gemini

    🎤 Vosk STT Engine

    🐍 Python 3.11+

    🖼️ Typer + Shell Styling

📄 License

MIT — see LICENSE