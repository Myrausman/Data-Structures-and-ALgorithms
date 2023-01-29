#!/usr/bin/env python
# coding: utf-8

# #### Lab1                                                    
# #### Data Structures and Algorithms
# #### Maira usman           
# #### 21B-011-SE                                                                      

# In[3]:


# // your code goes here
def is_multiply(m,n):
    if n%m==0:
        return True
    else:
        return False
a=is_multiply(3,10)
b=is_multiply(3,12)
print(a)
print(b)


# In[2]:


def is_even(k):
    a= [i for i in range(0,k+2,2)]
    if k in a:
        return True
    else :
        return False
x=is_even(9)
y=is_even(8)
print(x)
print(y)


# In[4]:


def EvenList(n):
    a=[]
    n=n.split(",")
    for i in range (1,len(n)+1):
        if i%2 ==0:
            a.append(i)
    return a
n=input("enter numbers seperated by comma")
x=EvenList(n)
print(x)


# In[5]:


def minmax(data):
    a=data[0]
    b=data[0]
    for i in range(len(data)):
        if a >data[i]:
            a=data[i]
        if b<data[i]:
            b=data[i]
    return (a,b)
x=minmax([6,2,1,4,5,5])
print(x)      
            


# In[6]:


def sumsquares(n):
    a=0
    for i in range(n+1):
        a+=i**2
    return a
x=sumsquares(6)
print(x)


# In[7]:


def sumoddsquares(k):
    a=0
    for i in range(k+1):
        if i%2!=0:
            a+=i**2
    return a
x=sumoddsquares(6)
print(x)


# In[19]:


def distinctoddpairgen(array):
    a=[]
    for i in range (len(array)-1):
        print(i)
        for j in range(len(array)):
            if (array[i]*array[j])%2!=0 and i!=j:
                a.append((array[i],array[j]))
    return a
x=distinctoddpairgen([1,3,4,6,7])
print(x)


# In[24]:


def distinctoddpairgen(array):
    return [(array(i),len(array)-i) for i in range(len(array) ) if (array[i]*(len(array)-i))%2!=0]
x=distinctoddpairgen([1,3,4,6,7])
print(x)


# In[9]:


def Reverse(list):
    return list[::-1]
x=Reverse([1,2,3,4,5])
print(x)


# In[10]:


def Unique(y):
    return  list(set(y))
x=Unique([1,2,3,3,4,4,5,6,7,5])
print(x)   


# In[13]:


def UserNumbers(y):
    a=[i for i in range(1,len(y)+1) if i %2 ==0 ]
    print(a)
    print("last element: ",a[-1])
    print(max(a))
    print(min(a))
    print(a[-2])
user=input("enter numbers comma seperated")
UserNumbers(user.split(","))
    


# In[14]:


def ShowExcitement(y):
    for i in range(5):
        print(y,end=" ")
x="A quick brown fox jumps over the lazy dog"
ShowExcitement(x)


# In[15]:


def Greater(n1, n2, n3):
    a=[n1,n2,n3]
    return(max(a))
print(Greater(3,5,8))


# In[16]:


