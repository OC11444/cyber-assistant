guides/nmap_basics.md

# 🌐 Nmap Basics Guide with Parrot GPT Assistant

## What is Nmap?
Nmap ("Network Mapper") is a popular open-source tool used for network discovery and security auditing. It helps scan ports, discover hosts, and identify services.

---

## Using Nmap with Parrot GPT Assistant

Nova can help you generate and explain Nmap commands based on your query. For example, ask:

> "How do I scan open ports on 192.168.1.1?"

Nova will suggest a safe Nmap command and provide alternatives.

---

## Common Nmap Commands

### 1. Simple port scan
```bash
nmap 192.168.1.1

<!-- [ADD SCREENSHOT: Nova suggests basic nmap scan command] -->
2. Scan with service version detection

nmap -sV 192.168.1.1

<!-- [ADD SCREENSHOT: Nova suggests nmap with -sV] -->
3. Scan a subnet

nmap 192.168.1.0/24

<!-- [ADD SCREENSHOT: Nova suggesting subnet scan] -->
4. Aggressive scan (more info)

nmap -A 192.168.1.1

<!-- [ADD SCREENSHOT: Nova suggesting aggressive scan] -->
How to Ask Nova

Examples of voice/text inputs you can say:

    "Scan all ports on my local network."

    "Show me services running on 10.0.0.5"

    "Help me do an aggressive scan on 192.168.1.10"

Nova will respond with command options and explanations.
Ethical Reminder

Always have permission before scanning any network or host. Unauthorized scanning can be illegal.
Tips

    Use the numbered menu to select the command to run

    Ask Nova to explain command outputs for better understanding