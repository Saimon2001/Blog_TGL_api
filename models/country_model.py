from config.database import Base
from sqlalchemy import Column, Integer, String

class Countrie(Base):
    
    __tablename__ = "countries"
    
    id = Column( String, primary_key= True)
    name_common = Column( String )
    name_official = Column( String )
    independent = Column( String )
    languages = Column( String )
    region = Column( String )
    subregion = Column( String )
    flag_svg = Column( String )
    flag_icon = Column( String )
    population =  Column( String )
    gini = Column( String )
    