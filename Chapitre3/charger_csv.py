import pandas as pd

# Charger un fichier CSV dans un dataframe
df = pd.read_csv('ventes.csv')

# Afficher les premières lignes du dataframe
print(df.head())
