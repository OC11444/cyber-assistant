# shell_tools.py

import subprocess


def run_shell_command(command):
    """
    Executes a shell command and returns its output or error.

    Args:
        command (str): Shell command to run.

    Returns:
        str: Output or error message.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.strip()
