from dispatcher import dp
from databases import Users, UserGroupStats, session, sa
from aiogram import filters, types
from filters import IsGroup
from logs import logger

@dp.message_handler(IsGroup(), filters.Command("botan_reg"))
async def botan_reg(message:types.Message):
    logger.info(f"Registration new user < group_id= {message.chat.id}, user_id={message.from_user.id} >")
    is_user_in_Users = session.query(Users).filter(Users.t_user_id == message.from_user.id).all()
    is_user_Registed = session.query(UserGroupStats).filter(sa.and_(
        UserGroupStats.user_id == message.from_user.id,
        UserGroupStats.group_id == message.chat.id
    )).all()

    if not is_user_in_Users:
        session.add(
            Users(
                t_user_id = message.from_user.id, 
                fullname = message.from_user.full_name,
                username = message.from_user.username
            )
        )
        session.commit()
    if not is_user_Registed:
        session.add(
            UserGroupStats(
                user_id = message.from_user.id,
                group_id = message.chat.id
            )
        )
        session.commit()
        await message.reply(f"Реєстрація пройшла успішно.")
    else:
        await message.answer("Хей... Ти вже разеєстрований.")