import pandas as pd

df=pd.read_csv("/data/ty64/Desktop/ty64/FDS/Assignment no-1/SOCR-HeightWeight.csv")
df.head(10)
df.tail(10)
df.sample(20)
print(df)
print("shape of dataframe object:",df.shape)
print("size of dataframe object:",df.size)
print("datatype of dataframe object:",df.dtypes)

print("statistical data:",df.describe())
print("Number of obeservation:",df.info())
print("Missing values:",df.isnull())

df["BMI"]=weight/(height)**2
