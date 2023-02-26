from dispatcher import dp
from databases import UserGroupStats, session, sa
from aiogram import filters, types
from filters import IsGroup
from logs import logger

@dp.message_handler(IsGroup(), filters.Command("botan_leave"))
async def botan_leave(message:types.Message):
    logger.info(f"Leave user from botanDay < group_id={message.chat.id}, user_id={message.from_user.id} >")
    is_user_Registed = session.query(UserGroupStats).filter(sa.and_(
        UserGroupStats.user_id == message.from_user.id,
        UserGroupStats.group_id == message.chat.id
    )).all()
    if is_user_Registed:
        session.delete(is_user_Registed[0])
        session.commit()
        await message.reply("⚠️ Увага ⚠️ бОтан вийшов з гри...")
    else:
        await message.reply("Хей... Ти не разеєстрований.\n/botan_reg - Зареєструватись у <b>ботан дня</b>")