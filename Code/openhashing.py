class _ListNode:
    def __init__(self,data):
        
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def append(self, data):
        curNode = self.head
        prevNode = None
        while curNode is not None:
            if curNode.data > data:
                break
            prevNode = curNode
            curNode = curNode.next

        newNode = _ListNode(data)
        if prevNode is None:
            newNode.next = self.head
            self.head = newNode
            self.length += 1
        else:
            newNode.next = curNode
            prevNode.next = newNode
            self.length += 1
            

    def remove(self, data):
        curNode = self.head
        prevNode = None
        if self.length > 0:
            if curNode.data == data:
                self.head = curNode.next
                curNode = curNode.next
                self.length -= 1
            while curNode != None:
                if curNode.data != data:
                    prevNode = curNode
                    curNode = curNode.next
                elif curNode.data == data: 
                    prevNode.next = curNode.next
                    curNode = curNode.next
                    self.length -= 1
        else:
            raise IndexError('Linked list is empty')




    def __str__(self):
        curNode=self.head
        llist="("
        while curNode is not None:
            llist+="-->"+str(curNode.data)
            curNode=curNode.next
        llist+=")"
        return  llist

    def __len__(self):
        return self.length
    def middle(self,start, last):
        
        if (start == None):
            return None
        slow = start
        fast = start . next
        while (fast != last):
            fast = fast . next
            if (fast != last):
                slow = slow . next
                fast = fast . next
        
        return slow    
    def binary_search(self,value):
        curNode = self.head
        last = None
        count=0
        while True :
          
            mid = self.middle(curNode, last)
#             print(mid.data)
            if (mid == None):
                return None
            if (mid . data == value):
                
                return f"{mid.data} is at position : {count}"
            elif (mid . data < value):
                curNode = mid . next
            else:
                last = mid
            if not (last == None or last != curNode):
                break
            count+=1
        return None   


    def __contains__(self, element):
        for nodes in self:
            if nodes == element:
                return True
        return False


class openhashing:
    def __init__(self,size):
        self.size=size
        self.data = [None]*size
        self.fslots = 0

    def __len__(self):
        return self.fslots
    def hashFunction(self, key, size):
        if key == "flag":
            return 0
        return key % size
    
    def add(self,item):
        hashKey = self.hashFunction(item, self.size)
        if self.data[hashKey] == None:
            self.data[hashKey] = LinkedList()
            self.data[hashKey].append(item)
#             print(self.data[hashKey])
            self.fslots += 1
        else:
            self.data[hashKey].append(item)
            self.fslots += 1
        
    def delete(self,item):
        hashKey = self.hashFunction(item, self.size)
        self.data[hashKey].remove(item)
            
        
    def search(self, item):
        hashkey = self.hashFunction(item, self.size)
        high=self.size-1
        low=0
        while low<=high:
            
            mid=(high+low)//2
            if mid==hashkey and self.data[mid] is not None:
                
                return f"{self.data[mid].binary_search(item)} at  position : {mid} in {self}"
            elif mid>hashkey:
                high=mid-1   
            elif mid<hashkey:
                low=mid+1
        return "item not found"    
    def __str__(self):
        llist="["
        for item in range(len(self.data)):
            if self.data[item] == self.data[-1]:
                llist+=str(self.data[item])
            else:
                llist+=str(self.data[item])+","
        llist+="]"
        return llist
    

oh=openhashing(4)
data=[35,76,98,65,45,32,78,75,89,68,26,25]
# data=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for item in data:
    oh.add(item)
print(oh)
oh.delete(9)

print("---"*10,"searching 35 ","---"*10,"\n",oh.search(35))
print()
print("---"*10,"after deleteing","---"*10,"\n\n",oh)