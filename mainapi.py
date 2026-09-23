from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Magazzino, Item, ItemCreate, MagazzinoCreate, ItemResponse, MagazzinoResponse

app = FastAPI()


@app.get('/')
def test():
    return {'message': 'hello world'}

@app.get('/items/', response_model=list[ItemResponse])
def all_items(db:Session = Depends(get_db)):
    return db.query(Item).all()
