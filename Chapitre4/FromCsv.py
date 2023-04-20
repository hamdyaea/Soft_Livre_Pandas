import pandas as pd

# Charger un fichier CSV dans un dataframe
df = pd.read_csv('ventes.csv')

# Créer une série à partir de la colonne 'nom_colonne'
serie = df['Total']

# Afficher la série
print(serie)
