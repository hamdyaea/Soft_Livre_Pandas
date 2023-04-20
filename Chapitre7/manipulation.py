import pandas as pd

ventes = pd.read_csv('ventes.csv')

ventes_triees = ventes.sort_values('Quantité', ascending=False)

print(ventes_triees)
