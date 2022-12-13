from pandas import *
from numpy import *
from sklearn import preprocessing
import scipy.stats as s

df=read_csv("winequality-red.csv")
print(df)

print("Rescaling Data")
print("\n\n Data scaled between 0 and 1")
data_scaler=preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled=data_scaler.fit_transform(df)
print("..........................")
print(data_scaled.round(2))

print("\n Standardizing Data ")
arr=array(df)
print(arr)
print("\n Initial mean : ",s.tmean(arr).round(2))
print("\n Initial Standard Deviation : ",round(arr.std(),2))
x_scaled=preprocessing.scale(arr)
x_scaled.mean(axis=0)
x_scaled.std(axis=0)
print("\n Standardizing data : \n",x_scaled.round(2))
print("\n Scaled Mean : ",s.tmean(x_scaled).round(2))
print("\n Scaled Standard Deviation : ",round(x_scaled.std(),2))

"""OUTPUT-
ty64@pc23:~/Desktop/ty64/FDS/Assignment no-3/Set B$ python3 SetB.py
      fixed acidity  volatile acidity  citric acid  residual sugar  chlorides  ...  density    pH  sulphates  alcohol  quality
0               7.4             0.700         0.00             1.9      0.076  ...  0.99780  3.51       0.56      9.4        5
1               7.8             0.880         0.00             2.6      0.098  ...  0.99680  3.20       0.68      9.8        5
2               7.8             0.760         0.04             2.3      0.092  ...  0.99700  3.26       0.65      9.8        5
3              11.2             0.280         0.56             1.9      0.075  ...  0.99800  3.16       0.58      9.8        6
4               7.4             0.700         0.00             1.9      0.076  ...  0.99780  3.51       0.56      9.4        5
...             ...               ...          ...             ...        ...  ...      ...   ...        ...      ...      ...
1594            6.2             0.600         0.08             2.0      0.090  ...  0.99490  3.45       0.58     10.5        5
1595            5.9             0.550         0.10             2.2      0.062  ...  0.99512  3.52       0.76     11.2        6
1596            6.3             0.510         0.13             2.3      0.076  ...  0.99574  3.42       0.75     11.0        6
1597            5.9             0.645         0.12             2.0      0.075  ...  0.99547  3.57       0.71     10.2        5
1598            6.0             0.310         0.47             3.6      0.067  ...  0.99549  3.39       0.66     11.0        6

[1599 rows x 12 columns]
Rescaling Data


 Data scaled between 0 and 1
..........................
[[0.25 0.4  0.   ... 0.14 0.15 0.4 ]
 [0.28 0.52 0.   ... 0.21 0.22 0.4 ]
 [0.28 0.44 0.04 ... 0.19 0.22 0.4 ]
 ...
 [0.15 0.27 0.13 ... 0.25 0.4  0.6 ]
 [0.12 0.36 0.12 ... 0.23 0.28 0.4 ]
 [0.12 0.13 0.47 ... 0.2  0.4  0.6 ]]

 Standardizing Data 
[[ 7.4    0.7    0.    ...  0.56   9.4    5.   ]
 [ 7.8    0.88   0.    ...  0.68   9.8    5.   ]
 [ 7.8    0.76   0.04  ...  0.65   9.8    5.   ]
 ...
 [ 6.3    0.51   0.13  ...  0.75  11.     6.   ]
 [ 5.9    0.645  0.12  ...  0.71  10.2    5.   ]
 [ 6.     0.31   0.47  ...  0.66  11.     6.   ]]

 Initial mean :  7.93

 Initial Standard Deviation :  16.03

 Standardizing data : 
 [[-0.53  0.96 -1.39 ... -0.58 -0.96 -0.79]
 [-0.3   1.97 -1.39 ...  0.13 -0.58 -0.79]
 [-0.3   1.3  -1.19 ... -0.05 -0.58 -0.79]
 ...
 [-1.16 -0.1  -0.72 ...  0.54  0.54  0.45]
 [-1.39  0.65 -0.78 ...  0.31 -0.21 -0.79]
 [-1.33 -1.22  1.02 ...  0.01  0.54  0.45]]

 Scaled Mean :  -0.0

 Scaled Standard Deviation :  1.0
"""
