import asyncio
import os
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TELEGRAM_BOT_TOKEN')

async def check():
    bot = Bot(token=token)
    print('Checking recent messages to bot...')
    updates = await bot.get_updates()
    for u in updates:
        if u.message:
            print(f'FOUND MESSAGE: "{u.message.text}" from Chat ID: {u.message.chat.id}')
            print(f'Chat Title: {u.message.chat.title}')
    if not updates:
        print('No new messages found. Please send "hi" to the bot again now.')

if __name__ == '__main__':
    asyncio.run(check())
