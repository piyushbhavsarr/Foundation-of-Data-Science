from numpy import *
from matplotlib.pyplot import *
from pandas import *

df=read_csv("Iris.csv")
data=df['PetalLengthCm']
data1=df['PetalWidthCm']
data2=df['SepalLengthCm']
data3=df['SepalWidthCm']
boxplot(data,vert=False)
boxplot(data1,vert=False)
boxplot(data2,vert=False)
boxplot(data3,vert=False)
show()
