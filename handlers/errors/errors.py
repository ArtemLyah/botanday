from dispatcher import dp, bot
from aiogram import types
from aiogram.utils import exceptions
from config import FATHER_ID

@dp.errors_handler()
async def error_handler(update:types.Update, exception):
    if isinstance(exception, exceptions.BotBlocked):
        await bot.send_message(FATHER_ID, "Bot was blocked")
    await bot.send_message(FATHER_ID, exception.text)
    return True