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
    
#Tutto il contenuto del Magazzino
@app.get('/magazzino/', response_model=list[MagazzinoResponse])
def all_magazzino(db:Session = Depends(get_db)):
    return db.query(Magazzino).all()

#Aggiunge item al al Magazzino se il codice prodotto è presente nel database ufficiale!
@app.post('/magazzino/', response_model=MagazzinoResponse)
def add_magazzino(new_item: MagazzinoCreate, db:Session = Depends(get_db)):

    item_db = db.query(Item).filter(Item.code == new_item.code.upper()).first()

    if db.query(Magazzino).filter(Magazzino.code == new_item.code.upper()).first():
        raise HTTPException(status_code=404, detail='Item già esistente nel magazzino')
    elif item_db:
        item = Magazzino(code = item_db.code, name = item_db.name, quantity = new_item.quantity)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
    else:
        raise HTTPException(status_code=404, detail='Item non presente nel database ufficiale')
   
    
        
