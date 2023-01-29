#!/usr/bin/env python
# coding: utf-8

# In[20]:


def linearSearch( theValues , target ) :
    n = len( theValues ) 
    for i in range( n ) :
        # If the target is in the ith element , return True 
        if theValues[i] == target:
            return True 
    return False # If not found, return False.
values=([1,15,61,7,8])
print(linearSearch(values,53))


# In[19]:


def sortedLinearSearch( theValues , item ) : 
    n = len( theValues ) 
    for i in range( n ) : 
        if theValues[i] == item : 
            return True
        elif theValues[i] > item : 
            return False 
        return False 
values=([1,15,61,7,8])
print(sortedLinearSearch(values,53))        


# In[18]:


def binarySearch( theValues , target ) : 
    low = 0 
    high = len(theValues) - 1 
    while low <= high : 
        mid = (high + low) // 2 
        if theValues[mid] == target : 
            return True 
        elif target < theValues[mid] : 
            high = mid - 1 
            # Or does it follow the midpoint? 
        else : 
            low = mid + 1 
            # If the sequence cannot be subdivided further , we’re done. 
            return False 
values=([1,15,61,7,8])
print(binarySearch(values,53))  


# In[17]:


def bubbleSort( theSeq ):
    n = len( theSeq )
    for i in range( n - 1 ) :
        for j in range(  n - 1-i ) :
            if theSeq[j] > theSeq[j + 1] :
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
    return theSeq
values=([1,15,61,7,8])
c=bubbleSort(values)
print(c)


# In[16]:


# Sorts a sequence in ascending order using the insertion sort algorithm . 
def insertionSort( theSeq ): 
   n = len( theSeq ) 
   for i in range( 1, n ) : 
       value = theSeq[i] 
       pos = i 
       while pos > 0 and value < theSeq[pos - 1] : 
           theSeq[pos] = theSeq[pos - 1] 
           pos -= 1  
       theSeq[pos] = value 
   return theSeq
values=([1,15,61,7,8])
print(insertionSort(values))


# In[15]:


def selectionSort( theSeq ):
        n = len( theSeq )
        for i in range( n - 1 ):
            smallNdx = i
            for j in range( i + 1, n ):
                if theSeq[j] < theSeq[smallNdx] :
                    smallNdx = j
                if smallNdx != i :
                    tmp = theSeq[i]
                    theSeq[i] = theSeq[smallNdx]
                    theSeq[smallNdx] = tmp
            return(theSeq)        
values=([1,15,61,7,8])  
print(selectionSort(values))


# In[34]:


class Set:
    def __init__(self,*initElements):
        self._elements= list(initElements)
    def __len__(self):
        return len(self._elements)
    def __contains__(self,item):
        return item in self._elements
    def add( self, element ):
        if element not in self :
            ndx = self._findPosition( element )
            self._elements.insert( ndx, element )
    def remove( self, element ):
        assert element in self,"The element must be in the set."
        ndx = self._findPosition( element )
        self._elements.pop( ndx )
    def __eq__(self,setB):
        if len(self)!= len(setB):
            return False
        else:
            return self.isSubsetOf(setB)
    def isSubsetOf(self,setB):
        for item in self:
            if item not in setB:
                return False
        return True
    def union(self,setB):
        newSet=Set()
        newSet._elements.extend(self._elements)
        for item in setB:
            if item not in self:
                newSet._elements.append(item)
        return newSet
    def intersect(self,setB):
        newSet=Set()
        for item in self:
            if item in setB:
                newSet._elements.append(item)
        return newSet
    def difference(self,setB):
        newSet=Set()
        for item in self:
            if item not in setB:
                newSet._elements.append(item)
        return newSet
    def ProperSet(self,setB):
        if len(self._elements) !=len (setB):
            newSet=self.intersect(setB)
            if len (newSet ) == len(self):
                return True
        else:
            return False
    def _findPosition( self, target ): 
        low = 0
        high = len( self._elements )-1
        while low <= high :
            mid = (high + low) // 2
            if self._elements[ mid ] == target :
                return mid 
            elif target < self._elements[ mid ] :
                high = mid-1
            else:
                low = mid + 1
        return low      
    def __str__(self):
        x= str(self._elements)[1:-1]
        return f"{{{x}}}"
    def __iter__(self):
        return _SetIterator(self._elements)
