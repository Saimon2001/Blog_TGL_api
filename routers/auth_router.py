from schemas.auth_schema import auth

from middlewares.jwt_manager import create_token
from middlewares.jwt_bearer import JWTBearer

from fastapi import FastAPI, Body, Depends, HTTPException, Path, Query, status, Request
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session, engine, Base


auth_router = FastAPI()

@auth_router.post('/admin', tags=['Authenticator'], response_model=dict, status_code=200)
def login(user: auth):
    if user.email == 'admin@TGL_blog.com' and user.password == 'admin':
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)