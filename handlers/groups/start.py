from dispatcher import dp
from aiogram import filters, types
from databases import session, Groups, BotanInfo
from filters import IsGroup

@dp.message_handler(IsGroup(), filters.CommandStart())
async def start(message:types.Message):
    await message.answer(
        "🤓 Ботан дня 🤓 покаже хто у вашому чаті справжній розумник.\n"
        "Команди:\n"
        "/help - Вивести список команд\n"
        "/botan_reg - Зареєструватися у <b>ботан дня</b>\n"
        "/botan - Показати ботана дня\n"
        "/botan_leave - Покинути ботан дня\n"
        "/botan_top - Вивести топ розумників\n"
        "/botan_me - Показати мою статистику\n"
    )
    is_group_in_Groups = session.query(Groups)\
            .filter(Groups.t_group_id == message.chat.id).all()
    is_group_in_BotanInfo = session.query(BotanInfo)\
            .filter(BotanInfo.group_id == message.chat.id).all()

    if not is_group_in_Groups:
        session.add(Groups(
            t_group_id = message.chat.id, 
            fullname = message.chat.full_name
        ))
        session.commit()
    if not is_group_in_BotanInfo:
        session.add(
            BotanInfo(group_id = message.chat.id)
        )
        session.commit()

@dp.message_handler(IsGroup(), filters.CommandHelp())
async def help(message:types.Message):
    await message.answer(
        "🤓 Ботан дня 🤓 покаже хто у вашому чаті справжній розумник.\n"
        "Команди:\n"
        "/help - Вивести список команд\n"
        "/botan_reg - Зареєструватися у <b>ботан дня</b>\n"
        "/botan - Показати ботана дня\n"
        "/botan_leave - Покинути ботан дня\n"
        "/botan_top - Вивести топ розумників\n"
        "/botan_me - Показати мою статистику\n"
    )