"""File containing the database connection logic"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLITE_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(SQLITE_DATABASE_URL, connect_args={
                       "check_same_thread": False
                       })

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """A function that gets us a database session

    Yields:
        db: A database session
    """
    _db = SessionLocal()
    try:
        yield _db
    finally:
        _db.close()
