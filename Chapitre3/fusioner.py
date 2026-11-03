# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from pathlib import Path
import pandas as pd

# Charger deux fichiers CSV dans des dataframes
df1 = pd.read_csv(Path(__file__).resolve().parent / 'ventes.csv')
df2 = pd.read_csv(Path(__file__).resolve().parent / 'ventes3.csv')

# Fusionner les deux dataframes en fonction d'une colonne commune
df_fusion = pd.merge(df1, df2, on='Total')
print(df_fusion)
