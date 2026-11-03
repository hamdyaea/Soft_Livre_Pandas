# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from pathlib import Path
import pandas as pd

ventes = pd.read_csv(Path(__file__).resolve().parent / 'ventes.csv')

tableau_croise = pd.pivot_table(ventes, values='Prix', index='Produit', columns='Date', aggfunc='sum')

print(tableau_croise)
