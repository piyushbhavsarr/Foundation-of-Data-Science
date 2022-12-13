import pandas as pd
from scipy.stats import iqr
import numpy as np
d={'score':[80,85,90,75],'Name':['Raju','Ravi','Rucha','Rekha']}
df=pd.DataFrame(d)
print(df)
r=max(df['score'])-min(df['score'])
print("\n value of range in distribution : ",r)
col=df['score']
mean_of_score=col.mean()
print("Average of score : ",mean_of_score)
q3,q1=np.percentile(col,[75,25])
iqrvalue=q3-q1
print("Interquartile range : ",iqrvalue)

"""OUTPUT-
ty64@pc23:~/Desktop/ty64/FDS/Assignment no-2/Set A$ python3 A3.py
   score   Name
0     80   Raju
1     85   Ravi
2     90  Rucha
3     75  Rekha

 value of range in distribution :  15
Average of score :  82.5
Interquartile range :  7.5
"""
