import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import database_settings

class Database():
    url = sa.engine.url.URL.create(**database_settings)

    engine = sa.create_engine(url, 
        pool_size=10,
        max_overflow=2,
        pool_recycle=300,
        pool_pre_ping=True,
        pool_use_lifo=True
    )
    Base = declarative_base()
    
    @classmethod
    def create_tables(cls):
        cls.Base.metadata.create_all(cls.engine)

    @classmethod
    def connect(cls):
        Session = sessionmaker(cls.engine)
        cls.session = Session()
