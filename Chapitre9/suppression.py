# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from pathlib import Path
import pandas as pd

data = pd.read_csv(Path(__file__).resolve().parent / 'data.csv')
data = data.dropna() # supprimer les lignes contenant des valeurs manquantes
print(data)
