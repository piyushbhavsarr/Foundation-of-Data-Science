def distancesum(x,y,n):
       sum=0
       for i in range(n):
              for j in range(i+1,n):
                   sum+=(abs(x[i]-x[j])+abs(y[i]-y[j]))
                  
       return sum
x=[-1,1,3,2]
y=[5,6,5,3]
n=len(x)
print("sum of Manhattan Distance:",distancesum(x,y,n))


"""
OUTPUT-
ty64@pc23:~/Desktop/ty64/FDS/Assignment no-2/Set A$ python3 A4.py
sum of Manhattan Distance: 22
"""

