# 🦜 Parrot GPT Assistant

**Parrot GPT Assistant** is an intelligent, voice-enabled terminal companion built for **Parrot OS**. Designed for cybersecurity learners, ethical hackers, and Linux tinkerers, it blends AI, shell interaction, and offline voice synthesis into a hacking-friendly experience. Nova is not just a voice — it’s your first mate in the terminal.

![Nova Voice Terminal Banner](https://i.imgur.com/VYYjMue.png)

---

## 🎯 Key Features

### 🎙️ Voice-Activated Boot Greeting

> Nova greets you with a custom voice message every time you launch your virtual machine.

### 🧠 GPT-Like Terminal Intelligence

> Ask Nova to explain commands, give security tips, or walk you through tool usage.

### 🛠️ Built-In Tool Guides

> From reconnaissance to exploitation, Nova helps with:

* `nmap`
* `sqlmap`
* `john`
* `metasploit`

### ⚙️ Modular Hacking Support

> Specialized modules for:

* Malware analysis
* Hash cracking
* Cipher decoding
* SQL Injection
* OSINT lookups

### 🐚 Shell Integration

> Execute shell commands with contextual help, feedback, and suggestions.

---

## 🧱 Project Structure

```
parrot-gpt-assistant/
├── assistant/            # Core logic & terminal interactions
├── nova_voice/           # Voice greeting engine (Nova)
├── tools/                # Custom hacking modules
├── guides/               # Markdown tutorials for popular tools
├── shell_interface.py    # Connects Nova to your shell
├── run_nova.py           # Greets user at startup
├── sounds/               # Nova's .wav & voice files
├── venv/                 # Python virtual environment
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

### 🔧 1. Clone the Repo

```bash
git clone https://github.com/your-username/parrot-gpt-assistant.git
cd parrot-gpt-assistant
```

### 🧪 2. Set Up the Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ▶️ 3. Run Nova

```bash
python run_nova.py
```

Nova will greet you with a custom voice intro.

---

## 🔊 Make Nova Greet You on VM Boot

### Step 1: Create a Startup Script

```bash
nano ~/start_nova.sh
```

Paste this:

```bash
#!/bin/bash
cd ~/Desktop/parrot-gpt-assistant
source venv/bin/activate
python run_nova.py
```

Make it executable:

```bash
chmod +x ~/start_nova.sh
```

### Step 2: Add to System Startup

**For XFCE or MATE**:

* Go to **Session and Startup** > **Application Autostart**
* Click **Add**

  * **Name**: Nova
  * **Command**: `/home/your-username/start_nova.sh`

---

## 👥 Target Users

* Cybersecurity students
* Penetration testers
* Ethical hackers
* Parrot OS power users
* AI + Linux automation enthusiasts

---

## 🔉 Voice Engine

Nova uses `pyttsx3` for local, offline speech synthesis. You can extend it with:

* Emotion-aware greetings
* Custom voices
* .wav overlays for audio personality

---

## 🔮 Future Possibilities

* Interactive chat-style mode in terminal
* Real-time alerts from logs or scans
* Integration with TryHackMe, HackTheBox
* Web panel + API control for remote Nova instances

---

## 📜 License

**MIT License** – Free to use, modify, and distribute. Credit appreciated.

---

## ✨ Acknowledgements

* 🐧 **Parrot OS** – For a powerful ethical hacking environment
* 🧠 **OpenAI** – For inspiring natural language intelligence
* 🧑‍💻 **You** – For pushing the boundaries of what's possible in your terminal

> "Not just a script. Not just a voice. It's your cyber companion."
> — *Nova the Assistant* ✨🦜

