from .connection import Database
from .models import Groups, Users, UserGroupStats, BotanInfo
import sqlalchemy as sa
from sqlalchemy.sql.selectable import Select

Database.connect()
session = Database.session