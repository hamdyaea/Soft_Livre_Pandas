import pandas as pd

# Charger un fichier CSV dans un dataframe
df = pd.read_csv('ventes.csv')

# Ajouter une colonne au dataframe
df['nouvelle_colonne'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(df)
