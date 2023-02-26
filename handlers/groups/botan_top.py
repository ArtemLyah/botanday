from dispatcher import dp
from databases import UserGroupStats, Users, session, sa
from aiogram import filters, types
from filters import IsGroup
from logs import logger

def format_toplist(stats_list):
    result_text = "🧠 Топ 10 розумників в чаті 🧠:\n"
    for i, stats in enumerate(stats_list, 1):
        result_text += f"{i}. <b>{stats[0]}</b> - {stats[1]}\n"
    return result_text

@dp.message_handler(IsGroup(), filters.Command("botan_top"))
async def botan_top(message:types.Message):
    logger.info(f"Get top of botans < group_id={message.chat.id} >")
    stats_list = session.execute(sa.select(Users.fullname, UserGroupStats.botan_count)\
        .join(UserGroupStats, Users.t_user_id == UserGroupStats.user_id)\
            .where(UserGroupStats.group_id == message.chat.id)\
                .order_by(sa.desc(UserGroupStats.botan_count))\
                    .limit(10)
    ).fetchall()
    if stats_list:
        toplist_text = format_toplist(stats_list)
        await message.answer(toplist_text)
    else:
        await message.answer("В чаті нема ботанів 🤯🤯🤯 Може хтось зухвалиться зареєструватись?")