import pandas as pd

df = pd.read_csv('ventes.csv')

# Calcul de la moyenne de la colonne "Prix unitaire"
mean = df['Prix'].mean()
print(mean)

# Calcul de la somme de la colonne "Quantité vendue"
sum = df['Quantité'].sum()
print(sum)

# Recherche de la valeur minimale de la colonne "Prix unitaire"
min = df['Prix'].min()
print(min)

# Recherche de la valeur maximale de la colonne "Prix unitaire"
max = df['Prix'].max()
print(max)

# Calcul de l'écart type de la colonne "Prix unitaire"
std = df['Prix'].std()
print(std)

# Calcul de la variance de la colonne "Prix unitaire"
var = df['Prix'].var()
print(var)
