import pandas as pd

ventes = pd.read_csv('ventes.csv')

tableau_croise = pd.pivot_table(ventes, values='Prix', index='Produit', columns='Date', aggfunc='sum')

print(tableau_croise)
