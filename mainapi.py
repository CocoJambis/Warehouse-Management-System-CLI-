from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models import Magazzino, Item, ItemCreate, MagazzinoCreate, ItemResponse, MagazzinoResponse

app = FastAPI()


@app.get('/')
def test():
    return {'message': 'hello world'}

#All Items in db
@app.get('/items/', response_model=list[ItemResponse])
def all_items(db:Session = Depends(get_db)):
    return db.query(Item).all()

#Aggiungi Item al database ufficiale
@app.post('/items/', response_model=ItemResponse)
def create_item(new_item:ItemCreate, db:Session = Depends(get_db)):
    if db.query(Item).filter(Item.code == new_item.code.upper()).one_or_none():
        raise HTTPException(status_code=404, detail='Item già nel database')
    else:
        new_item = Item(code = new_item.code.upper(), name = new_item.name.upper())
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    
#Rimuovi item dal database ufficiale
@app.delete('/items/{item_code}')
def remove_item(item_code=str, db:Session = Depends(get_db)):
    item = db.query(Item).filter(Item.code == item_code.upper()).one_or_none()

    if item:
        db.delete(item)
        db.commit()
        return {'message': 'Item Deleted'}
    else:
        raise HTTPException(status_code= 404, detail='Item non esistente nel database')
    
#Visualizza un item in base al codice
@app.get('/items/{item_code}', response_model=ItemResponse)
def single_item(item_code:str, db:Session = Depends(get_db)):
    item = db.query(Item).filter_by(code=item_code.upper()).one_or_none()

    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail='Item non esistente nel database')


