#!/usr/bin/env python3

import re

# List of known system-level or non-PyPI packages to exclude
BLACKLIST = {
    "apparmor",
    "dbus",
    "apt",
    "pygobject",
    "gi",
    "xlib",
    "systemd",
    "python-apt",
    "ubuntu-drivers-common",
    "pyxdg",
    "pycairo",
    "lsb-release",
    "dbus-python",
    "gobject",
    "pygobject3",
}

# Optional: regex to match editable or local packages (not from PyPI)
LOCAL_EDITABLE_RE = re.compile(r"^-e\s+|^\.|^file:")

def clean_requirements(input_file="requirements.txt", output_file="requirements_clean.txt"):
    print(f"🧼 Cleaning {input_file}...")

    cleaned_lines = []

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            original = line.strip()
            package_name = re.split(r"[<=>]", original)[0].lower()

            # Skip blacklisted/system-level packages
            if package_name in BLACKLIST:
                print(f"🚫 Skipped system package: {package_name}")
                continue

            # Skip editable/local installs
            if LOCAL_EDITABLE_RE.match(original):
                print(f"🚫 Skipped local/editable package: {original}")
                continue

            cleaned_lines.append(original)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(cleaned_lines))

    print(f"✅ Cleaned requirements saved to {output_file}")
    return output_file

if __name__ == "__main__":
    clean_requirements()
