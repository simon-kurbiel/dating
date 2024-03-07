from fastapi import FastAPI, Depends
from .routes import images, users, auth
from . import utils
from typing import Annotated
from . import models
from .database import engine
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(images.router)



@app.get("/")
async def hello():
    
    return {"message": "Hi"}





