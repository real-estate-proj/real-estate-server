from .engine import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker (
    bind=engine,
    autocommit=False,
    autoflush=False
)

def init_database ():
    database = Session ()
    try:
        yield database
    finally:
        database.close ()
