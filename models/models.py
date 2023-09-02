from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship


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
    
    users = relationship("User", back_populates= "owner")
    
class User(Base):  
    __tablename__ = "users"
    
    
    user_id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String, unique = True)
    password = Column(String)
    country = Column(String, ForeignKey("countries.id"))
    register_time = Column(Float)
    role = Column(String)
    
    publications = relationship("Publication", back_populates= "owner")
    comments = relationship("Comment", back_populates= "owner")
    

class Publication(Base):
    __tablename__ = "publications"

    publication_id = Column( Integer, primary_key = True )
    user_id = Column( Integer, ForeignKey("users.user_id") )
    title = Column( String )
    content = Column( String ) 
    
    owner = relationship("User", back_populates= "publications")
    comments = relationship("Comment", back_populates= "owner")

class Comment(Base):
    __tablename__ = "comments"

    comment_id = Column( Integer, primary_key = True )
    user_id = Column( Integer, ForeignKey("users.user_id") )
    publication_id = Column( Integer, ForeignKey("publications.publication_id") )
    content = Column(String)
    
    owner = relationship("Publication", back_populates= "comments")
    

    
