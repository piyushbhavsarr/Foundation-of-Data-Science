from pandas import *
from numpy import *
from matplotlib.pyplot import *
df=read_csv("Iris.csv")
data=df['Species']
data1=df['Id']
pie(data1,labels=data)
show()
