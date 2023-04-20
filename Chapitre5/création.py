import pandas as pd

# Créer un DataFrame à partir d'un dictionnaire
mon_dict = {'nom': ['Jean', 'Marie', 'Pierre', 'Lucie'],
            'âge': [24, 30, 42, 18],
            'ville': ['Paris', 'Lyon', 'Marseille', 'Toulouse']}
mon_dataframe = pd.DataFrame(mon_dict)

# Afficher le DataFrame
print(mon_dataframe)
