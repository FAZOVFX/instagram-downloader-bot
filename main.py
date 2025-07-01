from telethon import TelegramClient, events
from config import Config
from handlers import *
import logging
import asyncio

logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)

client = TelegramClient('bot', Config.API_ID, Config.API_HASH)

async def main():
    await client.start(bot_token=Config.BOT_TOKEN)

    client.add_event_handler(handle_start, events.NewMessage(pattern='/start'))
    client.add_event_handler(handle_help, events.NewMessage(pattern='/help'))
    client.add_event_handler(handle_about, events.NewMessage(pattern='/about'))
    client.add_event_handler(handle_auth, events.NewMessage(pattern='/auth'))
    client.add_event_handler(handle_unauth, events.NewMessage(pattern='/unauth'))
    client.add_event_handler(handle_profile_pic, events.NewMessage(pattern=r'/(dp|profile_pic)\s*'))
    client.add_event_handler(handle_download, events.NewMessage())
    client.add_event_handler(handle_callback, events.CallbackQuery())

    logging.info("🤖 Bot ishga tushdi!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
