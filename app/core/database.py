from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.core.config import settings


# Conexão com PostgreSQL
engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)


# Gerenciamento das sessões
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Classe base dos nossos modelos
class Base(DeclarativeBase):
    pass


# Dependência para disponibilizar sessões
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()