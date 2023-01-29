from Chapter2.myarray import Array
class Array2D:
    def __init__(self, numRows, numCols):
        self._theRows = Array(numRows)
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0])

    def clear(self, value):
        for row in range(self.numRows()):
            self._theRows[row].clear(value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple)==2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(),\
            "Array subscript out of range"
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple)==2, "Invalid no of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >=0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
            "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value
##-------------------------------------
## Implementation
##-------------------------------------
twoDArray = Array2D(3,3)
twoDArray.clear(0)
print('Initialize 2D array with \'0\' value')
for i in range(twoDArray.numRows()):
    print('')
    for j in range(twoDArray.numCols()):
        print(twoDArray[i,j],end =" ")


for i in range(twoDArray.numRows()):
    for j in range(twoDArray.numCols()):
        twoDArray[i,j] = int(input('enter value of array item (%d,%d) =  '%(i,j)))

print('Your 2D-Array is here:')
for i in range(twoDArray.numRows()):
    print()
    for j in range(twoDArray.numCols()):
        print(twoDArray[i,j],end =" ")