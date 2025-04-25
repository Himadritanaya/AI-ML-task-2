import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic-Dataset.csv')

print(df.describe())
print(df.info())
print(df.isnull().sum())

df['Age'].hist(bins=30)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Age vs Survived')
plt.show()

sns.pairplot(df.dropna(), hue='Survived')

corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()



