from fastapi import FastAPI, Body, Depends, HTTPException, Path, Query, status, Request, Response
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session, engine, Base
from typing import List

from middlewares.jwt_manager import create_token
from middlewares.jwt_bearer import JWTBearer

from routers.user_router import user_router
from routers.publi_router import publi_router
from routers.comments_router import comments_router
from routers.plot_router import plot_router
from routers.country_router import country_router

app = FastAPI()
app.title = "Blog TGL"

app.include_router(user_router)
app.include_router(publi_router)
app.include_router(comments_router)
app.include_router(plot_router)
app.include_router(country_router)

Base.metadata.create_all(bind=engine)

class auth(BaseModel):
    email: str
    password: str

@app.post('/admin', tags=['auth'], response_model=dict, status_code=200)
def login(user: auth):
    if user.email == 'admin@TGL_blog.com' and user.password == 'admin':
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)