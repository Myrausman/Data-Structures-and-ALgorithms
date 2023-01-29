import sys
sys.path.append('../')
from multidimensionalarray import MultiArray

multiArray = MultiArray(2,2,2)
for i in range(2):
    for j in range(2):
        for k in range(2):
            multiArray[i,j,k]=int(input('Enter value (%i,%i,%i)'%(i,j,k)))
