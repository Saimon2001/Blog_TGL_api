from schemas.publi_schema import Publication
from fastapi import APIRouter
from models.user_model import Publication as PublicationModel
from fastapi import FastAPI, Body, Depends, HTTPException, Path, Query, status, Request
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session, engine, Base
from typing import List

publi_router = APIRouter()

@publi_router.post('/publication', tags=['publi'], response_model=dict, status_code=201)
def create_publi(publi: Publication) -> dict:
    db = Session()
    new_publi = PublicationModel(**publi.dict())
    db.add(new_publi)
    db.commit()
    return JSONResponse(status_code=201, content={'message':'Se ha registrado la publicacion'})

@publi_router.get('/publication', tags=['publi'], response_model=List[Publication], status_code=200)
def get_publi() -> List[Publication]:
    db = Session()
    result = db.query(PublicationModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@publi_router.put('/publication/{id}', tags=['publi'], response_model=dict, status_code=200)
def update_publi(id: int, publi: Publication) -> dict:
    db = Session()
    result = db.query(PublicationModel).filter(PublicationModel.publi_id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message':'No encontrado'})

    result.user_id = publi.user_id
    result.comment = publi.comment
    result.hastags = publi.hastags
    db.commit()
    return JSONResponse(status_code=200, content={'message':'Se ha modificado la publicacion'})

@publi_router.delete('/publication/{id}', tags=['publi'], response_model=dict, status_code=201)
def delete_publi(id:int) -> dict:
    db = Session()
    result = db.query(PublicationModel).filter(PublicationModel.publi_id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message':'No encontrado'})
    db.delete(result)
    db.commit() 
    return JSONResponse(status_code=200, content={'message':'Se ha eliminado la publi'})