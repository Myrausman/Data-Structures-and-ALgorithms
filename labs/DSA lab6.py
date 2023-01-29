#!/usr/bin/env python
# coding: utf-8

# ### Lab6
# ##### Maira usman
# ##### 21B-011-se

# In[55]:


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self._head = None
        
    def traversal(self):
        curNode = self._head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next

    def unorderedSearch(self, target):
        curNode = self._head
        while curNode is not None and curNode.data != target:
            curNode = curNode.next
        return curNode is not None

    def prependNode(self, item):
        newNode = ListNode(item)
        newNode.next = self._head
        self._head = newNode

    def removeNode(self, item):
        predNode = None
        curNode = self._head
        while curNode is not None and curNode.data != item:
            predNode = curNode
            curNode = curNode.next

        assert curNode is not None, "Item must be in the Linked List!"
        if curNode is self._head:
            self._head = curNode.next
        else:
            predNode.next = curNode.next
List = LinkedList()
List.prependNode(2)
List.prependNode(7)
List.prependNode(3)
List.prependNode(8)
List.removeNode(3)
print("1 in list: ", List.unorderedSearch(2))
print("2 in list: ", List.unorderedSearch(8))
List.traversal()


# In[42]:


class Bag :
    
    def __init__( self ):
        self._head = None
        self._size = 0

  # Returns the number of items in the bag.
    def __len__( self ):
        return self._size

  # Determines if an item is contained in the bag.
    def __contains__( self, target ):
        curNode = self._head
        while curNode is not None and curNode.item != target :
            curNode = curNode.next
        return curNode is not None

  # Adds a new item to the bag.
    def add( self, item ):
        newNode = _BagListNode( item )
        newNode.next = self._head
        self._head = newNode
        self._size += 1
    def __str__(self):
        if self._head is None:
            print("linked List is empty")
            return
        iter = self._head
        output="{"
        while iter:
            output+= str(iter.item) + ","
            iter=iter.next
        return output+"}"
  # Removes an instance of the item from the bag.
    def remove( self, item ):
        predNode = None
        curNode = self._head
        while curNode is not None and curNode.item != item :
            predNode = curNode
            curNode = curNode.next

      # The item has to be in the bag to remove it.
        assert curNode is not None, "The item must be in the bag."

      # Unlink the node and return the item.
        self._size -= 1
        if curNode is self._head :
            self._head = curNode.next
        else :
            predNode.next = curNode.next
        return curNode.item

      # Returns an iterator for traversing the list of items.
    def __iter__( self ):
        return _BagIterator( self._head )

  # Defines a private storage class for creating list nodes.
class _BagListNode( object ):
    def __init__( self, item ) :
        self.item = item
        self.next = None
class  _setiterator:
    def __init__(self,head):
        self._curNode=head
    def __iter__(self):
        return self
    def __next__(self):
        if self._curNode is None: 
            entry=self._curNode.data
            self._curNode= self._curNode.next
            return entry
        else:
            raise StopIteration     
robert=Bag()
robert.add(1)
robert.add(3)
robert.add(5)
robert.add(7)
robert.remove(1)
print(robert)


# In[61]:


class ListNode :
    def __init__ ( self , data ) :
        self . data = data
        self . next = None
  
    def traversal ( self, head ) :
        curNode = head
        while curNode is not None :
            print (curNode . data)
            curNode = curNode.next

    def unorderedSearch( head, target ): 
        curNode = head 
        while curNode is not None and curNode.data != target : 
            curNode= curNode.next 
        return curNode is not None
        newNode = ListNode( item ) 
        newNode.next = head 
        head = newNode
        predNode = None 
        curNode = head 
        while curNode is not None and curNode.data != target : 
            predNode = curNode 
            curNode = curNode.next 
        if curNode is not None : 
            if curNode is head : 
                head = curNode.next 
            else : 
                predNode.next = curNode.next

    def removeAll(self):
        while self is not None:
            if self!=None:
                temp=self
                self=self.next
                temp.data=None
        print("All nodes are deleted successfully.")
a = ListNode( 11 )
b = ListNode( 52 )
c = ListNode( 18 )
a.next=b
b.next=c
print(a.data)
print(a.next.data)
print(a.next.next.data)
# a.removeAll(1)
print(a.unorderedSearch(1))
a.removeAll()
print(a.data)
print(a.next.data)
print(a.next.next.data)


# In[45]:


#task2
class Node:
    
    def __init__(self, data, next = None):
        
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):       
        self.head = None
        
    def splitInHalf(self, listt1, listt2):
        first = self.head
        second = first.next
        while (first is not None and second is not None and first.next is not None):
            self.MoveNode(listt1, first) 
            self.MoveNode(listt2, second) 
            first = first.next.next
            if first is None:
                break
            second = first.next
            
    def MoveNode(self, dest, node):
        new_node = Node(node.data)
        if dest.head is None:
            dest.head = new_node
        else:
            new_node.next = dest.head
            dest.head = new_node

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print (temp.data)
            temp = temp.next 
        print("")

list0 = LinkedList()
listt1 = LinkedList()
listt2 = LinkedList()

list0.push(5)
list0.push(4)
list0.push(3)
list0.push(2)
list0.push(1)
list0.push(0)

list0.splitInHalf(listt1,listt2)

print("Original Linked List: ")
list0.printList()

print ("Resultant Linked List 01 : ")
listt1.printList()

print ("Resultant Linked List 02 : ")
listt2.printList()


# In[46]:


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


# In[16]:


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

    def sorted_add(self, new_node): 
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
       
    def sorted_add(self,element):
        newnode=Node(element)
        self.__size+=1
        self.elements.sorted_add(newnode)
        return
    def remove(self,ndx):
        assert ndx<len(self) and ndx>=0,"Invalid Index"
        self.elements.remove(ndx)
        self.__size-=1

    def __str__(self):
        if self.elements.head is None:
            print("linked List is empty")
            return
        iter = self.elements.head
        output="{"
        while iter:
            output+= str(iter.data) + ","
            iter=iter.next
        return output+"}"   

    def union(self,setB):
        newSet=Set()
        newSet.elements=self.elements
        for element in setB:
            if element not in self:
                newSet.sorted_add(element)
            return newSet

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
set1.sorted_add(5)
set1.sorted_add(6)
set1.sorted_add(7)
set1.sorted_add(0)
# set1.remove()
print("SET1")
print(set1)
set2=Set()
set2.sorted_add(8)
set2.sorted_add(1)
set2.sorted_add(3)
set2.sorted_add(4)
print("SET2")
print(set2)
print("Union")
print(set1.union(set2))


# In[ ]:




