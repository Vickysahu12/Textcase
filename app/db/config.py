from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from typing import Generator
import os

# --- Database path ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "vicky.db")
DATABASE_URL = f"sqlite:///{db_path}"

# --- Engine ---
engine = create_engine(
    DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)

# --- Base for models ---
Base = declarative_base()

# --- Session ---
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Create tables ---
def create_tables():
    from app.account.models import User
    from app.converter.models import UserCredits, APIKey, CreditRequest
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
