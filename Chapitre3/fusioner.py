import pandas as pd

# Charger deux fichiers CSV dans des dataframes
df1 = pd.read_csv('ventes.csv')
df2 = pd.read_csv('ventes3.csv')

# Fusionner les deux dataframes en fonction d'une colonne commune
df_fusion = pd.merge(df1, df2, on='Total')
print(df_fusion)
