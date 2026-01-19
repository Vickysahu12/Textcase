from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.config import create_tables
from app.account.routers import router as account_router

# Import all models so SQLAlchemy knows them
from app.account.models import User
from app.converter.models import UserCredits, APIKey, CreditRequest

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(account_router)

@app.get("/")
async def root():
    return {"msg": "FastAPI is working, tables are created!"}
