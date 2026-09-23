from sqlalchemy import  create_engine
from sqlalchemy.orm import  sessionmaker

engine = create_engine('sqlite:///database.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#session = Session()


#Connessione al Database
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()