from dispatcher import dp, bot
from databases.connection import  Database
from aiogram import types
from aiogram.utils.exceptions import RetryAfter, TerminatedByOtherGetUpdates
from traceback import format_exc
from sqlalchemy.exc import PendingRollbackError, OperationalError
from asyncio import sleep
from config import FATHER_ID
from logs import logger
from databases import session
import os

@dp.errors_handler()
async def error_handler(update:types.Update, exception:Exception):
    if isinstance(exception, RetryAfter):
        logger.warning(exception)
    elif isinstance(exception, (PendingRollbackError, OperationalError)):
        os.system('sudo service postgresql restart')
        await sleep(1)
        session.rollback()
    else:
        await bot.send_message(FATHER_ID, str(exception))
        logger.error("=============================================================")
        logger.exception(format_exc())
        logger.exception("Message information"
            "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"+\
            f"<Chat id: {update.message.chat.id}>\n<From user id: {update.message.from_user.id}>"+\
            "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        await update.message.answer("😢Бот трошки поламався😢\n🛠Зараз розробник все налагодить🛠")
    return True