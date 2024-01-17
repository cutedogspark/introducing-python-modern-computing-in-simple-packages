from fastapi import FastAPI

from platform import python_version



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/version")
async def root():
    return {"python version ": python_version()}
