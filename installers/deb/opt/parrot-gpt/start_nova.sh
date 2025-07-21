#!/bin/bash
# 🌐 Parrot-GPT Launcher Script

echo "[⚙️] Starting Nova..."

# Activate virtual environment if needed
if [ -d "venv" ]; then
  source venv/bin/activate
fi

# Run the assistant
python3 /opt/parrot-gpt/main.py "$@"

