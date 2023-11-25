from .connection import Database
from .models import Groups, Users, UserGroupStats, BotanInfo
import sqlalchemy as sa
from config import create_tables

if create_tables:
    Database.create_tables()
    
Database.connect()
session = Database.session
