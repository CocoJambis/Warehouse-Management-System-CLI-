from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from pydantic import BaseModel

engine = create_engine('sqlite:///database.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

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
    pass

class Item(ItemBase):
    id:int

    class Config:
        orm_mode = True


#Pydantic models Magazzino
class MagazzinoBase(BaseModel):
    code:str
    name:str
    quantity:int

class MagazzinoCreate(MagazzinoBase):
    pass

class Magazzino(MagazzinoBase):
    id:int

    class Config:
        orm_mode = True