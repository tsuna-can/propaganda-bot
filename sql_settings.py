#sql_settings.py
import os
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

PSQL_USER = os.environ['PSQL_USER']
PSQL_PASSWORD = os.environ['PSQL_PASSWORD']
PSQL_HOST = os.environ['PSQL_HOST']
PSQL_DB = os.environ['PSQL_DB']
DATABASE = 'postgresql+psycopg2://{user}:{password}@{host}/{db}'\
                       .format(user=PSQL_USER, password=PSQL_PASSWORD, host=PSQL_HOST, db=PSQL_DB)

# ##########localのDB############
# DATABASE = 'postgresql+psycopg2://{user}:{password}@{host}/{db}'\
#                        .format(user='postgres', password='passsonglists', host='localhost', db="propaganda_song")
# ###########################

ENGINE = create_engine(DATABASE, encoding='utf-8', echo=True)

Session = sessionmaker(
    autocommit = False,
    autoflush = True,
    bind = ENGINE)
session = Session()

Base = declarative_base()

class SongList(Base):
    __tablename__ = "songlist"
    id = Column('id', Integer, primary_key=True,  autoincrement=True)
    song_name = Column('song_name', String, nullable=False)
    comments = Column('comments', String)
    url = Column('url', String)
    tourokusya = Column('tourokusya', String, default="名無しの宣教師")
    num_hukyo = Column('num_hukyo', Integer)

Base.metadata.create_all(ENGINE)