#!/usr/bin/env python3
import os
import subprocess
import sys
import venv

# Known safe dependencies
packages = [
    "requests",
    "python-dotenv",
    "SpeechRecognition",
    "vosk",
    "openai",
    "google-generativeai",
    "rich",
    "Pillow",
    "typer",
    "shellingham",
]

venv_dir = "venv"

def create_venv():
    if not os.path.exists(venv_dir):
        print(f"📦 Creating virtual environment at ./{venv_dir}")
        venv.create(venv_dir, with_pip=True)
    else:
        print("✅ Virtual environment already exists.")

def get_pip_path():
    pip_path = os.path.join(venv_dir, "bin", "pip") if os.name != "nt" else os.path.join(venv_dir, "Scripts", "pip.exe")
    return pip_path

def install_packages(pip_path):
    failed = []
    for pkg in packages:
        print(f"📥 Installing {pkg}...")
        try:
            subprocess.run([pip_path, "install", pkg], check=True)
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {pkg}")
            failed.append(pkg)
    return failed

def freeze_requirements(pip_path):
    print("📌 Freezing to requirements.txt...")
    with open("requirements.txt", "w") as f:
        subprocess.run([pip_path, "freeze"], stdout=f)
    print("✅ requirements.txt saved.")

def main():
    create_venv()
    pip_path = get_pip_path()
    failed = install_packages(pip_path)

    if failed:
        print("⚠️ Some packages failed to install.")
        with open("failed.txt", "w") as f:
            f.write("\n".join(failed))
        print("❗ Failed installs saved to failed.txt")

    freeze_requirements(pip_path)
    print("\n✅ Setup complete. To activate venv:\n")
    print(f"   source {venv_dir}/bin/activate" if os.name != "nt" else f"   {venv_dir}\\Scripts\\activate.bat")

if __name__ == "__main__":
    main()
