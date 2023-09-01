from fastapi import APIRouter
from schemas.comment_schema import Comment


from models.models import Comment as CommentModel

from fastapi import FastAPI, Body, Depends, HTTPException, Path, Query, status, Request
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session, engine, Base

comments_router = APIRouter()

@comments_router.post('/comments', tags=['Comment'], response_model=dict, status_code=201)
def create_comment(comment: Comment) -> dict:
    db = Session()
    new_comment = CommentModel(**comment.dict())
    db.add(new_comment)
    db.commit()
    return JSONResponse(status_code=201, content={'message':'Se ha registrado el commentario'})