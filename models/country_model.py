from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class Country(Base):
    
    __tablename__ = "Countries"
    
    id = Column( String, primary_key= True)
    name_common = Column( String )
    name_official = Column( String )
    independent = Column( Boolean )
    languages = Column( String )
    region = Column( String )
    subregion = Column( String )
    flag_svg = Column( String )
    flag_icon = Column( String )
    population =  Column( Integer )
    gini = Column( Float )
