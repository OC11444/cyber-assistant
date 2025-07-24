#!/bin/bash

echo "🔧 Cyber Assistant: Full Installer + Launcher"

# Step 1: Ask for sudo password early
echo "🔐 Requesting sudo to install system dependencies (only once)..."
sudo -v

# Step 2: Install system-level dependencies (for PyAudio and other tools)
echo "📦 Installing required system packages..."
sudo apt-get update
sudo apt-get install -y portaudio19-dev python3-venv python3-pyaudio

# Step 3: Set up virtual environment
if [ ! -d "venv" ]; then
  echo "🐍 Creating virtual environment..."
  python3 -m venv venv
fi

# Step 4: Activate virtual environment
echo "🧪 Activating virtual environment..."
source venv/bin/activate

# Step 5: Install Python dependencies
echo "📥 Installing Python dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 6: Choose mode
echo ""
echo "🌐 Choose a mode to launch:"
echo "1. Live Mode"
echo "2. Demo Mode"
read -p "Enter your choice [1/2]: " choice

# Step 7: Launch assistant
if [ "$choice" == "1" ]; then
  echo "🚀 Launching in Live Mode..."
  python main.py --live
elif [ "$choice" == "2" ]; then
  echo "🧪 Launching in Demo Mode..."
  python main.py --demo
else
  echo "❌ Invalid option. Please choose 1 or 2."
  exit 1
fi
