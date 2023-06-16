#!/usr/bin/env python
# coding: utf-8

# In[25]:


# task 1 checks if the input is a palindrome or not

def palincheck(str):
    if(str == str[::-1]):
        return str, "is a Palindrome"
    else:
        return str, 'is not a Palindrome'
print(palincheck(input("Enter the word = ")))


# In[21]:


# task 2 sorting string (converts string into list, sorts list and converts string back to string)

list = []
def wordsort(words):
    for i in words:
        list.append(i)
    list.sort()
    sorted_word = ""  # why did global variable not work?
    for i in list:
        sorted_word += i
    return sorted_word
argvar = input("Enter word = ")
print("sorted string is", wordsort(argvar))
# why is uppercase not being sorted?


# In[15]:


# task 3 list to string conversion

import functools as x

def listostr(li):
    return x.reduce(lambda x, y: x + y, li)
print(listostr(['Parry ', 'Hotter ', 'is ', 'real']))


# In[22]:


# task 4 insert number in a list and display largest and smallest
            
def smlg():
    li = []
    for i in range(int(input("Total elements = "))):
        li.append(int(input("Enter number = ")))
    print(li, "Is the final list")
    return "Max number is ", max(li), "Smallest number is ", min(li)

print(smlg())


# In[2]:


# task 5 create dictionary, insert keys and values and display largest and smallest values

def dict():
    di = {}
    for i in range(5):
        k = input("Enter keys = ")
        v = float(input("Enter values = "))
        di.update({k:v})
    print("final dictionary is = ", di)  
    return max(di.values()), "is the max value", min(di.values()), 'is the smallest value'

print(dict())


# In[4]:


# task 6 take input, display details using inner functions

def func():
    name = input("enter name = ")
    age = int(input("enter age = "))
    gender = input("enter gender")
    
    def prnt(na, ag, gen):
        print('%10s %10s %10s' % ("Name", "Age", "Gender"))
        print('%10s %10s %10s' % (na, ag, gen))
        
    prnt(name, age, gender)
print(func())


# In[6]:


# task 7 calulcate the math expression on input numbers, calling outer function inside of another function

def sq():
    num1 = int(input("Enter number #1 = "))
    num2 = int(input("Enter number #2 = "))
    return sqin(num1, num2)
    
def sqin(a, b):
    return a**2*b

print(sq())


# In[16]:


# task 8 sorting a dictionary

color = [('black', 4), ('green', 1), ('red', 5), ('blue', 2), ('yellow', 3)]
color.sort(key=lambda x:x[1])
print(color)


# In[17]:


# task 9 find the intersection or the common value in the list using lamba functions

a = ["Andy", "Mandy", "Sandy"]
b = ["Handy", "Brandy", "Mandy"]
print(list( filter( lambda x : x in a, b)))


# In[18]:


# task 10 addition of two list using lambda functions

c = [12,13,14]
d = [17,16,15]
li = list(map(lambda c, d : c + d, c, d))
print(li)

