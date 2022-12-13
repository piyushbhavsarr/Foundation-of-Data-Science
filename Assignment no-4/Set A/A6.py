from pandas import *
from numpy import *
from matplotlib.pyplot import *
df=read_csv("Iris.csv")
data=df['Species']
hist(data,edgecolor="k")
show()
