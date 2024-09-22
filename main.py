import pandas as pd 
import matplotlib.pyplot as plt
path="titanic.csv"
endl="-----------------------------------------------------------------------------------"
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


# 年龄分布
age_bins = range(0,90,5)
data['AgeGroup'] = pd.cut(data['Age'], bins=age_bins)
age_group_counts = data['AgeGroup'].dropna().value_counts().sort_index()
output("Age Group Counts", age_group_counts)

plt.hist(data['Age'].dropna(), bins=age_bins, color='skyblue', edgecolor='white')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.xticks(age_bins)
plt.show()
plt.close()