# assistant/core.py
# This module verifies if essential tools for the assistant (e.g. nmap, sqlmap) are installed.

import shutil
import os  # retained intentionally for future expansion or tool detection enhancements

# List of external tools required by the assistant
TOOLS = [
    "nmap",
    "sqlmap",
    "john",
    "whois",
    "hydra",
    "curl",
    "ping",
]


def check_tool(tool_name):
    """
    Check if a given tool is available in the system's PATH.

    Args:
        tool_name (str): Name of the tool to check.

    Returns:
        bool: True if the tool exists, False otherwise.
    """
    return shutil.which(tool_name) is not None


def run_assistant():
    """
    Verifies that all required tools are installed on the system.
    Prints the status of each tool and provides installation hints if missing.
    """
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

        print(
            "\n🔐 Please install the missing tools before using related features."
        )
    else:
        print("\n✅ All required tools are available. You're good to go!\n")
