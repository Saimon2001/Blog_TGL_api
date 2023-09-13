from pydantic import BaseModel, Field
from typing import Optional, List


class Country(BaseModel):
    
    id: str = Field(min_length=1, max_length=15)
    name_common: str = Field(min_length=3, max_length=1000)
    name_official: str = Field(min_length=3, max_length=1000)
    independent: bool
    languages: str = Field(min_length=3, max_length=1000)
    region: str = Field(min_length=3, max_length=1000)
    subregion: str = Field(min_length=3, max_length=1000)
    flag_svg: str = Field(min_length=3, max_length=1000)
    flag_icon: str = Field(min_length=3, max_length=1000) 
    population: int
    gini: float

    class Config:
        orm_mode = True
        
        schema_extra = {
            'example': {
                'id': 'CO',
                'name_common': 'Colombia',
                'name_official': 'Republic of Colombia',
                'independent': True,
                'languages': 'Spanish',
                'region': 'Americas',
                'subregion': 'South America',
                'flag_svg': "https://flagcdn.com/co.svg",
                'flag_icon': "🇨🇴",
                'population': 50882884,
                'gini': 51.3
                
            }
        }