import os
from sqlalchemy.sql.schema import MetaData
import sqlalchemy
from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = '../database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"
#print(database_url)

engine = create_engine(database_url, echo= True)
Session = sessionmaker( bind = engine)
sesion = Session()
Base = declarative_base()
metadata = MetaData()
Base.metadata  = metadata






