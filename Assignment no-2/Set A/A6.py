import numpy as np
import scipy.stats as s
import pandas as pd

d={'Name':['Lina','Sakshi','Shruti','Swanand','Pallavi'],'Percentage':[80,79,90,89,92],'Age':[19,20,20,19,20]}
df=pd.DataFrame(d)
print(df)
print("Average age of student : ",s.tmean(df['Age']).round(2))
print("Average age of student : ",s.tmean(df['Percentage']).round(2))
print(df.describe())

"""OUTPUT-
ty64@pc23:~/Desktop/ty64/FDS/Assignment no-2/Set A$ python3 A6.py
      Name  Percentage  Age
0     Lina          80   19
1   Sakshi          79   20
2   Shruti          90   20
3  Swanand          89   19
4  Pallavi          92   20
Average age of student :  19.6
Average age of student :  86.0
       Percentage        Age
count    5.000000   5.000000
mean    86.000000  19.600000
std      6.041523   0.547723
min     79.000000  19.000000
25%     80.000000  19.000000
50%     89.000000  20.000000
75%     90.000000  20.000000
max     92.000000  20.000000
"""
