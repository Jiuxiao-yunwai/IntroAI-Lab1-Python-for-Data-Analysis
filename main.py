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
gender_distribution = data['Sex'].value_counts().sort_index().reset_index()
gender_distribution.columns = ['Sex', 'Count']
output("Gender Distribution", gender_distribution)

gender_distribution.plot(x='Sex', y='Count', kind='bar', color='skyblue')
plt.title('Gender Distribution')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()
plt.close()


# 年龄分布
age_bins = range(0,90,5)
data['AgeGroup'] = pd.cut(data['Age'].dropna(), bins=age_bins)
age_group_counts = data['AgeGroup'].dropna().value_counts().sort_index()
output("Age Group Counts", age_group_counts)

plt.hist(data['Age'].dropna(), bins=age_bins, color='skyblue', edgecolor='white')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.xticks(age_bins)
plt.show()
plt.close()

# 船舱分布
cabin_distribution = data['Pclass'].value_counts().sort_index()
cabin_distribution.columns = ['CabinClass', 'Count']
output("Cabin Class Distribution", cabin_distribution)

cabin_distribution.plot(x='CabinClass', y='Count', kind='bar', color='skyblue')
plt.title('Cabin Class Distribution')
plt.xlabel('Cabin Class')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()
plt.close()

#分析概率

gender_survival_rate = data.groupby('Sex')['Survived'].mean().sort_index().reset_index()
gender_survival_rate.columns = ['Sex', 'SurvivalRate']
output("Gender Survival Rate", gender_survival_rate)

gender_survival_rate.plot(x='Sex', y='SurvivalRate', kind='bar', color='skyblue')
plt.title('Survival Rate by Gender')
plt.xlabel('Sex')
plt.ylabel('Survival Rate')
plt.xticks(rotation=0)
plt.show()
plt.close()

age_bins = range(0, 90, 10)
data['AgeGroup'] = pd.cut(data['Age'].dropna(), bins=age_bins)
age_group_survival_rate = data.groupby('AgeGroup', observed=True)['Survived'].mean().sort_index().reset_index()
age_group_survival_rate.columns = ['AgeGroup', 'SurvivalRate']
output("Age Group Survival Rate", age_group_survival_rate)

age_group_survival_rate.plot(x='AgeGroup', y='SurvivalRate', color='skyblue')
plt.title('Survival Rate by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate')
plt.xticks(ticks=range(len(age_group_survival_rate)), labels=age_group_survival_rate['AgeGroup'])
plt.xticks(rotation=45)
plt.show()
plt.close()

cabin_survival_rate = data.groupby('Pclass')['Survived'].mean().sort_index().reset_index()
cabin_survival_rate.columns = ['CabinClass', 'SurvivalRate']
output("Cabin Class Survival Rate", cabin_survival_rate)

cabin_survival_rate.plot(x='CabinClass', y='SurvivalRate', kind='bar', color='skyblue')
plt.title('Survival Rate by Cabin Class')
plt.xlabel('Cabin Class')
plt.ylabel('Survival Rate')
plt.xticks(ticks=range(len(cabin_survival_rate)), labels=cabin_survival_rate['CabinClass'])
plt.xticks(rotation=0)
plt.show()
plt.close()
