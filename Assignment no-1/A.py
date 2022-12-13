import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
 
df=pd.DataFrame(columns=['name','age','percentage'])
df.loc[0]=['lina',19,93]
df.loc[1]=['shruti',18,89]
df.loc[2]=['sakshi',17,90]
df.loc[3]=['pallavi',18,87]
df.loc[4]=['arpita',19,92]
df.loc[5]=['sneha',18,89]
df.loc[6]=['siddhi',20,88]
df.loc[7]=['sejal',20,87]
df.loc[8]=['prachi',19,85]
df.loc[9]=['nikita',20,89]
print(df)

print("Shape of data:",df.shape)
print("No.of rows & columns:",df.size)
print("Data types:",df.dtypes)
print("Features names:",df.info())
print("Description of data:",df.describe())

df.loc[10]=['lina',19,93]
df.loc[11]=['shruti',18,89]
df.loc[12]=['yogita',17,None]
df.loc[13]=['sangeeta',None,87]
df.loc[14]=['ankita',19,92]
df['remark']=None
print(df)

print("Number of obeservation:",df.info())
print("Missing values:",df.isnull())
print("Dupalicate values:",df.duplicated())

df.drop(columns='remark',axis=1,inplace=True)
print(df)
#df.fillna()
#df.dropna()
print(df)

print(df.plot(x='name', y='percentage'))
plt.show()

#print(df.plot.scatter(x="name",y="percentage"))
#plt.show()
