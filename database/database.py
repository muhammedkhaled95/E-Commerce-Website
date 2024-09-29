from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings

# PostgreSQL database URL
POSTGRESQL_DATABASE_URL = (
    f'postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}'
    f'@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}'
)

# Create the SQLAlchemy engine
engine = create_engine(POSTGRESQL_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()


def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()