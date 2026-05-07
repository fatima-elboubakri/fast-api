from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from app.db.database import engine

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

Base.metadata.create_all(bind=engine)