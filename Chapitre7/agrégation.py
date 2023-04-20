import pandas as pd

ventes = pd.read_csv('ventes.csv')

ventes_agregate = ventes.groupby('Produit')['Total'].sum()

print(ventes_agregate)