class _SetIterator:
    def __init__(self,elements):
        self._elements=elements
        self._curNdx=0
    def __iter__(self):
        return self
    def __next__(self):
        if self._curNdx <len(self._elements):
            entry = self._elements[self._curNdx]
            self._curNdx+=1
            return entry
        else:
            raise StopIteration

            

A=Set(150,75,23,86,49)
A=Set(150,75,23,86,49)

A.add(4)
print(A)


# In[43]:


def binarySearch( theValues , target ) : 
    low = 0 
    high = len(theValues) - 1 
    while low <= high : 
        mid = (high + low) // 2 
        if theValues[mid] == target : 
             return mid
        elif target < theValues[mid] : 
            high = mid - 1 
        else : 
            low = mid + 1 
    return False     
values=([1,2,3,4,4,5,5,5,6,7,8])
print(binarySearch(values,4))  


# In[27]:


def findNegative( theValues ) : 
    temp=[]
    for i in theValues :
        if i < 0:
            temp.append(i)
    return temp
values=([1,-2,3,-4,4,-5,5,5,6,-7,8])
print(findNegative(values))  


# In[23]:


from matplotlib import pyplot as plt 
class Bag:
    def __init__(self):
        self._theItems = list()

    def __len__(self):
        return len(self._theItems)

    def __contains__(self, item):
        return item in self._theItems
    def add( self, element ):
        if element not in self :
            ndx = self._findPosition( element )
            self._theItems.insert( ndx, element )
    def remove( self, element ):
        assert element in self,"The element must be in the set."
        ndx = self._findPosition( element )
        self._theItems.pop( ndx )
    def _findPosition( self, target ): 
        low = 0
        high = len( self._theItems )-1
        while low <= high :
            mid = (high + low) // 2
            if self._theItems[ mid ] == target :
                return mid 
            elif target < self._theItems[ mid ] :
                high = mid-1
            else:
                low = mid + 1
        return low      
    def __str__(self):
        x= str(self._theItems)[1:-1]
        return f"[{x}]"
    def __iter__(self):
        return _BagIterator(self._theItems)

class _BagIterator:
    def __init__(self, theList):
        self._bagItems = theList
        self._curItem = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration
# def simulation(n): 
#     B =Bag()
#     steps_version1=[0]*n 
#     steps_version2 = [0] * n 
#     for i in range(0,n): 
#         steps_version1[i]=B.add(i) 
#         steps_version2[i]=B.remove(i) 
#     x=list(range(n)) 
#     plt.plot(x,steps_version2) 
#     plt.plot(x, steps_version1) 
#     plt.grid(which='both') 
#     plt.xlabel(f'Input Size({n})')
#     plt.ylabel('Number of Steps') 
#     plt.legend(['version2','version1']) 
#     plt.show() 
# simulation(50)
B =Bag()
B.add(49)
B.add(7)
B.add(20)
B.add(2)
B.add(8)
print(B)


# In[22]:


class Map:
    def __init__(self):
        self._list = list()

    def __len__(self):
        return len(self._list)

    def __contains__(self,element):
        return element in self._list

    def add(self,element):
        self._list.append(element)

    def remove(self,element):
        assert element in self._list,"Element Dosenot exist ."
        if element in self._list:
            self._list.remove(element)

    def __iter__(self):
        return iter(self._list)

    def binary_search(self,key):
        first = 0
        last = len( self._list ) - 1
        found = False
        while ( first <= last and not found ):
            midpoint = ( first + last ) // 2
            if self._list[ midpoint ][0] == key :
                found = True
            else:
                if key < self._list [ midpoint ][0] :
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        return found


    def __getitem__(self,key):
        for i in range(len(self._list)):
            if self._list[i][0] == key:
                return self._list[i][1]
        return None
    
    def __setitem__(self,key,value):
        for i in range(len(self._list)):
            if self._list[i][0] == key:
                self._list[i][1] = value
                return
        self._list.append([key,value])

obj3 = Map()
obj3.add([1,2])
obj3.add([3,4])
obj3.add([5,6])
obj3.add([7,8])
print(obj3.binary_search(3))


# In[ ]:




