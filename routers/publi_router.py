from schemas.publi_schema import Publication
from fastapi import APIRouter
from models.user import Publication as PublicationModel
from fastapi import FastAPI, Body, Depends, HTTPException, Path, Query, status, Request
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session, engine, Base

publi_router = APIRouter()


@publi_router.post('/publication', tags=['publi'], response_model=dict, status_code=201)
def create_publi(publi: Publication) -> dict:
    db = Session()
    new_publi = PublicationModel(**publi.dict())
    db.add(new_publi)
    db.commit()
    return JSONResponse(status_code=201, content={'message':'Se ha registrado la publicacion'})