#!/usr/bin/env python
# coding: utf-8

# In[2]:


mynames = ['Joe', 'Zoe', 'world', 'Brad', 'Angelina', 'world', 'zuki', 'Tom', 'Paris', 'world', 'magic']


# In[30]:


# task 1, true if present, false if not
for i in range(len(mynames)):
    if(mynames[i] == 'USA'):
        print("TRUE")
        break
    else:
        print("FALSE")
        break


# In[19]:


# task 2, count of presense of word
count = 0
for i in range(len(mynames)):
    if(mynames[i] == 'world'):
        count += 1
print(count)


# In[28]:


# task 3, count of even and odd numbers
even_count = 0
odd_count = 0
dataset = list(range(1, 30))
for i in range(len(dataset)):
    if(dataset[i] % 2 == 0):
        print(dataset[i], "is even")
        even_count += 1
    else:
        print(dataset[i], "is odd")
        odd_count += 1
print("There are", even_count, "even numbers and ", odd_count, "odd numbers in the given list")


# In[94]:


# task 4, finds out first 5 even numbers and puts them in a new list
newlist = []
dataset = list(range(1, 30))  
for i in range(len(dataset)):  
    if(dataset[i] % 2 == 0):
        newlist.append(dataset[i])
        if(len(newlist) == 5):
            break
print(newlist)


# In[49]:


# task 5, last two odd numbers
count = 0
dataset = list(range(1, 30))
for i in dataset[::-1]:
    if(i % 2 != 0):
        print(i)
        count += 1
        if(count == 2):
            break;


# In[2]:


# task 6, 
x = []
y = []
for i in range(5):
    x.append(int(input("value of x = ")))
    y.append(int(input("value of y = ")))
x.extend(y)
print("x before appending y = ", x)
x.append(input("enter string = "))
print("final value of x", x)
print("final value of y", y)


# In[92]:


# task 7, first and last 10 elements where values are squares of numbers between 1 and 40

lis1 = []
for i in range(40):
    i *= i
    lis1.append(i)
print(lis1[:10:])
print(lis1[:-11:-1])


# In[63]:


# task 8, table of number
num = int(input("enter num"))
for i in range(1, 11):
    print(num, "X", i, "=", num * i)

