from config.database import Base
from sqlalchemy import Column, Integer, String, Float,   ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

#https://fastapi.tiangolo.com/tutorial/sql-databases/
#https://docs.sqlalchemy.org/en/20/orm/relationships.html
#https://www.youtube.com/watch?v=5JZMcCnVm3g

#esta es la tabla de la base de datos
class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    country = Column(String)
    regiter_time = Column(Float)

class Publication(Base):

    __tablename__ = "Publication"

    publi_id = Column(Integer, primary_key = True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    comment = Column(String)
    hastags = Column(String)