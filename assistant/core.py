# assistant/core.py

import shutil
import os

TOOLS = [
    "nmap",
    "sqlmap",
    "john",
    "whois",
    "hydra",
    "curl",
    "ping"
]

def check_tool(tool_name):
    return shutil.which(tool_name) is not None

def run_assistant():
    print("\n🔧 [System Check] Verifying required tools...\n")

    missing = []
    for tool in TOOLS:
        if check_tool(tool):
            print(f"[✔️] {tool} is installed.")
        else:
            print(f"[❌] {tool} is missing.")
            missing.append(tool)

    if missing:
        print("\n⚠️ Some tools are missing:")
        for tool in missing:
            print(f"   - {tool} → To install: `sudo apt install {tool}`")
        print("\n🔐 Please install the missing tools before using related features.")
    else:
        print("\n✅ All required tools are available. You're good to go!\n")
