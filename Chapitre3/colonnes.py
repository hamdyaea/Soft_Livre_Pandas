# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from pathlib import Path
import pandas as pd

# Charger un fichier CSV dans un dataframe
df = pd.read_csv(Path(__file__).resolve().parent / 'ventes.csv')

# Accéder à une colonne en utilisant son nom
colonne1 = df['Date']
print(colonne1)

# Accéder à plusieurs colonnes en utilisant une liste de noms de colonnes
colonnes = ['Produit', 'Total']
df2 = df[colonnes]
print(df2)
