import pandas as pd

# Charger un fichier CSV dans un dataframe
df = pd.read_csv('ventes.csv')

# Filtrer les lignes du dataframe en fonction d'une condition
df_filtre = df['Prix'] > 10
print(df_filtre)
