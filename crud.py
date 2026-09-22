from db import session, Magazzino, Item

#Aggiungi item al database
def add_item(codice:str, nome:str) -> None:
    new_item = Item(code=codice, name=nome)
    session.add(new_item)
    session.commit()
    print(f'{codice} aggiunto con successo al database!')

#Trova tutti gli oggetti in Item
def all_items() -> object:
    items = session.query(Item).all()
    return items

#Elimina item in database
def delete_item_database(codice:str) -> None:
    session.query(Item).filter_by(code=codice).delete()
    session.commit()
    print(f'{codice} eliminato con successo dal database')

#Il codice è nel database? True/False
def code_in_database(codice:int) -> bool:
    trovato = None

    for item in all_items():
        if item.code == codice:
            trovato = True
            return True
    if trovato != True:
        return False
    
#Il nome è dell'articolo è nel database? True/False
def name_in_database(nome:str) -> bool:
    item = session.query(Item).filter_by(name=nome).one_or_none()
    return True if item else False    


#Aggiunge articoli a Magazzino
def add_to_magazzino(codice:str, nome:str, quantità:int) -> None:
    item = Magazzino(code=codice, name=nome, quantity=quantità)
    session.add(item)
    session.commit()
    print(f'{item.code} aggiunto al magazzino, quantità : {quantità}')

#Trova il nome dell'articolo tramite il codice
def find_name_by_code(codice:str) -> str:
    item = session.query(Item).filter_by(code=codice).one_or_none()
    return item.name

#Articolo in magazzino? True/False
def item_in_magazzino(codice:str) -> bool:
    item= session.query(Magazzino).filter_by(code=codice).one_or_none()
    if item:
        return True
    else:
        return False
    
#Oggetto singolo in magazzino -> Oggetto
def single_item(codice:str) -> object:
    item = session.query(Magazzino).filter_by(code=codice).one_or_none()
    return item

def togli_quantità(codice:str, quantità:int) -> None:
    item = session.query(Magazzino).filter_by(code=codice).one_or_none()
    item.quantity -= quantità
    session.commit()
    print(f'Quantità di {item.code} -{quantità}')

def aggiungi_quantità(codice:str, quantità:int) -> None:
    item = session.query(Magazzino).filter_by(code=codice).one_or_none()
    item.quantity += quantità
    session.commit()
    print(f'Quantità di {item.code} +{quantità}')

#Lista di tutti gli item in Magazzino con giacenza 0
def giacenza_zero() -> list[()]:
    items = session.query(Magazzino).filter(Magazzino.quantity <= 0).all()
    return [item.name for item in items]

#Elimina tutti gli articoli in Magazzino con giacenza 0
def delete_zero() -> None:
    session.query(Magazzino).filter(Magazzino.quantity <= 0).delete()
    session.commit()
    print('Eliminati con successo!')

