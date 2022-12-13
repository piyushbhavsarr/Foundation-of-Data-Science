import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nums=np.array([0.5,0.7,1,1.2,1.3,2.1])
bins=np.array([0,1,2,3])
print("nums:",nums)
print("bins:",bins)
print('\n')
plt.hist(nums,bins,edgecolor='orange',alpha=0.4)
plt.show()

"""OUTPUT-
ty64@pc23:~/Desktop/ty64/FDS/Assignment no-2/Set A$ python3 A5.py
nums: [0.5 0.7 1.  1.2 1.3 2.1]
bins: [0 1 2 3]

"""
