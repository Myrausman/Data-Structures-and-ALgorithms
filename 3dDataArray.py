import sys
sys.path.append('../')
import ctypes
import random

class Array:
    def __init__(self,size):
        assert size>0 ,"Array size mustbe > 0"
        self._size=size
        PyArrayType=ctypes.py_object*size
        self._elements=PyArrayType()
        self.clear(None)
    def __len__(self):
        return self._size
    def __getitem__(self,index):
        assert index>=0 and index<len(self),"Array index out of range"
        return self._elements[index]
    def __setitem__(self,index,value):
        assert index>=0 and index<len(self),"Array index out of range"
        self._elements[index] =value
    def clear(self,value):
        for i in range(len(self)):
            self._elements[i]=value
    def __iter__(self):
        return _ArrayIterator(self._elements)
class _ArrayIterator:
    def __init__(self,Array):
        self._arrayRef=Array
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index < len(self._arrayRef):
            entry=self.arrayRef[self.index]
            self.index+=1
            return entry
        else:
            raise StopIteration  

class MultiArray:
    def __init__(self, *dimensions):
        assert len(dimensions) > 1, "Dimensions can not be less than 1"
        self._dims = dimensions
        size = 1
        for d in dimensions:
            assert d > 0, "Dimensions should be greater than 0"
            size *= d
        #create a 1-D array to store all elements
        self._elements = Array(size)
        #create 1-D array to store the equation factors
        self._factors = Array(len(dimensions))
        self._computeFactors()
    #no of dimensions in the array
    def numDims(self):
        return len(self._dims)

    #returns the lenth of the given dimension
    def length(self, dim):
        assert dim >= 1 and dim <= len(self._dims),\
               "Dimension component out of range"
        return self._dims[dim-1]

    #def clears the array by setting all elements to value
    def clear(self, value):
        self._elements.clear(value)

    #returns the cotnest of element(i_1, i_2,..., i_n)
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == self.numDims(), "Invalid array subscripts!"
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range"
        return self._elements[index]

    #sets the contents of element(i_1, i_2, i_3,...i_n)
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts"
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range"
        self._elements[index] = value

    #computes a 1-D array offset for element (i_1, i_2, ...i_n)
    #using the equation i_1 * f_1 + i_2 * f_2 +.... + i_n * f_n
    def _computeIndex(self, idx):
        offset = 0
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
        self._factors[len(self._factors)-1] = 1
        for j in reversed(range(len(self._factors) - 1)):
            self._factors[j] = self._factors[j+1] * self._dims[j+1]

def generateReport(fileName):
        multiarray = MultiArray(5,20,12)
        inputFO = open(fileName, "r")

        for line in inputFO:
            
            words = line.split()
            if len(words) == 2:
                item_counter = 0 
                f_index = int(words[1][1]) - 1#store index
            if len(words) == 13:
                if words[0] == "Item#":
                    pass
                else:
                    for i in range(12):
                        print(f_index,item_counter)
                        multiarray[f_index, item_counter, i] = float(words[i+1])
                    item_counter += 1
        inputFO.close()
        inputFO = None
        return multiarray

def totalSalesByStore( SalesData, store ):
# Subtract 1 from the store # since the array indices are 1 less
# than the given store #.
    s = store-1
    # Accumulate the total sales for the given store.
    total = 0.0
    # Iterate over item.
    for i in range( SalesData.length(2) ):
        # Iterate over each month of the i item.
        for m in range( SalesData.length(3) ):
            total += SalesData[s, i, m]
    return total
 
salesData=generateReport("SalesData.txt")
print ("totalsalesby store 1 : ",totalSalesByStore(salesData,1)) #print stores 1 total sell
print ("totalsalesby store 2 : ",totalSalesByStore(salesData,2))
print ("totalsalesby store 3 : ",totalSalesByStore(salesData,3))