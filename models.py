from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
from db import engine

Base = declarative_base()

#Sqlalchemy models
class BaseModello(Base):
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)

class Magazzino(BaseModello):
    __tablename__ = 'magazzino'

    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer)


class Item(BaseModello):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)

Base.metadata.create_all(engine)

#Pydantic models Item
class ItemBase(BaseModel):
    code:str
    name:str

class ItemCreate(ItemBase):
    id:int
    pass

class ItemResponse(BaseModel):
    id:int
    code:str
    name:str
    class Config:
        from_attributes = True


#Pydantic models Magazzino
class MagazzinoBase(BaseModel):
    code:str
    name:str
    quantity:int

class MagazzinoCreate(MagazzinoBase):
    id:int
    pass

class MagazzinoResponse(BaseModel):
    id:int
    code:str
    name:str
    quantity:int

    class Config:
        from_attributes = True