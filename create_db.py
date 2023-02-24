from databases.connection import Base, engine

Base.metadata.create_all(engine)