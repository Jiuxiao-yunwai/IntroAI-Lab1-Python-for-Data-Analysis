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

# 性别分布
gender_distribution = data['Sex'].value_counts().reset_index()
gender_distribution.columns = ['Sex', 'Count']
output("Gender Distribution", gender_distribution)

gender_distribution.plot(x='Sex', y='Count', kind='bar', color=['skyblue', 'lightgreen'])
plt.title('Gender Distribution')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()
plt.close()
