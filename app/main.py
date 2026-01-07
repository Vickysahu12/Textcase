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

@app.get("/target")
async def main():
     return{
        "target1":"Crack the cat with 99.54 percentile",
        "target2":"Launch the startup and grow it to atleast 10k user and 1k paying user"
    }

@app.get("/mine")
async def main():
     return{
        "target1":"Just phodna hai CAT kuch bhi karke with 99.54percentile"
    }

@app.post("/")
async def dream():
     return{
          "me":"This year Motto CAT and STARTUP"
     }