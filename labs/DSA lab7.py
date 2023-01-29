#!/usr/bin/env python
# coding: utf-8

# ### LAB 7
# #### Maira Usman (21B-011-se)

# In[51]:


import ctypes

class Array:
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        #create the array structure using the ctypes module
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        #initialize each element using clear method of Array class
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >=0 and index < len(self), "Array subscript out of range!"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert index >=0 and index < len(self), "Array subscript out of range!"
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration

class SparseMatrix:
    # Creates a sparse matrix of size numRows x numCols initialized to 0.
    def __init__(self, numRows, numCols):
        self._numCols = numCols
        self._listOfRows = Array(numRows)
    
    # Returns the number of rows in the matrix.
    def numRows(self):
        return len(self._listOfRows)
    
    # Returns the number of columns in the matrix.
    def numCols(self):
        return self._numCols
    
    # Returns the value of element (i,j): x[i,j]
    def __getitem__(self, ndxTuple):
        row = ndxTuple[0]
        col = ndxTuple[1]
        predNode = None
        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col:
            predNode = curNode
            curNode = curNode.next
        if curNode is not None and curNode.col == col:
            return curNode.value
    
    # Sets the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__(self, ndxTuple, value):
        row = ndxTuple[0]
        col = ndxTuple[1]
        predNode = None
        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col:
            predNode = curNode
            curNode = curNode.next
        # See if the element is in the list.
        if curNode is not None and curNode.col == col:
            if value == 0.0:  # remove the node.
                if curNode == self._listOfRows[row]:
                    self._listOfRows[row] = curNode.next
                else:
                    predNode.next = curNode.next
            else:  # change the node’s value.
                curNode.value = value
        # Otherwise, the element is not in the list.
        elif value != 0.0:
            newNode = _MatrixElementNode(col, value)
            newNode.next == curNode
            if curNode == self._listOfRows[row]:
                self._listOfRows[row] = newNode
            else:
                predNode.next = newNode
    
    # Scales the matrix by the given scalar.
    def scaleBy(self, scalar):
        for row in range(self.numRows()):
            curNode = self._listOfRows[row]
            while curNode is not None:
                curNode.value *= scalar
                curNode = curNode.next
    
    # Creates and returns a new matrix that is the transpose of this matrix.
    def transpose(self):
        ob1=SparseMatrix(self.numRows(),self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                ob1[i,j]=self[j,i]
        return ob1 
    
    def __add__ ( self , rhsMatrix ) :
        # Make sure the two matrices have the correct size .
        assert rhsMatrix.numRows () == self.numRows () and         rhsMatrix.numCols () == self.numCols () ,         " Matrix sizes not compatable for adding ."
        # Create a new sparse matrix of the same size .
        newMatrix = SparseMatrix ( self.numRows () , self.numCols () )
        # Add the elements of this matrix to the new matrix .
        for row in range ( self.numRows () ) :
            curNode = self._listOfRows [ row ]
            while curNode is not None :
                newMatrix [ row , curNode.col ] = curNode.value
                curNode = curNode . next
        # Add the elements of the rhsMatrix to the new matrix .
        for row in range ( rhsMatrix.numRows () ) :
            curNode = rhsMatrix._listOfRows [ row ]
            while curNode is not None :
                value = newMatrix [ row , curNode.col ]
                value += curNode.value
                newMatrix [ row , curNode . col ] = value
                curNode = curNode . next
        # Return the new matrix .
        return newMatrix
                # --- Matrix subtraction and multiplication ---
    def __sub__ ( self , rhsMatrix ) :
        # Make sure the two matrices have the correct size .
        assert rhsMatrix.numRows () == self.numRows () and         rhsMatrix.numCols () == self.numCols () ,         " Matrix sizes not compatable for subtracting ."
        # Create a new sparse matrix of the same size .
        newMatrix = SparseMatrix ( self.numRows () , self.numCols () )
        # Add the elements of this matrix to the new matrix .
        for row in range ( self.numRows () ) :
            curNode = self._listOfRows [ row ]
            while curNode is not None :
                newMatrix [ row , curNode.col ] = curNode.value
                curNode = curNode.next
        # Add the elements of the rhsMatrix to the new matrix .
        for row in range ( rhsMatrix.numRows () ) :
            curNode = rhsMatrix._listOfRows [ row ]
            while curNode is not None :
                value = newMatrix [ row , curNode.col ]
                value -= curNode.value
                newMatrix [ row , curNode.col ] = value
                curNode = curNode.next
        # Return the new matrix .
        return newMatrix
    def __mul__(self, rhsMatrix):
        # Make sure the two matrices have the correct size .
        assert rhsMatrix.numRows () == self.numRows () and         rhsMatrix.numCols () == self.numCols () ,         " Matrix sizes not compatable for subtracting ."
        # Create a new sparse matrix of the same size .
        newMatrix = SparseMatrix ( self.numRows () , self.numCols () )
        value=0
        for row in range ( self.numRows () ) :
            for col in range(rhsMatrix.numCols()):
                for k in range(self.numCols()):
                    value += self[row, k] * rhsMatrix[k, col]
                newMatrix[row,col] =value
        return newMatrix
    def __str__(self):
        print("matrix")
        # Create a list of strings, where each string represents a row of the matrix
        row_strings = []
        for row in range(self.numRows ()):
            row_string = ''
            curNode = self._listOfRows [ row ]
            j = 0
            while j <  self.numCols ():
                if curNode is not None and curNode.col == j:
                    # The element at (i, j) is non-zero, so add it to the string
                    row_string += str(curNode.value) + '  | '
                    curNode = curNode.next
                else:
                    # The element at (i, j) is zero, so add a zero to the string
                    row_string += '0'+"  |  "
                j += 1
            row_strings.append(row_string)

        # Join the list of row strings into a single string
        matrix_string = '\n'.join(row_strings)
        return matrix_string
# Storage class for creating matrix element nodes .
class _MatrixElementNode :
    def __init__ ( self , col , value ) :
        self . col = col
        self . value = value
        self . next = None
my=SparseMatrix(3,3)
my[0,0]=9
my[0,1]=1
my[0,2]=2
my[1,0]=3
my[1,1]=4
my[1,2]=5
my[2,0]=6
my[2,1]=7
my[2,2]=8
print(my)
you=SparseMatrix(3,3)
you[0,0]=1
you[0,1]=2
you[0,2]=3
you[1,0]=4
you[1,1]=5
you[1,2]=6
you[2,0]=6
you[2,1]=8
you[2,2]=7
print(you)
print("adding both matrix\n",my+you)
print("subtracting both matrix\n",my-you)
print("multiplication both matrix\n",my*you)
print("\n transpose \n",my.transpose())


# In[40]:


import ctypes
import random

class Array:
    def __init__(self,size):
        
        assert size > 0,"Size 0 cannot be accepted"
        
        self.size = size
        
        pyarray = ctypes.py_object * self.size
        self.element = pyarray()
        self.clear(None)
        
    def __len__(self):
        return self.size
    def clear(self,val):
        
        for i in range(len(self.element)):
            self.element[i] = val
            
            
    def __getitem__(self,index):
        assert index <= self.size and index >=0,"index out of range"
        
        return self.element[index]
    
    def __setitem__(self,index,val):
        assert index < self.size and index >=0,"index out of range"
        
        self.element[index] = val


class Polynomial:
    def __init__(self, degree = None, coefficient = None):
        if degree is None:
            self._polyHead = None
        else:
            self._polyHead = _PolyTermNode(degree, coefficient)
        self._polyTail = self._polyHead


    def degree(self):
        if self._polyHead is None:
            return -1
        else:
            return self._polyHead.degree
    def coffient(self):
        if self._polyHead is None:
            return 0
        else:
            return self._polyHead.coefficient
    def __getitem__(self, degree):
        assert self.degree() >= 0,             "Operation not permitted in empty polynomial."
        curNode = self._polyHead
        while curNode is not None and curNode.degree >= degree:
            curNode = curNode.next
        if curNode is None or curNode.degree != degree:
            return 0.0
        else:
            return curNode.degree

    def __add__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0,             "Addition only allowed in non-empty Polynomials"
        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = rhsPoly._polyHead

        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree
                value = nodeA.coefficient + nodeB.coefficient
                #adds when degree is same
                nodeA = nodeA.next
                nodeB = nodeB.next
            newPoly._appendTerm(degree, value)

        while nodeA is not None:
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next
            #if the list itself is longer
        while nodeB is not None:
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next
        return newPoly

    def __sub__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0,             "Addition only allowed in non-empty Polynomials"
        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = rhsPoly._polyHead

        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
            else:
                
                #print(nodeA.degree)
                degree = nodeA.degree
                value = nodeA.coefficient - nodeB.coefficient
                #adds when degree is same
                nodeA = nodeA.next
                nodeB = nodeB.next
            newPoly._appendTerm(degree, value)

        while nodeA is not None:
            
            print("hola ",degree)
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next
            #if the list itself is longer
        while nodeB is not None:
            print("hola ",degree)
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next
        return newPoly

    def __mul__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0,             "Multiplication only allowed in non-empty Polynomials"
        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = self._polyHead

        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree + nodeB.degree
                value = nodeA.coefficient * nodeB.coefficient
                #adds when degree is same
                nodeA = nodeA.next
                nodeB = nodeB.next
            newPoly._appendTerm(degree, value)
        

        while nodeA is not None:
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next
            #if the list itself is longer
        while nodeB is not None:
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next
        return newPoly


    #Helper method for appending terms in the polynomial
    def _appendTerm(self, degree, coefficient):
        if coefficient != 0.0:
            newTerm = _PolyTermNode(degree, coefficient)
            if self._polyHead is None:
                self._polyHead = newTerm
            else:
                self._polyTail.next = newTerm
            self._polyTail = newTerm
        
    def evaluate(self, x):
        assert self.degree() >= 0,             "Only non-empty polynomials can be evaluated!"
        result = 0.0
        curNode = self._polyHead
        p="    when x="+str(x)+"\n"
        while curNode is not None:
            result += curNode.coefficient * (x ** curNode.degree)
            if curNode.next is not None:
                p+=str(curNode.coefficient )+ '('+str(x)+')''^' + str(curNode.degree) + ' + '
            else:
                p+=str(curNode.coefficient )+'^' + str(curNode.degree) +' ='+str(result)
            curNode = curNode.next
        
        return p
    def __str__(self):
        curNode=self._polyHead
        p=""
        while curNode is not None:
            if curNode.next is not None:
                p+=str(curNode.coefficient) + 'x^' + str(curNode.degree) + ' + '
            else:
                p+=str(curNode.coefficient) + 'x^' + str(curNode.degree) +' = 0'
            curNode=curNode.next
        if p=="":
            return "0"
        return p
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None
        
    
eq1 = Polynomial(4,5)
eq1._appendTerm(3,2)
eq1._appendTerm(2,3)
eq2 = Polynomial(4,2)
eq2._appendTerm(3,2)
eq2._appendTerm(2,7)
print('_____________________________\n A= ',eq1)
print('_____________________________\n B= ',eq2)
print('_____________________________\n A+B= ',eq1+eq2)
new2 = eq1 - eq2
print('_____________________________\n A-B= ',new2)
new3 = eq1 * eq2
print('_____________________________\n A*B= ',new3)
print("_____________________________\n")
print("equation 1:",eq1.evaluate(10))
print("equation 1:",eq1.evaluate(9))
print("_____________________________\n")
print("equation 2:",eq2.evaluate(4))


# In[ ]:




