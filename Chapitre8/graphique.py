# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ventes = pd.read_csv(Path(__file__).resolve().parent / 'ventes.csv')

ventes.groupby('Produit')['Quantité'].sum().plot(kind='bar', color='green')

plt.title('Quantité totale vendue pour chaque produit')
plt.xlabel('Produit')
plt.ylabel('Quantité vendue')
plt.show()
