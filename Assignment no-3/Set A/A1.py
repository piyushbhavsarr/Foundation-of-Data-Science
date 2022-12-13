from pandas import *
df=read_csv("data.csv")
print("Description of data:")
print(df.describe())
print("..........................................")
print("Shape of data:",df.shape)
print(".............................................")
print("first three rows are :")
print(df.iloc[:3])

'''OUTPUT-
ty64@pc34:~/Desktop/ty64/FDS/Assignment no-3$ python3 A1.py
Description of data:
             Age        Salary
count   9.000000      9.000000
mean   38.777778  63777.777778
std     7.693793  12265.579662
min    27.000000  48000.000000
25%    35.000000  54000.000000
50%    38.000000  61000.000000
75%    44.000000  72000.000000
max    50.000000  83000.000000
..........................................
Shape of data: (10, 4)
.............................................
first three rows are :
   Country   Age   Salary Purchased
0   France  44.0  72000.0        No
1    Spain  27.0  48000.0       Yes
2  Germany  30.0  54000.0        No
'''


