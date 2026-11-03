# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from pathlib import Path
import pandas as pd

mon_dataframe = pd.read_csv(Path(__file__).resolve().parent / 'ventes.csv')

print(mon_dataframe)
