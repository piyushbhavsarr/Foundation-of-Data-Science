from numpy import *
from matplotlib.pyplot import *
from pandas import *

df=read_csv("Iris.csv")
data=df['PetalLengthCm']
data1=df['PetalWidthCm']
scatter(data,data1)
show()
