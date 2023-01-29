#implementation of the Matrix ADT using 2-D array

from my2darray import Array2D

class Matrix:
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)

    def numRows(self):
        return self._theGrid.numRows()

    def numCols(self):
        return self._theGrid.numCols()

    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0], ndxTuple[1]]

    def __setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0],ndxTuple[1]]=scalar

    def scaleBy(self, scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r,c] *= scalar

    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
            "Matrix size not compatible for adding"
        newMatrix = Matrix(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r,c] + rhsMatrix[r,c]
        return newMatrix

    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
            "Matrix size not compatible for adding"
        newMatrix = Matrix(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r,c] - rhsMatrix[r,c]
        return newMatrix

    def __mul__(self,rhsMatrix):
        assert self.numCols() == rhsMatrix.numRows(), \
            "Matrix size not compatible for adding"
        newMatrix = Matrix(self.numRows(), rhsMatrix.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                for k in range(rhsMatrix.numCols()):
                    newMatrix[r, k] += self[r,c] * rhsMatrix[c,k]
        return newMatrix

    def transpose(self):
        newMatrix = Matrix(self.numCols(), self.numRows())
        for c in range(self.numCols()):
            for r in range(self.numRows()):
                newMatrix[c,r]=self[r,c]
        return newMatrix


# if '__name__==__main__':
#
#     print('enter Matrix A')
#     A=Matrix(2,2)
#     for r in range(A.numRows()):
#         for c in range(A.numCols()):
#             A[r,c]=int(input('Enter value %d , %d: '%(r,c)))
    #
    # print('enter Matrix B')
    # B=Matrix(2,2)
    # for r in range(B.numRows()):
    #     for c in range(B.numCols()):
    #         B[r,c]=int(input('Enter value %d , %d: '%(r,c)))
    # ## Multiplication of Matrix
    # C=A*B
    # print('\nMatrix A')
    # for i in range(A.numRows()):
    #     print()
    #     for j in range(A.numCols()):
    #         print(A[i,j],end =" ")
    # print('\nMatrix B')
    # for i in range(B.numRows()):
    #     print()
    #     for j in range(B.numCols()):
    #         print(B[i, j], end=" ")
    # print('\nMatrix A x B')
    # for i in range(C.numRows()):
    #     print()
    #     for j in range(C.numCols()):
    #         print(C[i,j],end =" ")

    # Tranpose of Matrix
    # T=A.transpose()
    # for r in range(T.numRows()):
    #     print()
    #     for c in range(T.numCols()):
    #         tu = (r,c)
    #         print(T[r,c],end=' ')
