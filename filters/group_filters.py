from aiogram.dispatcher import filters
from aiogram import types
from databases import stickers

class IsGroup(filters.BoundFilter):
    async def check(self, message:types.Message) -> bool:
        return message.chat.type == types.ChatType.GROUP or message.chat.type == types.ChatType.SUPERGROUP