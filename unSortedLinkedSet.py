#unsorted set
class Node:
  def __init__(self,data,next=None):
    self.data=data
    self.next=next
class LinkedList:
  def __init__(self):
    self.head=None  

  def __len__(self):
    count,iter=0,self.head
    while iter:
      iter=iter.next
      count+=1
    return count  


  def append(self,elmnt):
    node=Node(elmnt,None)
    node.next=self.head
    self.head= node

  def remove_val(self,val):
    current=self.head
    prev=current
    while current.data!=val:
      if current.next==None:
        print("No such Item")
        return
      prev=current
      current=current.next
    prev.next=current.next

  def remove(self,ndx):
    iter,count=self.head,0
    if ndx==0:
      self.head=iter.next
      return  
    while iter:
      if count==ndx-1:
        iter.next=iter.next.next
        return
      iter=iter.next
      count+=1   

class Set:
  def __init__(self):
    self.elements=LinkedList()
    self.__size=0

  def __len__(self):
    return self.__size

  def __contains__(self,elmt):
    iter= self.elements.head
    while iter:
      if iter.data==elmt:
        return True
      iter=iter.next  
    return False    

  def add(self,elmnt):
    assert not(elmnt in self), "Element Exists"
    self.__size+=1
    self.elements.append(elmnt)

  def remove(self,ndx):
    assert ndx<len(self) and ndx>=0,"Invalid Index"
    self.elements.remove(ndx)
    self.__size-=1
      
  def __str__(self):
    if self.elements.head is None:
      return "Set is empty"
    iter = self.elements.head
    output="{"
    while iter:
      output+= str(iter.data) + ","
      iter=iter.next

    return output[:-1]+"}"   

  def union(self,setB):
    newSet=Set()
    newSet.elements=self.elements
    for element in setB:
      if element not in self:
        newSet.elements.append(element)
    return newSet

  def intersection(self,setB):
    newSet=Set()
    for element in setB:
      if element in self:
        newSet.add(element)
    return newSet

  def isSubsetOf(self,setB):
    for element in self:
      if element not in setB:
        return False
    return True

  def difference(self,setB):
    newSet=Set()
    # newSet.elements=self.elements
    newSet.__size=self.__size
    for element in self:
      if element not in setB:
        newSet.add(element)    
    return newSet 

  def properSubset(self,setB):
    if not (len(setB)==len(self)):
      return  len(self.intersection(setB))==len(setB)

  def __iter__(self):
      return _setiterator(self.elements.head)

class  _setiterator:
  def __init__(self,elements):
    self._elements=elements
  def __iter__(self):
    return self
  def __next__(self):
    if self._elements!=None: 
      entry=self._elements.data
      self._elements= self._elements.next
      return entry
    else:
      raise StopIteration      

set1=Set()
set1.add(2)
set1.add(7)
set1.add(4)
print("SET1")
print(set1)
set2=Set()
set2.add(5)
set2.add(6)
set2.add(7)
set2.add(4)
set2.add(44)
print("SET2")
print(set2)
print("Differecec")
print(set1.difference(set2))
print(set2.intersection(set1),"intersection")
print(set1.union(set2),"<--union")