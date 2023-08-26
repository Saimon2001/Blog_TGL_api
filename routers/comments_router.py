from fastapi import APIRouter
from schemas.comments_schema import Comments
from models.user import Comments as CommentsModel
from fastapi import FastAPI, Body, Depends, HTTPException, Path, Query, status, Request
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session, engine, Base

comments_router = APIRouter()

@comments_router.post('/comments', tags=['comments'], response_model=dict, status_code=201)
def create_comment(comment: Comments) -> dict:
    db = Session()
    new_comment = CommentsModel(**comment.dict())
    db.add(new_comment)
    db.commit()
    return JSONResponse(status_code=201, content={'message':'Se ha registrado el commentario'})