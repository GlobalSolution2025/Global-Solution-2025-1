import pandas as pd
import sqlite3
import os

# Caminho CORRIGIDO para o arquivo CSV — use / ou r"..." para evitar erro de unicode
csv_path = r"C:\Users\vitor\Documents\GitHub\Global-Solution-2025-1\dados\focos_ams_ref_2024.csv"
db_path = "focos_incendio.db"

# Verifica se o arquivo CSV existe antes de tentar importar
if not os.path.exists(csv_path):
    print(f"❌ Arquivo CSV não encontrado: {csv_path}")
    exit()

print("🔄 Lendo CSV...")
df = pd.read_csv(csv_path)
print(f"✅ {len(df)} linhas carregadas.")

# Conecta ao banco e importa os dados
conn = sqlite3.connect(db_path)
print("📥 Importando dados para o banco SQLite...")

df.to_sql("focos_incendio", conn, if_exists="replace", index=False)

conn.close()
print("✅ Banco de dados criado com sucesso: focos_incendio.db")
