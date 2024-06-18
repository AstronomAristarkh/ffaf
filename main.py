from fastapi import FastAPI
import uvicorn

import user
from db import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(user.router, tags=["Users"])

if __name__ == '__main__':
    uvicorn.run("main:app", host = 'localhost', port = 8000, reload = True)