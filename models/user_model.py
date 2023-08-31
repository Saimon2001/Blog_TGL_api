from config.database import Base
from sqlalchemy import Column, Integer, String, Float,   ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from typing import List

#https://fastapi.tiangolo.com/tutorial/sql-databases/
#https://docs.sqlalchemy.org/en/20/orm/relationships.html
#https://www.youtube.com/watch?v=5JZMcCnVm3g

#estas son las tabla de la base de datos
class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    country = Column(String)
    regiter_time = Column(Float)

    children1: Mapped[List["Publication"]] = relationship()
    children2: Mapped[List["Comments"]] = relationship()

class Publication(Base):

    __tablename__ = "Publication"

    publi_id : Mapped[int] = mapped_column(primary_key = True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    comment = Column(String)
    hastags = Column(String)

    children: Mapped[List["Comments"]] = relationship()

class Comments(Base):

    __tablename__ = "Comments"

    comment_id: Mapped[int] = mapped_column(primary_key = True)
    publi_id: Mapped[int] = mapped_column(ForeignKey("Publication.publi_id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    new_comment = Column(String)