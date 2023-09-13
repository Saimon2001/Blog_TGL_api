from schemas.user_schema import User
from fastapi import FastAPI, Body, Depends, HTTPException, Path, Query, status, Request
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session, engine, Base
from models.user_model import User as UserModel
from typing import List
from fastapi import APIRouter
from middlewares.jwt_bearer import JWTBearer

user_router = APIRouter()

@user_router.get("/user", tags=['users'], response_model=List[User], status_code=200, dependencies=[Depends(JWTBearer())])
def get_users() -> List[User]:
    db = Session()
    result = db.query(UserModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#falta get especifico de fecha publicacion y titulo
@user_router.post('/sing_up', tags=['users'], response_model=dict, status_code=201)
async def create_user(user: User) -> dict:
    db = Session()
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code=201, content={'message':'Se ha registrado el usuario'})

@user_router.put('/user/{id}', tags=['users'], response_model=dict, status_code=200)
def update_user(id: int, user: User) -> dict:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message':'No encontrado'})

    result.name = user.name
    result.email = user.email
    result.password = user.password
    result.country = user.country
    result.regiter_time = user.regiter_time
    db.commit()
    return JSONResponse(status_code=200, content={'message':'Se ha modificado el usuario'})

@user_router.delete('/user/{id}', tags=['users'], response_model=dict, status_code=201)
def delete_user(id:int) -> dict:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message':'No encontrado'})
    db.delete(result)
    db.commit() 
    return JSONResponse(status_code=200, content={'message':'Se ha eliminado el usuario'})