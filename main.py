import pandas as pd 
import matplotlib.pyplot as plt
path="titanic.csv"
endl="\n-----------------------------------------------------------------------------------\n"
data=pd.read_csv(path)

def output(title,df):
    print('------',title,'------')
    print(df)
    print(endl)


data.info()
output("Head",data.head())
output("describe",data.describe())
output("isNull",data.isnull().sum())