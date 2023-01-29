import sys
sys.path.append('../')
import ctypes
import random

class Array:
    def __init__(self, size):
        self._size = size
        PyArraytype = ctypes.py_object * size
        self._elements = PyArraytype()
        self.clear(0)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        return self._elements[index]
        

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self),("Array Subscript out of range")
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value
            
    def display(self):
        for i in range(self._size):
            print(self._elements[i])

    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    def __init__(self, myArr):
        self.arrRed = myArr
        self.currNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self.curNdx += 1
            return entry
        else:
            raise StopIteration

class MultiArray:
    def __init__(self, *dimensions):
        self._dims = dimensions
        size = 1
        for d in dimensions:
            size *= d
        #create a 1-D array to store all elements
        
        # self._elements = Array(24)
        self._elements = Array(size)
        #create 1-D array to store the equation factors
        self._factors = Array(len(dimensions))
        self._computeFactors()
    def numDims(self):
        return len(self._dims)
    #returns the lenth of the given dimension
    def length(self, dim):
        return self._dims[dim-1]
    #def clears the array by setting all elements to value
    def clear(self, value):
        self._elements.clear(value)
        #returns the cotnest of element(i_1, i_2,..., i_n)
    def __getitem__(self, ndxTuple):
        index = self._computeIndex(ndxTuple)
        return self._elements[index]
    def __setitem__(self, ndxTuple, value):
        index = self._computeIndex(ndxTuple)
        print(index)
        self._elements[index] = value
        #computes a 1-D array offset for element (i_1, i_2, ...i_n)
        #using the equation i_1 * f_1 + i_2 * f_2 +.... + i_n * f_n
    def _computeIndex(self, idx):
        offset = 0
        # [0,1,0]
        for j in range(len(idx)):
            #make sure the index componens within the legal range
            if idx[j] < 0 or idx[j] >= self._dims[j]:
                return None
            else:
                offset += idx[j] * self._factors[j]
        return offset
        #computes the factor values used in the index equation
        #done as part of exercise
    def _computeFactors(self):
        max_idx = len(self._factors) - 1
        self._factors[max_idx] = 1
        for i in range(max_idx, 0, -1):
            self._factors[i - 1] = self._dims[i] * self._factors[i]
        # self._factors.display()
        
            
multiArray = MultiArray(2,2,2)
for i in range(2):
    for j in range(2):
        for k in range(2):
            multiArray[i,j,k]=int(input("Enter value (%i,%i,%i)"%(i,j,k)))
            
print(multiArray.__getitem__([0,1,0]))
print(multiArray.__getitem__([1,1,1]))
print(multiArray.__getitem__([0,0,0]))