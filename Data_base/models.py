from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from decouple import config

url = URL.create(
    drivername="mysql",
    username=config("DB_USER"),
    password=config("DB_PASSWORD"),
    host="localhost",
    database="chat_bot",
    port=3306  # Default MySQL port
)

engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String(255))  # Adjust the length based on your needs
    message = Column(String(255))  # Adjust the length based on your needs
    response = Column(String(255))  # Adjust the length based on your needs


Base.metadata.create_all(engine)
