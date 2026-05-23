from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models.base import Base
from dotenv import load_dotenv
import os

load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")

engine = create_engine(f"postgresql+psycopg2://postgres:{DB_PASSWORD}@localhost/ecommerce", echo=True)

Base.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session
