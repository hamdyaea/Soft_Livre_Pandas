# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from pathlib import Path
import pandas as pd

# Charger un fichier CSV dans un dataframe
df = pd.read_csv(Path(__file__).resolve().parent / 'ventes.csv')

# Créer une série à partir de la colonne 'nom_colonne'
serie = df['Total']

# Afficher la série
print(serie)
