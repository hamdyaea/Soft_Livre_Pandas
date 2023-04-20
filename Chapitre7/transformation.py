import pandas as pd

ventes = pd.read_csv('ventes.csv')

ventes['Total'] = ventes.apply(lambda row: row['Quantité'] * row['Prix'], axis=1)

print(ventes['Total'])
