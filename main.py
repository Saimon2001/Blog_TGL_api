from fastapi import FastAPI, Body, Depends, HTTPException, Path, Query, status, Request
from pydantic import BaseModel, Field
from jwt_manager import create_token, validate_token
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
from config.database import Session, engine, Base
from models.user import User as UserModel
from models.user import Publication as PublicationModel
from typing import Optional, List

app = FastAPI()
app.title = "Blog TGL"

Base.metadata.create_all(bind=engine)

class User(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=3, max_length=15)
    email: str = Field(min_length=5)
    password: str = Field(min_length=3, max_length=15)
    country: str = Field(min_length=3, max_length=15)
    regiter_time: float

    class Config:
        schema_extra = {
            'example': {
                'id':1,
                'name': 'nombre apellido',
                'email': 'name@gmail.com',
                'password': 'pass',
                'country': 'Colombia',
                'regiter_time': 2
            }
        }

class Publication(BaseModel):
    publi_id: int
    user_id: int
    comment: str
    hastags: str

class auth(BaseModel):
    email: str
    password: str

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@TGL_blog.com":
            return HTTPException(status_code=403, detail="Credenciales no son validas")

@app.post('/admin', tags=['auth'], response_model=dict, status_code=200)
def login(user: auth):
    if user.email == 'admin@TGL_blog.com' and user.password == 'admin':
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)

@app.get("/user", tags=['users'], response_model=List[User], status_code=200, dependencies=[Depends(JWTBearer())])
def get_users() -> List[User]:
    db = Session()
    result = db.query(UserModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#falta get especifico de fecha publicacion y titulo
@app.post('/sing_up', tags=['users'], response_model=dict, status_code=201)
async def create_user(user: User) -> dict:
    db = Session()
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code=201, content={'message':'Se ha registrado el usuario'})

@app.post('/publication', tags=['publi'], response_model=dict, status_code=201)
def create_publi(publi: Publication) -> dict:
    db = Session()
    new_publi = PublicationModel(**publi.dict())
    db.add(new_publi)
    db.commit()
    return JSONResponse(status_code=201, content={'message':'Se ha registrado la publicacion'})

@app.put('/user/{id}', tags=['users'], response_model=dict, status_code=200)
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

@app.delete('/user/{id}', tags=['users'], response_model=dict, status_code=201)
def delete_user(id:int) -> dict:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message':'No encontrado'})
    db.delete(result)
    db.commit() 
    return JSONResponse(status_code=200, content={'message':'Se ha eliminado el usuario'})