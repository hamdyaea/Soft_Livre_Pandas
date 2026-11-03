# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from pathlib import Path
import pandas as pd

data = pd.read_csv(Path(__file__).resolve().parent / 'data.csv')
#print(data['column_name'].describe())
print(data['Age'].describe())
