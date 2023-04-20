import pandas as pd

df = pd.read_csv('ventes1.csv')

# Remplacement de toutes les occurrences de "France" par "FR" dans la colonne "Pays"
df['Pays'] = df['Pays'].str.replace('France', 'FR')
print(df['Pays'])
