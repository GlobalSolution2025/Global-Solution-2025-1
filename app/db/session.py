from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseSettings
import os

# Carregar configurações do arquivo .env
class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./test.db"  # Defina o caminho para o banco de dados SQLite

    class Config:
        env_file = ".env"

settings = Settings()
print(f"Using database URI: {settings.SQLALCHEMY_DATABASE_URI}")

# Criando o engine para SQLite
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False}  # Necessário para SQLite em multithreading
)

# Criando a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
