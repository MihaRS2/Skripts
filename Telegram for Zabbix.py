# This script will help you send trigger notifications to Telegram

import requests
import sys

# Telegram Configuration
TELEGRAM_TOKEN = 'your_telegram_bot_token'  # Replace with your token
CHAT_ID = 'your_chat_id'  # Replace with your Chat ID

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, json=payload)
    return response.json()

if __name__ == "__main__":
    # The message is passed from Zabbix as a command-line parameter
    if len(sys.argv) < 2:
        print("Usage: send_telegram_notification.py <message>")
        sys.exit(1)

    message = sys.argv[1]
    response = send_telegram_message(message)
    print(response)