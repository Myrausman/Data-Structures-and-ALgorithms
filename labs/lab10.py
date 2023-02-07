#!/usr/bin/env python
# coding: utf-8

# In[32]:


class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
        self.prev=None      
class Doubly_linked_list:
    def __init__(self):
        self.head=None        
       
     ### ADDITION   
    def prepending(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node 
        else:
            new_node.next=self.head 
            self.head.prev=new_node
            self.head=new_node 
  
    def postpending(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=None
        else:
            n=self.head 
            while n.next is not None:
                n=n.next 
            n.next=new_node
            new_node.prev=n
    
    ### DELETION 
    def del_strt(self):
        if self.head is None:
            print("linked list is epmty!")
        else:
            print("deleted",self.head.data)
            self.head=self.head.next 
            self.head.prev=None
        
            
    def del_end(self):
         if self.head is None:
            print("linked list is epmty!")
         else:
           n=self.head 
           while n.next is not None:
               n=n.next 
               
           n.prev.next=None
           
    
    def Search(self,target):
        i = 1
        temp = None
        currNode = self.head
        if self.head == None:
            print("List is empty")
            return
        while currNode != None:
            if currNode.data == target:
                temp = True
                break
            currNode = currNode.next
            i = i+1

        if temp:
            print("The node is present in the list at position : ")
            print(i)
        else:
            print("The node isn't present in the list")
        
   ### LIST OPERATIONS     
    def fwd_traverse(self):
        if self.head is None:                                                                            
            print("linked list is empty! ")
        else:
            n=self.head 
            while n is not None:
                print(n.data,"---",end=" ")
                n=n.next 
                
                
                
    def bkw_traverse(self):
         if self.head is None:
            print("linked list is empty! ")
         else:
            n=self.head 
            while n.next is  None:
                n=n.next 
                
            while n is not None:
                print(n.data,"---",end=" ")
                n=n.prev 
                
                
obj1=Doubly_linked_list()
obj1.prepending(10)
obj1.postpending(20)
obj1.postpending(30)
print(obj1.fwd_traverse())
# print(obj1.bkw_traverse())
obj1.prepending(40)
print(obj1.fwd_traverse())
obj1.del_strt()
print(obj1.fwd_traverse())


# In[25]:


# ### task 2
class node: 
    def __init__(self, element, next):
        self._element = element
        self._next = next

class CircularQueue:

    def __init__(self):
        self._tail = None 
        self._size = 0  

    def _len_(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        
        else :
            self._tail._next = oldhead._next
        
        self._size -= 1
        return oldhead._element
    
    def enqueue ( self , e ) :
        newest =  node(e , None )
        if self.is_empty () :
            newest._next = newest 
            
        else :
            newest._next = self._tail._next 
            self._tail._next = newest 
        self._tail = newest 
        self._size += 1
    
    def rotate ( self ) :
        if self._size > 0:
            self._tail = self._tail._next
    def printQueue(self):
        q="--"
        for i in range(self._size):
            q+=str(self._tail._next._element)+"---"
            # print(self._tail._element)
            
            self._tail=self._tail._next
        print(q)
a=CircularQueue()
a.enqueue(10)     
a.enqueue(20)
a.enqueue(30)
a.enqueue(40)
a.enqueue(50)
print(a.first() )
a.printQueue()  
a.dequeue()
a.printQueue()
a.rotate()
a.printQueue()
a.rotate()
a.printQueue()


# In[22]:


## task 3
class createNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None


class multiLevelLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def traverseNext(self, Node, data):
        curNode = Node
        while (curNode != None):
            if curNode.data == data:
                return nextlink, True
            nextlink = curNode
            curNode = curNode.next
        return nextlink, False

    def traverseChild(self, Node):
        curNode = Node
        while (curNode != None):
            nextchild = curNode
            curNode = curNode.child
        return nextchild

    def createNode(self, data):
        duplicate = False
        if self._head == None:
            self._head = Node(data)
            self._size += 1
        else:
            curNode = self._head
            newNode, duplicate = self.traverseNext(curNode, data)
            if duplicate == True:
                print('item already exist, can not add into the list')
                return
            else:
                newNode.next = Node(data)
                self._size += 1

    def createChild(self, parent, child):
        isParent=False
        curNode=self._head
        if (curNode==None):
            print('list is empty, can not create a child')
            return
        else:
            while(curNode!=None):
                if (curNode.data==parent and curNode.child==None):
                    isParent=True
                    curNode.child=Node(child)
                    self._size += 1
                elif (curNode.data==parent and curNode.child!=None):
                    isParent=True
                    tmpNode = self.traverseChild(curNode.child)
                    tmpNode.child = Node(child)
                    self._size += 1
                curNode = curNode.next
            if isParent==False:
                print('{0} does not exist as parent, therefore {1} is not added as child of {0}'.format(str(parent),str(child)))

    def printList(self):
        count = 1
        curNode=self._head
        while (curNode!=None):
            print("->",curNode.data , end=' ')
            if curNode.child!=None:
                tmpNode = curNode.child
                while (tmpNode!=None):
                    print("---->( ", tmpNode.data, end=") ")
                    count = count + 1
                    tmpNode = tmpNode.child
            curNode=curNode.next
        print("\nSize : ", count)

    def searchItem(self, data):
        
        count = 1
        count1=0
        count2=0
        curNode=self._head
        while (curNode!=None):
            if curNode.data == data:
                print(data, "number is at Position:", count)  
            count2+=1
            count = count + 1    
            if curNode.child!=None:
                tmpNode = curNode.child
                while (tmpNode!=None):
                    if tmpNode.data == data:
                        print(data, "number is at Position:", count1,"of Parent Node that is at position:  ",count2)    
                    count1 = count1 + 1 
                    
                    tmpNode = tmpNode.child
            curNode=curNode.next


obj=multiLevelLinkedList()
obj.createNode(3)
obj.createNode(2)
obj.createChild(2,7)
obj.createChild(3,6)
obj.createChild(3,5)
obj.createChild(2,10)
obj.createChild(2,11)
obj.printList()
print("search for no.  7")
obj.searchItem(7)

# obj.printList()


# In[ ]:




