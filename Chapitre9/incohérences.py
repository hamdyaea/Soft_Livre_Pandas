import pandas as pd

data = pd.read_csv('data.csv')
#print(data['column_name'].describe())
print(data['Age'].describe())
