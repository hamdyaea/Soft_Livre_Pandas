# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from pathlib import Path
import pandas as pd

ventes = pd.read_csv(Path(__file__).resolve().parent / 'ventes.csv')

ventes['Total'] = ventes.apply(lambda row: row['Quantité'] * row['Prix'], axis=1)

print(ventes['Total'])
