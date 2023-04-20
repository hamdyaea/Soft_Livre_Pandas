import pandas as pd

data = pd.read_csv('data.csv')
#data['column_name'] = data['column_name'].replace(incorrect_value, correct_value)
data['Age'] = data['Age'].replace(35,30)
print(data)
