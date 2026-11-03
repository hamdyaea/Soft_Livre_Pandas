# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from pathlib import Path
import pandas as pd

# Charger un fichier CSV dans un dataframe
df = pd.read_csv(Path(__file__).resolve().parent / 'ventes.csv')

# Ajouter une colonne au dataframe
df['nouvelle_colonne'] = range(1, len(df) + 1)
print(df)
