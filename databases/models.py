from .connection import Database
from sqlalchemy import Column, Integer, BigInteger, String, Date
from datetime import datetime
import sqlalchemy as sa

class Users(Database.Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    t_user_id = Column(BigInteger)
    fullname = Column(String)
    username = Column(String)

class Groups(Database.Base):
    __tablename__ = "Groups"
    id = Column(Integer, primary_key=True)
    t_group_id = Column(BigInteger)
    fullname = Column(String)

class UserGroupStats(Database.Base):
    __tablename__ = "UserGroupStats"
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    group_id = Column(BigInteger)
    botan_count = Column(Integer, default=0)

class BotanInfo(Database.Base):
    __tablename__ = "BotanInfo"
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    group_id = Column(BigInteger, unique=True)
    update_time = Column(Date, default=datetime.min)