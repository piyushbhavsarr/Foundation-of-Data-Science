"""import pandas as pd
import numpy as np
df=pd.read_csv("/data/ty64/Desktop/ty64/FDS/Assignment no-2/Set B/Iris.csv")
print("Random Samples : ",df.sample(10)) 
print("Maximum value of numeric attribute : ")
print(df.max(axis=None))
print("Minimum value of numeric attribute :)
print(np.min(df))
================================================"""

from pandas import *
import numpy as np
import scipy.stats as s
df=read_csv("Iris.csv")
print(df.sample(10))
print(df)
print(df.dtypes)

print("min and max value spealLengthCm")
print(max(df["SepalLengthCm"]))
print(min(df["SepalLengthCm"]))

print("min and max value petalLength")
print(max(df["PetalLengthCm"]))
print(min(df["PetalLengthCm"]))
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(df.info())
print("-----------------------------------------------------------------------------------------------------------------------------------------")
print("Mean:-")
print("SepalLengthCm Mean : ",s.tmean(df["SepalLengthCm"]).round(2))
print("SepalWidthCm Mean : ",s.tmean(df["SepalWidthCm"]).round(2))
print("PetalLengthCm Mean : ",s.tmean(df["PetalLengthCm"]).round(2))
print("PetalWidthCm Mean : ",s.tmean(df["PetalWidthCm"]).round(2))

print("Median:-")
print("SepalLengthCm Median : ",np.median(df["SepalLengthCm"]).round(2))
print("SepalWidthCm Median : ",np.median(df["SepalWidthCm"]).round(2))
print("PetalLengthCm Median: ",np.median(df["PetalLengthCm"]).round(2))
print("PetalWidthCm Median: ",np.median(df["PetalWidthCm"]).round(2))


"""OUTPUT-
ty64@pc23:~/Desktop/ty64/FDS/Assignment no-2/Set B$ python3 B1.py
      Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm          Species
11    12            4.8           3.4            1.6           0.2      Iris-setosa
20    21            5.4           3.4            1.7           0.2      Iris-setosa
76    77            6.8           2.8            4.8           1.4  Iris-versicolor
86    87            6.7           3.1            4.7           1.5  Iris-versicolor
50    51            7.0           3.2            4.7           1.4  Iris-versicolor
129  130            7.2           3.0            5.8           1.6   Iris-virginica
120  121            6.9           3.2            5.7           2.3   Iris-virginica
2      3            4.7           3.2            1.3           0.2      Iris-setosa
12    13            4.8           3.0            1.4           0.1      Iris-setosa
147  148            6.5           3.0            5.2           2.0   Iris-virginica
      Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm         Species
0      1            5.1           3.5            1.4           0.2     Iris-setosa
1      2            4.9           3.0            1.4           0.2     Iris-setosa
2      3            4.7           3.2            1.3           0.2     Iris-setosa
3      4            4.6           3.1            1.5           0.2     Iris-setosa
4      5            5.0           3.6            1.4           0.2     Iris-setosa
..   ...            ...           ...            ...           ...             ...
145  146            6.7           3.0            5.2           2.3  Iris-virginica
146  147            6.3           2.5            5.0           1.9  Iris-virginica
147  148            6.5           3.0            5.2           2.0  Iris-virginica
148  149            6.2           3.4            5.4           2.3  Iris-virginica
149  150            5.9           3.0            5.1           1.8  Iris-virginica

[150 rows x 6 columns]
Id                 int64
SepalLengthCm    float64
SepalWidthCm     float64
PetalLengthCm    float64
PetalWidthCm     float64
Species           object
dtype: object
min and max value spealLengthCm
7.9
4.3
min and max value petalLength
6.9
1.0
----------------------------------------------------------------------------------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Id             150 non-null    int64  
 1   SepalLengthCm  150 non-null    float64
 2   SepalWidthCm   150 non-null    float64
 3   PetalLengthCm  150 non-null    float64
 4   PetalWidthCm   150 non-null    float64
 5   Species        150 non-null    object 
dtypes: float64(4), int64(1), object(1)
memory usage: 7.2+ KB
None
-----------------------------------------------------------------------------------------------------------------------------------------
Mean:-
SepalLengthCm Mean :  5.84
SepalWidthCm Mean :  3.05
PetalLengthCm Mean :  3.76
PetalWidthCm Mean :  1.2

Median:-
SepalLengthCm Median :  5.8
SepalWidthCm Median :  3.0
PetalLengthCm Median:  4.35
PetalWidthCm Median:  1.3
"""
