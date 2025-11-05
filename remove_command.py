import asyncio
from aiogram import Bot
from aiogram.types import BotCommandScopeDefault, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats
from config import BOT_KEY

async def remove_all_commands():
    bot = Bot(token=BOT_KEY)

    await bot.set_my_commands([], scope=BotCommandScopeDefault())
    await bot.set_my_commands([], scope=BotCommandScopeAllPrivateChats())
    await bot.set_my_commands([], scope=BotCommandScopeAllGroupChats())

    await bot.session.close()
    print("🔥 Все команды удалены из Telegram!")

if __name__ == "__main__":
    asyncio.run(remove_all_commands())
