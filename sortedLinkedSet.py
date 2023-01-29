#sorted Set
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

  def index(self,element):
    count=0
    iter= self.head
    while iter:
      if iter.data==element:
        return count
      iter=iter.next 
      count+=1  

  def add(self,element):
    new_node=Node(element)
    # for the empty linked list
    if self.head is None:
        new_node.next = self.head
        self.head = new_node

    #for head at end
    elif self.head.data >= new_node.data:
        new_node.next = self.head
        self.head = new_node
    else :
        # Locate the node before the point of insertion
        current = self.head
        while(current.next is not None and
                current.next.data < new_node.data):
            current = current.next
            
        new_node.next = current.next
        current.next = new_node

    
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
    self._theElements=LinkedList()
    self.size=0
  def __len__(self):
    return self.size
  def __contains__(self,element):
    iter=self._theElements.head
    while iter:
      if iter.data==element:
        return True
      iter=iter.next
    return False
  def add(self,element):
    if element not in self:
      self._theElements.add(element)
      self.size = self.size+1
  def remove(self,element):
    assert element in self._theElements,"The element must be in the set."
    self._theElements.remove(element)
    self.size= self.size-1
  def __eq__(self,setB):
    if len(self) != len(setB):
      return False
    else:
      return self._theElements.isSubsetOf(setB)
  def isSubsetOf(self,setB):
    for element in self:
      if element not in setB:
        return False
    return True 
  def union(self,setB):
    newSet=Set()
    newSet._theElements=self._theElements
    for element in setB :
      if element not in self:
        newSet._theElements.add(element)
    return newSet
  def intersect(self,setB):
    newSet=Set()
    for element in self:
      if element in setB:
        newSet.add(element)
    return newSet
  def difference(self,setB):
    newSet=Set()
    for element in self:
      if element not in setB:
        newSet.add(element)
    return newSet
  def properset(self,setB):

    x=self.intersect(setB)
    if len(self)==len(x):
      return False
    else:
      return True
  def __str__(self):
    iter = self._theElements.head
    output="{"
    while iter:
      output+= str(iter.data) + ","
      iter=iter.next

    return output[:-1]+"}"
  def __iter__(self):
      return _setiterator(self._theElements.head)

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
set1.add(3)
print(set1,"<--set 1")
set2=Set()
set2.add(5)
set2.add(7)
set2.add(2)
set2.add(6)
print(set2,"<--set 2")
z=set1.intersect(set2)
print(z,"<--intersect")
x=set1.union(set2)
print(x,"<--union")
y=set1.properset(set2)
print(y,"-- properset")



