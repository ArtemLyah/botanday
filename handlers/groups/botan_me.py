from dispatcher import dp
from databases import UserGroupStats, session, sa
from aiogram import filters, types

@dp.message_handler(filters.Command("botan_me"))
async def botan_me(message:types.Message):
    user_stats = session.execute(sa.select(UserGroupStats.botan_count).where(sa.and_(
        UserGroupStats.group_id == message.chat.id,
        UserGroupStats.user_id == message.from_user.id
    ))).fetchall()
    if user_stats:
        await message.answer(f"✍️ Твій рівень ботанства становить - <b>{user_stats[0][0]}</b>")
    else:
        await message.answer("Хей... Ти не разеєстрований.\n/botan_reg - Зареєструватись у <b>ботан дня</b>")
    