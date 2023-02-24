from dispatcher import dp, bot
from databases.connection import  Database
from aiogram import types
from aiogram.utils.exceptions import RetryAfter, TerminatedByOtherGetUpdates
from sqlalchemy.exc import OperationalError
from config import FATHER_ID
from logs import logger

@dp.errors_handler()
async def error_handler(update:types.Update, exception:Exception):
    if isinstance(exception, RetryAfter):
        logger.warning(exception)
    elif isinstance(exception, OperationalError):
        Database.connect()
    else:
        await bot.send_message(FATHER_ID, str(exception))
        logger.error("=============================================================")
        logger.exception(exception)
        logger.exception("Message information"
            "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"+\
            f"<Chat id: {update.message.chat.id}>\n<From user id: {update.message.from_user.id}>"+\
            "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        await update.message.answer("😢Бот трошки поламався😢\n🛠Зараз розробник все налагодить🛠")
    return True