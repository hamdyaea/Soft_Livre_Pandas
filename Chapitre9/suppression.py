import pandas as pd

data = pd.read_csv('data.csv')
data = data.dropna() # supprimer les lignes contenant des valeurs manquantes
print(data)
