import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')
#print(DATABASE_URI)

# Error with DATABASE_URL being none?
# AttributeError: 'NoneType' object has no attribute '_instantiate_plugins' ???
engine = create_engine(DATABASE_URI)

metadata = MetaData()

events = Table(
    'events',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(80)),
    Column('description', String(250)),
    Column('people', ARRAY(String))
)

database = Database(DATABASE_URI)