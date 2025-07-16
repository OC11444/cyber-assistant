from datetime import datetime


def get_greeting():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning. I'm Nova, your Parrot assistant."
    elif 12 <= current_hour < 18:
        return "Good afternoon. I'm Nova, your Parrot assistant."
    else:
        return "Good evening. I'm Nova, your Parrot assistant."
