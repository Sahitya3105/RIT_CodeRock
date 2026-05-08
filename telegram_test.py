import asyncio
import os
import sys
from telegram import Bot
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

async def test():
    print(f'Testing Bot with ID: {chat_id}...')
    bot = Bot(token=token)
    try:
        me = await bot.get_me()
        print(f'Bot Name: {me.first_name}')
        await bot.send_message(chat_id=chat_id, text='🚀 *RADAR Telegram Connection Test:* SUCCESSFUL\n\nEverything is set for the demo\.', parse_mode='MarkdownV2')
        print('[SUCCESS] Message sent to Telegram!')
    except Exception as e:
        print(f'[ERROR] Telegram Test Failed: {e}')

if __name__ == '__main__':
    asyncio.run(test())
