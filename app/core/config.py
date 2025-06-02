import os
from pathlib import Path

# Diretório base onde está rodando o código
BASE_DIR = Path(__file__).resolve().parent

# Caminho seguro para o banco de dados
db_file = BASE_DIR / "test.db"

# String de conexão
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{db_file}")
print(DATABASE_URL)

