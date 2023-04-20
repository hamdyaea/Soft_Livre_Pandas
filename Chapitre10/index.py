import pandas as pd

df = pd.read_csv('ventes2.csv')

# Création d'un index hiérarchique avec les colonnes "Mois" et "Produit"
df = df.set_index(['Mois', 'Produit'])

# Accès aux données de vente pour le mois de janvier pour le produit A
data = df.loc[('Janvier', 'A')] # puis print(data)
print(data)
