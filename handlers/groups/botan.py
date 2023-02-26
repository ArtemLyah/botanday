from dispatcher import dp
from databases import BotanInfo, UserGroupStats, Users, session, sa
from aiogram import filters, types
from datetime import datetime, timedelta
from utils.text_templates import text_of_choosen_botan
from filters import IsGroup
from logs import logger
import random

def update_tables(botan_UserGroup:UserGroupStats, today):
    update_BotanInfo = {
        BotanInfo.user_id : botan_UserGroup.user_id,
        BotanInfo.update_time : today + timedelta(days=1)
    }
    update_UserGroupStats = {
        UserGroupStats.botan_count : botan_UserGroup.botan_count + 1
    }
    group_id = botan_UserGroup.group_id
    user_id = botan_UserGroup.user_id
    # Update tables
    session.query(BotanInfo)\
        .filter(BotanInfo.group_id == group_id)\
            .update(update_BotanInfo, synchronize_session=False)
    session.query(UserGroupStats)\
        .filter(sa.and_(
            UserGroupStats.group_id == group_id, 
            UserGroupStats.user_id == user_id
        ))\
            .update(update_UserGroupStats, synchronize_session=False)
    session.commit()

@dp.message_handler(IsGroup(), filters.Command("botan"))
async def botan(message:types.Message):
    logger.info(f"Handle botan < group_id={message.chat.id} >")
    botanInfo = session.query(BotanInfo).filter(BotanInfo.group_id == message.chat.id).one()
    today = datetime.now().date()
    if today >= botanInfo.update_time:
        participants_in_group = session.query(UserGroupStats).filter(
            UserGroupStats.group_id == message.chat.id 
        ).all()
        if participants_in_group:
            botan_UserGroup:UserGroupStats = random.choice(participants_in_group) 
            logger.info(f"New botan < user_id={botan_UserGroup.user_id} >")

            update_tables(botan_UserGroup, today)

            botan_User = session.query(Users)\
                .filter(Users.t_user_id == botan_UserGroup.user_id)\
                    .one()
            await message.answer(text_of_choosen_botan(botan_User.username))
        else:
            await message.answer("В чаті нема ботанів 🤯🤯🤯 Може хтось зухвалиться зареєструватись?")
    else:
        botan_User = session.query(Users)\
            .filter(Users.t_user_id == botanInfo.user_id)\
                .one()
        await message.answer(text_of_choosen_botan(botan_User.username))
