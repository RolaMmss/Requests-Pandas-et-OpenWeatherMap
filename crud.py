import pandas as pd

import sqlite3

# Charger le fichier CSV dans un dataframe pandas
df = pd.read_csv("informations_meteo.csv")

# Créer une connexion à la base de données SQLite
conn = sqlite3.connect("meteo.db")

# Écrire le dataframe dans une table SQLite
df.to_sql("Meteo_villes", conn, if_exists="replace", index=False)

# Fermer la connexion
conn.close()
