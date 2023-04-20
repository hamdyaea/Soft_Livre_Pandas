import pandas as pd

ventes = pd.read_csv('ventes.csv')

ventes_filtrees = ventes[ventes['Quantité'] > 4]

print(ventes_filtrees)
