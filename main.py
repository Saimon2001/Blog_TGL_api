from fastapi import FastAPI, Body, Depends, HTTPException, Path, Query, status, Request, Response
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session, engine, Base
from typing import List
import sqlalchemy


from routers.auth_router import auth_router
from routers.healthCheck_router import health
from routers.user_router import user_router
from routers.publication_router import publi_router
from routers.comment_router import comments_router
from routers.plot_router import plot_router
from routers.country_router import country_router


app = FastAPI()
app.title = "🌌🧑🏻‍🚀🧑🏻‍🚀🌌Top Gun Lab: The real blog to boost our career🪐🚀🛸🌎"

app.include_router(health)
app.include_router(user_router)
app.include_router(publi_router)
app.include_router(comments_router)
#app.include_router(plot_router)
app.include_router(country_router)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)


