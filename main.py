from aiogram import executor

from dispatcher import dp
from utils.set_bot_commands import set_default_commands

import databases
import filters
import handlers
from logs import logger

async def on_startup(dp):
    await set_default_commands(dp)
    logger.info("Start working")
    print("OK")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)