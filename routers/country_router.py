from fastapi import FastAPI, APIRouter, Body, Depends, HTTPException, Path, Query, status, Request
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session, engine, Base


from models.models import Country as CountryModel
from schemas.country_schema import Country

from typing import List

from services.countrie_services import fetch_data_from_external_api,extract_data

from middlewares.jwt_bearer import JWTBearer

country_router = APIRouter()



@country_router.post("/countries",tags=["Country"] )
async def populate_countries_table( new_countrie_list: list ):
    
    original_countrie_list = fetch_data_from_external_api()
    new_countrie_list = extract_data(original_countrie_list)
    
    db = Session()
    for item in new_countrie_list:
        new_country = Country(
            id = item[0],
            name_common = item[1],
            name_official = item[2],
            independent = item[3],
            region = item[4],
            subregion = item[5],
            flag_svg = item[6],
            flag_icon = item[7],
            population = item[8],
            languages = item[9],
            gini = item[10]
        )
        db.add(new_country)
    db.commit()
    return {"message": "Datos de países guardados exitosamente"}


""" @country_router.get("/countries", tags=["Country"], response_model=List[Country], status_code=200)
async def get_all_countries() -> List[Country]:
    db = Session()
    result = db.query(CountryModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
 """
