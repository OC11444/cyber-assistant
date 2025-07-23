#!/usr/bin/env python3

import os
import subprocess
import re

# Known third-party packages for pip installation
KNOWN_PIP_PACKAGES = {
    "typer": "typer",
    "dotenv": "python-dotenv",
    "rich": "rich",
    "shellingham": "shellingham",
    "vosk": "vosk",
    "pydub": "pydub",
    "speech_recognition": "SpeechRecognition",
    "requests": "requests",
    "openai": "openai",
    "google": "google-generativeai",
    "pyttsx3": "pyttsx3",
    "nltk": "nltk",
    "sklearn": "scikit-learn",
    "cv2": "opencv-python",
    "PIL": "Pillow",
    "flask": "flask"
    # Add more as needed
}

def grep_python_imports(project_dir="."):
    print("🔍 Grep-style scan for imports...")
    imported = set()
    pattern = re.compile(r'^\s*(import|from)\s+([a-zA-Z0-9_\.]+)')
    
    for root, _, files in os.walk(project_dir):
        for fname in files:
            if fname.endswith(".py"):
                with open(os.path.join(root, fname), encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        match = pattern.match(line)
                        if match:
                            module = match.group(2).split('.')[0]
                            imported.add(module)
    return imported

def resolve_to_pip_names(imported_modules):
    return {KNOWN_PIP_PACKAGES[m] for m in imported_modules if m in KNOWN_PIP_PACKAGES}

def install_packages(packages):
    failed = []
    for pkg in packages:
        print(f"📦 Installing: {pkg} ...")
        result = subprocess.run(
            ["pip", "install", pkg],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode != 0:
            print(f"❌ Failed: {pkg}")
            failed.append(pkg)
    return failed

if __name__ == "__main__":
    imports = grep_python_imports()
    resolved = resolve_to_pip_names(imports)

    print("\n📦 Found these pip packages:")
    for r in sorted(resolved):
        print(f" - {r}")

    failed = install_packages(resolved)

    print("\n📄 Freezing installed packages to requirements.txt ...")
    with open("requirements.txt", "w") as f:
        subprocess.run(["pip", "freeze"], stdout=f)

    if failed:
        print("\n❗ Some packages failed to install. Logged in 'failed_deps.txt'")
        with open("failed_deps.txt", "w") as f:
            f.write("\n".join(failed))
    else:
        print("\n✅ All packages installed successfully.")
