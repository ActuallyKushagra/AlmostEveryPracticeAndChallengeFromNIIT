#!/usr/bin/env python
# coding: utf-8

# In[6]:


# task 1 take input of 10 elements and reverse it
list = []
list2 = []
for i in range(10):
    list.append(input("Enter one word = "))
list2 = list[::-1]
print(list)
print(list2)


# In[4]:


# task 2 Reverse a list using list method (reverse())
l1 = []
for i in range(10):
    l1.append(input("Enter one word "))
print(l1, "before reverse")
l1.reverse()
print(l1, "After reverse")


# In[10]:


# task 3 add elements in list one by one (must contain duplicate values)
alist = []
for i in range(10):
    alist.append(input("enter element = "))
    print("Updated list looks like = ", alist)


# In[11]:


# task 4 print unique or non repeating values from list created in task 3, count() used
blist = []
for i in range(len(alist)):
    if(alist.count(alist[i]) == 1):
        blist.append(alist[i])
print(blist)


# In[12]:


# task 5 sort the list using sort()
print(blist)
blist.sort()
print(blist)


# In[13]:


# task 6 remove all elements one by one - pop()
for i in range(len(blist)):
    print(blist, "before popping")
    blist.pop()
    print(blist, "after popping")
    print("_________________________________________________")
    if(len(blist) == 0):
        break


# In[14]:


# task 7 numbers divivsible by 7 and 5 in range 1500 and 2700
for i in range(1500, 2701):
    if(i % 7 == 0 and i % 5 == 0):
        print(i)


# In[15]:


# task 8 print first 30 natural numbers but skip the ones divisible by number provided as input
lis = []
n = int(input("Enter value of n "))
for i in range(30):
    if(i % n == 0):
        continue
    else:
        lis.append(i)
print("List of numbers not divisible are", lis)


# In[30]:


# task 9 sum of two matrices. put result in another list
firstlist = [[ 1, 2, 3], [ 4, 5, 6], [ 7, 8, 9]]
secondlist=[[ 19, 18, 17] ,[ 16, 15, 14], [ 13, 12, 11]]
thirdlist = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3): 
        thirdlist[i][j]= firstlist[i][j] + secondlist[i][j]
print("third list is = ", thirdlist)


# In[32]:


# task 10, create nested lists by taking 18 inputs, 9 values each list.

firstlist = []       
for i in range(3):   
    a = []
    for j in range(3):  
        n=int(input("enter number = "))
        a.append(n)
    firstlist.append(a) 
print("firstlist = ", firstlist)   
secondlist = []
for i in range(3):
    b = []
    for j in range(3):
        n1 = int(input("enter number = "))
        b.append(n1)
    secondlist.append(b) 
print("secondlist = ", secondlist)

