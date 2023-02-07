#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from matplotlib import pyplot as plt
import random


# In[10]:



def linearsearch(seq,item):
    counter=0
    for i in seq:
        counter+=1
        if item == i:
            return counter
    counter=0
    return counter
# linearsearch([1,3,4,11,23,65,78,65],65)
def sortedlinear(seq,item):
    counter=0
    for i in seq:
        counter+=1
        if i == item:
#             print(" found")
            return counter
        elif i>item:
            counter=0
            return counter
    counter=0
    return counter
def binarysearch(seq,item):
    n=len(seq)
    low=0
    high=n-1
    counter=0
    while low<=high:
        counter+=1
        mid=(low+high)//2
        if seq[mid]==item:
            return counter
        elif seq[mid]<item:
            low=mid+1
        else:
            high=mid-1
    counter=0
    return counter
        
def simulation(n):
    step1=[0]*n
    step2=[0]*n
    step3=[0]*n
    matrix=[i for i in range(n)]
    matrix1=[i for i in range(n)]
    random.shuffle(matrix1)
    for i in range(n):
        b=random.choice(matrix)
        step1[i]=linearsearch(matrix1,b)
        step2[i]=sortedlinear(matrix,b)
        step3[i]=binarysearch(matrix,b)
    print("complexity of linear search: ",sum(step1)//len(step1),"%")
    print("complexity of sorted linear search: ",sum(step2)//len(step2),"%")
    print("complexity of binary search: ",sum(step3)//len(step3),"%")
    x=list(range(10))
    plt.plot(x,step1)
    plt.plot(x,step2)
    plt.plot(x,step3)
    plt.grid(which="both")
    plt.legend(["linear search","sortedlinear search","binary search"])
    plt.show()
simulation(10)


# In[4]:



def bubblesort(seq):
    n=len(seq)
    counter=0
    for i in range(n):
        for j in range(n-i-1):
            if seq[j]>seq[j+1]:
                counter+=1
                seq[j],seq[j+1]=seq[j+1],seq[j]
    return counter
def insertionSort( theSeq ): 
    n = len( theSeq ) 
    count=0
    for i in range( 1, n ) : 
        value = theSeq[i]
        
        pos = i 
        while pos > 0 and value < theSeq[pos - 1] : 
#             print(value,"v",theSeq[pos-1],"seq")
            theSeq[pos] = theSeq[pos - 1] 
            pos -= 1  
            count+=1
#             print(theSeq)
        theSeq[pos] = value 
        count+=1
#         print(theSeq)
    return count
def selectionsort(seq):
    n=len(seq)
    count=0
    for i in range(n-1):
        small=i
        for j in range(i+1,n):
            if seq[j]<seq[small]:
                small=j
            if i!=small:
#                 count+=1
                seq[i],seq[small]=seq[small],seq[i]
            count+=1
    return count
                
        
def simulation(n):
    step1=[0]*n
    step2=[0]*n
    step3=[0]*n
    matrix1=[i for i in range(n)]
    print("length of array is :",len(matrix1))
    for i in range(n):
        random.shuffle(matrix1)
        print("array to be sorted: ",matrix1)
        step1[i]=bubblesort(matrix1)
        step2[i]=insertionSort(matrix1)
#         print(step2)
        step3[i]=selectionsort(matrix1)
            
    x=list(range(n))
    plt.plot(x,step1)
    plt.plot(x,step2)
    plt.plot(x,step3)
    plt.grid(which="both")
    plt.legend(["bubble sort","insertion sort","selectionsort"])
    plt.show()
simulation(20)
# values=([1,15,61,7,8])
# c=insertionsort(values)
# print(c)                


# In[ ]:




