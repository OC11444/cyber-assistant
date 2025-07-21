


---

### `guides/john_the_ripper.md`
```markdown
# 🔐 John the Ripper Basics Guide with Parrot GPT Assistant

## What is John the Ripper?
John the Ripper is a password cracking tool that helps test password strength by brute forcing or using wordlists.

---

## Using John the Ripper with Parrot GPT Assistant

Ask Nova for commands to crack password hashes or to use wordlists. For example:

> "How do I crack a hash file with John the Ripper?"

Nova will give you command options and explain what they do.

---

## Common John Commands

### 1. Crack hashes in a file
```bash
john hashes.txt

<!-- [ADD SCREENSHOT: Nova suggesting john cracking command] -->
2. Use a wordlist

john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

<!-- [ADD SCREENSHOT: Nova suggesting john with wordlist] -->
3. Show cracked passwords

john --show hashes.txt

<!-- [ADD SCREENSHOT: Nova showing cracked passwords] -->
How to Ask Nova

Examples you can say or type:

    "Crack password hashes from file."

    "Use a wordlist with John."

    "Show me the cracked passwords."

Nova will respond with command choices and explanations.
Ethical Reminder

Only crack passwords you have explicit permission to test.
Tips

    Use wordlists for better cracking chances

    Combine with hash cracking tools for advanced usage