from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.automap import automap_base
import os

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

DATABASE_URL = f'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'


engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True
)

SessionLocal = sessionmaker(
    bind=engine, autoflush=False, autocommit=False, class_=Session)

Base = automap_base()

Base.prepare(engine, reflect=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
