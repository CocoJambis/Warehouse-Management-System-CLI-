from sqlalchemy import  create_engine
from sqlalchemy.orm import  sessionmaker

engine = create_engine('postgresql://postgres:1312@localhost:5432/Magazzino')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Connessione al Database
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()