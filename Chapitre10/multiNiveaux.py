import pandas as pd

# Charger le fichier csv
data = pd.read_csv('ventes3.csv')

# Convertir la colonne 'Date' en format de date
data['Date'] = pd.to_datetime(data['Date'])

# Extraire toutes les ventes pour les villes Paris et les pays France
paris_france = data.loc[(data['Ville'] == 'Paris') & (data['Pays'] == 'France')]

# Extraire toutes les ventes pour les mois de janvier et février
jan_feb_sales = paris_france.loc[(paris_france['Date'] >= '2022-01-01') & (paris_france['Date'] <= '2022-02-28')]

# Afficher les résultats
print(jan_feb_sales)
