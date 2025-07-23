# 🧠 LLM Shell Assistant

A **cybersecurity-focused voice & text assistant** for ethical hacking, CTFs, and automation. Combines **AI intelligence** (OpenAI + Gemini) with real terminal tools. Works offline in demo mode — ideal for judges and restricted environments.

---

## 🚀 Summary

LLM Shell Assistant helps students, researchers, and cybersecurity enthusiasts quickly get **AI-powered command suggestions, tool explanations, and voice control** — directly from the terminal.

It auto-generates shell commands for password cracking, SQL injection, info gathering, and more. Built-in **DEMO MODE** simulates all responses without internet access.

---

## 🧩 Features

- ✅ **AI Suggestions** (OpenAI + Gemini)
- 🎤 Voice & Text Input
- 🧪 **Offline Demo Mode** (No API needed)
- 🔐 Built-in Ethical Tools:
  - SQLmap
  - John the Ripper
  - Nmap / Rustscan
  - Malware Analysis Tools
- 🧠 LLM Explains Command Output
- 🧰 Fully CLI-Based, No GUI Needed

---

## 🌐 Use Cases

- Ethical Hacking Labs
- CTF Environments
- Air-Gapped or Secure Terminals
- Student/Beginner Training
- Accessible Voice-Controlled Hacking

---

## 📦 Quick Setup

```bash
# 1. Clone the project
git clone https://github.com/OC11444/parrot-gpt-assistant
cd parrot-gpt-assistant

# 2. Install requirements
pip install -r requirements/common.txt

# 3. Copy env
cp .env.example .env
🧪 Demo Mode (Offline)
No API keys or internet required.
# Enable demo mode
DEMO_MODE=true

# Start
python3 main.py
✅ Simulates AI suggestions, tools, and explanations
✅ Ideal for judges or offline labs
🤖 Live Mode (Real AI)
DEMO_MODE=false
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
python3 main.py
🧠 Sample Prompts
Prompt:
scan open ports on 127.0.0.1
Response:
nmap -sV 127.0.0.1
sudo nmap -A 127.0.0.1
Prompt:
crack password hash
Response:
john --wordlist=rockyou.txt hashes.txt
john --incremental hashes.txt
📸 Screenshots (See /docs/screenshots/)
Image	Description
demo-startup.png	Demo Mode welcome
demo-suggestions.png	Simulated shell command options
live-response.png	Actual GPT/Gemini output
voice-mode.png	Voice input example
🔐 Ethics First
Use this tool only in legal, ethical, and educational settings.
Not for real-world exploitation or unauthorized scanning.
🧰 Tech Stack
Python 3.11+
Typer CLI Framework
OpenAI & Gemini APIs
Vosk STT Engine
Tested on Debian, Kali, Parrot OS
🔮 What’s Next
🧩 Tool Plugins (Metasploit, Wireshark)
🎨 Custom Terminal Themes
🐳 Docker + .deb Installers
🌍 Language Packs & Accessibility Modes
🧪 Tests
pytest tests/
📄 License
MIT License — see LICENS