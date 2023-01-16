from aiogram.dispatcher import filters
from aiogram import types

# creating filters we must to create a method check
# this method will be check a message on a certain condition
# BoundFilter - main class of filters
# result must be Boolean
class CommandBot(filters.BoundFilter):
    async def check(self, message:types.Message) -> bool:
        return message.text.startswith("/bot")