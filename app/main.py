from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"data":"creating a new project named Textcasepro"}

@app.get("/vicky")
async def me():
    return{"data":"Hey guys I am vicky and I am making an app that can help to the CAT ASPIRANT FOR CRACKING THE CAT"}

@app.get("/dream")
async def me():
    return{"data":"lets fucking start from tomorrow"}

@app.get("/trip")
async def trip():
    return{"data":"sry for everything dude we will gonna crush 30 video in next 2days to start a strong comeback"}
