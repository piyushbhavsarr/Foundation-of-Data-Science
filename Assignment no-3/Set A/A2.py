from pandas import *

df=read_csv("data.csv")
print("Missing values:")
print(df.isnull())
print("...................................................")
df=df.fillna(0)
print(df)
print("...................................................")
mean_age=df['Age'].mean()
print("Mean of Age: ",mean_age)
print("...................................................")
mean_salary=df['Salary'].mean()
print("Mean of Salary: ",mean_salary)
print("...................................................")
df['Age'].fillna(mean_age,inplace=True)
df['Salary'].fillna(mean_salary,inplace=True)
print(df)

