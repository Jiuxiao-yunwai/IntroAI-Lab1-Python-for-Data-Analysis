import pandas as pd 
path="titanic.csv"

data=pd.read_csv(path)

print(data.info())


