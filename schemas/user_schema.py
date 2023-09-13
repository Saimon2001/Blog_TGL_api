from pydantic import BaseModel, Field
from typing import Optional, List
from schemas.publication_schema import Publication
from schemas.comment_schema import Comment


class User(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=3, max_length=15)
    email: str = Field(min_length=5)
    password: str = Field(min_length=3, max_length=15)
    country: str = Field(min_length=3, max_length=200)
    regiter_time: float
    role: str = (Field(min_length=3, max_length=15))
    publications: list[Publication]
    comments: list[Comment]
    
    class Config:
        orm_mode = True
        
        schema_extra = {
            'example': {
                'id':1,
                'name': 'nombre apellido',
                'email': 'name@gmail.com',
                'password': 'pass',
                'country': 'Colombia',
                'regiter_time': 2,
                'role': 'admin'
            }
        }