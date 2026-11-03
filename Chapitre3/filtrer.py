# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from pathlib import Path
import pandas as pd

# Charger un fichier CSV dans un dataframe
df = pd.read_csv(Path(__file__).resolve().parent / 'ventes.csv')

# Filtrer les lignes du dataframe en fonction d'une condition
df_filtre = df['Prix'] > 10
print(df_filtre)
