from pydantic import BaseModel, Field
from typing import Optional, List


class Country(BaseModel):
    
    id: str = Field(min_length=1, max_length=15)
    name_common: str = Field(min_length=3, max_length=200)
    name_official: str = Field(min_length=3, max_length=200)
    independent: str = Field(min_length=3, max_length=15)
    languages: str = Field(min_length=3, max_length=15)
    region: str = Field(min_length=3, max_length=15)
    subregion: str = Field(min_length=3, max_length=15)
    flag_svg: str = Field(min_length=3, max_length=15)
    flag_icon: str = Field(min_length=3, max_length=15) 
    population: float
    gini = float

    class Config:
        schema_extra = {
            'example': {
                'id': 'CO',
                'name_common': 'Colombia',
                'name_official': 'Republic of Colombia',
                'independent': 'pass',
                'languages': 'Colombia',
                'region': 'Americas',
                'subregion': 'South America',
                'flag_svg': "https://flagcdn.com/co.svg",
                'flag_icon': "🇨🇴",
                'population': 50882884,
                'gini': 51.3,
                
            }
        }