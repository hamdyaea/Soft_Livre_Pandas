# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from pathlib import Path
import pandas as pd

ventes = pd.read_csv(Path(__file__).resolve().parent / 'ventes.csv')

ventes_filtrees = ventes[ventes['Quantité'] > 4]

print(ventes_filtrees)
