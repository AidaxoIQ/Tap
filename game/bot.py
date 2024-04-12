import telethon
import asyncio
from telethon import functions, types
from telethon.sync import TelegramClient


async def main():
    
    bot = telethon.TelegramClient(
        session = 'bot',
        api_id = 26477451,
        api_hash= '027df208fe06c14ae69fbbdd7cfe145b'
     )
    
    bot_token = '7058701875:AAF18KpPTH3iZNjYQFPQnmn-3rIxwIZ6w8M'

    
    @bot.on(telethon.events.NewMessage())
    async def handler(event):
        
        if event.text.startswith('/'): # Команды
            
            if event.text.lower() == '/start':
                await bot.send_message(
                    entity = event.sender, 
                    message= 'Привет)', 
                    buttons=[
                                types.KeyboardButtonWebView(
                                    "Начать игру",
                                    "file:///C:/Users/Milan/Desktop/game/index.html",
                                )
                            ]
                    )
    
    await bot.start(bot_token=bot_token)
    await bot.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())