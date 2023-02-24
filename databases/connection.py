import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import database_settings

class Database():
    url = sa.engine.url.URL.create(**database_settings)

    engine = sa.create_engine(url)
    Base = declarative_base()
    

    @classmethod
    def connect(cls):
        Session = sessionmaker(cls.engine)
        cls.session = Session()
