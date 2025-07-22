#!/usr/bin/env python3

import os
import ast

# Simple mapping for common non-standard libraries
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
    "google.generativeai": "google-generativeai",
}

def extract_imports_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)
    return {node.names[0].name.split('.')[0] for node in ast.walk(tree) if isinstance(node, ast.Import)} | \
           {node.module.split('.')[0] for node in ast.walk(tree) if isinstance(node, ast.ImportFrom) and node.module}

def find_all_imports(project_dir="."):
    imports = set()
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(".py"):
                try:
                    path = os.path.join(root, file)
                    imports.update(extract_imports_from_file(path))
                except Exception as e:
                    print(f"⚠️ Failed to parse {file}: {e}")
    return imports

def resolve_dependencies(imports):
    pip_deps = set()
    for imp in imports:
        if imp in KNOWN_PIP_PACKAGES:
            pip_deps.add(KNOWN_PIP_PACKAGES[imp])
    return pip_deps

if __name__ == "__main__":
    print("🔍 Scanning project for used imports...")
    all_imports = find_all_imports()
    resolved = resolve_dependencies(all_imports)
    
    print("\n📦 Detected third-party dependencies:")
    for pkg in sorted(resolved):
        print(f" - {pkg}")

    with open("requirements_full.txt", "w") as f:
        f.write("\n".join(sorted(resolved)))
    
    print("\n✅ Saved to requirements_full.txt")
