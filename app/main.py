from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"data":"creating a new project named Textcasepro"}

@app.get("/vicky")
async def me():
    return{"data":"Hey guys I am vicky and I am making an app that can help to the CAT ASPIRANT FOR CRACKING THE CAT"}