def divide(dividend,divisor):
    return (dividend//divisor,dividend%divisor)
           
print(divide(10,3))


# In[17]:


class Person:
    def __init__ (self, name, age):
        self.name=name
        self.age=age
    
    def birthday(self):
        self.age+=1
        return self.age  
a=Person("myra",19)
print (a.birthday())
        


# ---
# ### 1.1	
# A click counter is a small hand-held device that contains a push button and a count display. To increment the counter, the button is pushed and the new count shows in the display. Clicker counters also contain a button that can be pressed to reset the counter to zero. Design and implement the Counter ADT that functions as a hand-held clicker.

# In[2]:


class Counter:
    def __init__(self):
        self._start=0
    def push(self):
        self._start+=1
    def down(self):
        assert self.start>0 ,"already counter is zero"
        self._start-=1
    def get(self):
        return self._start
    def reset(self):
        self._start=0
c=Counter()
c.push()
c.push()
c.push()
print(c.get())
c.reset()
print(c.get())


# ---
# ### 1.2	
# A Grab Bag ADT is similar to the Bag ADT with one difference. A grab bag does not have a remove() operation, but in place of it has a grabItem() operation, which allows for the random removal of an item from the bag. Implement the Grab Bag ADT.

# In[18]:


import random
class CountBag:
    def __init__(self):
        self._items = list()

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items
    def add(self, item):
        self._items.append(item)
    def grabItem(self):
        assert item in self._items, "The item must be in the bag."
        c=random.choice(self._items)
        ndx = self._items.index(random.choice(self._items))
        return self._items.pop(ndx)

    def __iter__(self):
        return _BagIterator(self._items)

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

B =Bag()
B.add(49)
B.add(7)
B.add(20)
B.add(2)
print(B._items)
print(B.grabItem())
print("items in bag")
for item in B:
    print(item)


# ---
# ### 1.3
# A Counting Bag ADT is just like the Bag ADT but includes the numOf(item) operation, which returns the number of occurrences of the given item in the bag. Implement the Counting Bag ADT and defend your selection of data structure.
# 
# 

# In[36]:


import random
class CountBag:
    def __init__(self):
        self._items = list()

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items
    def add(self, item):
        self._items.append(item)
    def remove(self, item):
        assert item in self._items, "The item must be in the bag."
        ndx = self._items.index(item)
        self._items.pop(ndx)
        return self._items
    def numOf(self,item):
        return self._items.count(item)
            
    def __iter__(self):
        return _BagIterator(self._items)

class _BagIterator:
    def __init__(self, List):
        self._bagItems = List
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

B =CountBag()
print(len(B))
B.add(49)
B.add(7)
B.add(7)
B.add(20)
B.add(2)
print(B.numOf(7))
print(B.remove(2))
for item in B:
    print(item)


# ---
# ### 1.4	
# The use of the Student File Reader ADT makes it easy to extract student records from a text _le no matter the format used to store the data. Implement a new version of the ADT to extract the data from a text file in which each record is stored on a separate line and the individual fields are separated by commas. For example, the following illustrates the format of a sample file containing three student records:
# 
# 10015, John, Smith, 2, 3.01
# 10334, Jane, Roberts, 4, 3.81
# 10208, Patrick, Green, 1, 3.95
# 

# In[19]:



class StudentFileReader:
    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputFile = None
    def open(self):
        self._inputFile = open(self._inputSrc,"r")
    def close(self):
        self._inputFile.close()
        self._inputFile=None
    def fetchRecord(self):
        line=self._inputFile.readline().strip()
        if line =="":
            return None
        line=line.split(',')
        student=StudentRecord()
        student.idNum =int (line[0])
        student.firstName= line[1]
        student.lastName=line[2]
        student.classCode=int(line[3])
        student.gpa=float(line[4])

        return student
    def fetchAll(self):
        records=list()
        student=self.fetchRecord()
        print("     ID     | First Name  |Last Name |Class Code |GPA")
        while student!=None:
            print(f"{student.idNum:10}  | {(student.firstName):12}|{ student.lastName:10}| {student.classCode:10}|{student.gpa}")
            student=self.fetchRecord()
            
class StudentRecord:
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0
    def getRecord(self):
        return [self.idNum,self.firstName ,self.lastName ,self.classCode ,self.gpa]
file="students.txt"
# fileopen=open("students.txt","r")
# print(fileopen.readlines())
record=StudentFileReader(file)
record.open()

print(record.fetchAll())               


# ---
# ### 1.5
# In the lecture 1, we defined and implemented the Student File Reader ADT for extracting student records from an external source. We can define and use a similar ADT for output.
# 
# a)	Design a Student File Writer ADT that can be used to display, or store to an output device, student records contained in a Student Record object.
# 
# b)	Provide an implementation of your ADT to output the records by displaying them to the terminal in a neatly formatted fashion.
# 
# c)	Provide an implementation of your ADT to output the records to a text file using the same format described in the text.
# 
# d)	Design and implement a complete program that extracts student records from a text file, sorts them by either student id or student name, and displays them to the terminal using your ADT. The choice of sort keys should be extracted from the user.
# 

# In[ ]:


class StudentFileWriter:
    def __init__(self,)


# ---
# ### 1.6	
# A line segment is a straight line bounded by two endpoints. The Line Segment ADT, whose operations are described below, represents a line segment defined by points in the two-dimensional Cartesian coordinate system. Use the Point class from Appendix D and implement the Line Segment ADT.
# <>
# <li>LineSegment(ptA,ptB): Creates a new Line Segment instance defined by the two Point objects.
# <li>endPointA(): Returns the first endpoint of the line.
# <li>endPointB(): Returns the second endpoint of the line.
# <li>length (): Returns the length of the line segment given as the Euclidean distance between the two endpoints.
# <li>toString (): Returns a string representation of the line segment in the format (Ax, Ay)#(Bx, By).
# <li>isVertical(): Is the line segment parallel to the y-axis?
# <li>isHorizontal(): Is the line segment parallel to the x-axis?
# <li>isParallel(otherLine): Is this line segment parallel to the otherLine?
# <li>isPerpendicular(otherLine): Is this line segment perpendicular to the otherLine?
# <li>intersects(otherLine): Does this line segment intersect the otherLine?
# <li>bisects(otherLine): Does this line segment bisect the otherLine?
# <li>slope(): Returns the slope of the line segment given as the rise over the run. If the line segment is vertical, None is returned.
# <li>shift(xInc,yInc): Shifts the line segment by xInc amount along the x-axis and yInc amount along the y-axis.
# <li> midpoint(): Returns the midpoint of the line segment as a Point object.
# 

# In[1]:


print("ID /t num /t/t gpa")


# ---
