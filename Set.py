class Set:
    def __init__(self,*initElements):
        self._elements= list(initElements)
    def __len__(self):
        return len(self._elements)
    def __contains__(self,item):
        return item in self._elements
    def add(self,item):
        if item not in self:
            self._elements.append(item)
    def remove(self,item):
        assert item in self,"element must be in the set"
        self._elements.remove(item)
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
    def __str__(self):
        elements=str(self._elements)    
        return f"{{{elements[1:-1]}}}"

           
        
            
            
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
B=Set(150,75,23,86,49,20,25)

if A == B:
    print("A and B are equal")
else:
    sameelements=A.intersect(B)
if len(sameelements)==0:
    print("A and B does not have same elements")
else:
    print("A and B have some elements common  ")
print(sameelements)
# uniqueelements=B.difference(A)
print("letters that are not in B ")
# for elements in uniqueelements:
print(B.difference(A))
print("elements  that are in A & B ")
print(A.union(B))
print(A.ProperSet(B))
