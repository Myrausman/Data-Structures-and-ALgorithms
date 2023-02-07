import sys
sys.path.append('../')
from multidimensionalarray import MultiArray
a=2
b=2
c=3
multiArray = MultiArray(a,b,c)
for i in range(a):
    for j in range(b):
        for k in range(c):
            multiArray[i,j,k]=int(input('Enter value (%i,%i,%i)'%(i,j,k)))
