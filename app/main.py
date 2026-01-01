from fastapi import FastAPI 
from contextlib import asynccontextmanager
from app.db.config import create_tables
# from app.account.models import User,RefreshToken
from app.account.routers import router as account_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(account_router)

@app.get("/me")
async def main():
     return{
        "me":"Hey Guys I am vickyyy",
        "dream":"I want to be an entreprenuer and crack the cat 2026"
    }

async def me():
     return{
          "vicky":"Hyy guys I am vicky you are seeing the richest person of odisha"
     }

async def vicky():
     return{
          "vicky":"Hyy guys I am vicky you are seeing the richest person of odisha"
     }