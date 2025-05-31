import sqlite3
import pandas as pd

conn = sqlite3.connect("focos_incendio.db")
df = pd.read_sql_query("SELECT * FROM focos_incendio LIMIT 5", conn)
print(df)
conn.close()
