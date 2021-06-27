import os
import databases
from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ARRAY)
from databases import Database


DATABASE_URI = os.getenv('DATABASE_URI')
engine = create_engine(DATABASE_URI)


metadata = MetaData()

JobProfile = Table(
    'JobProfile',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('experience', String(50)),
    Column('location', String(50)),
    Column('details', String(200))
)

database = Database(DATABASE_URI)