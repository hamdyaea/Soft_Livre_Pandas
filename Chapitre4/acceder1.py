import pandas as pd

ma_liste = [1,2,3,4,5]
ma_serie = pd.Series(ma_liste)

nouvelle_serie = ma_serie[1:4]

print(nouvelle_serie)
