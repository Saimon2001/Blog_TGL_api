from config.database import Base, metadata, engine
from sqlalchemy.types import Integer, String, Boolean, Float
from sqlalchemy.orm import relationship, mapper
from sqlalchemy.sql.schema import Column , ForeignKey
from schemas.country_schema import Country as CountrySchema
import weakref

class Country(Base):
    __tablename__ = "countries"
    
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
    
    def __weakref__ (self):
        return weakref.ref(self)
    #users = relationship("users", back_populates= "countries")
    
class User(Base):  
    __tablename__ = "users"
    
    
    user_id = Column(Integer, unique= True ,  primary_key = True, index = True, nullable= False)
    name = Column(String)
    email = Column(String, unique = True, nullable= False)
    password = Column(String)
    country = Column(String, ForeignKey("countries.id"))
    register_time = Column(Float)
    role = Column(String)
    
    publications = relationship("publications", back_populates= "users")
    #comments = relationship("comments", back_populates= "users")
    

class Publication(Base):
    __tablename__ = "publications"

    publication_id = Column( Integer, primary_key = True, index = True, nullable= False)
    user_id = Column( Integer, ForeignKey("users.user_id") )
    title = Column( String )
    content = Column( String ) 
    
    #user = relationship("users", back_populates= "publications")
    comments = relationship("comments", back_populates= "publications")

class Comment(Base):
    __tablename__ = "comments"

    comment_id = Column( Integer, primary_key = True )
    user_id = Column( Integer, ForeignKey("users.user_id") )
    publication_id = Column( Integer, ForeignKey("publications.publication_id") )
    content = Column(String)
    
    #publication = relationship("publications", back_populates= "comments")
    

metadata.create_all(bind= engine)

#mapper( CountrySchema ,Country)