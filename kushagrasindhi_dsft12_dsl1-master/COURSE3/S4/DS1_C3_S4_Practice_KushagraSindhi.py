#!/usr/bin/env python
# coding: utf-8

# In[10]:


# task 1, print factorial of input 
i = 1
num = int(input("Enter number"))
tempnum = num
while num >= 1:
    i *= num
    num -= 1
print(i, 'is the factorial of ', tempnum)


# In[12]:


# task 2 prime numbers until 20
count = 0
i = 1
while i <= 20:
    j = 1
    while j < i:       
        if(i % j == 0):
            count += 1
        j += 1
    if(count == 1):
        print(i)
    count=0    
    i += 1


# In[15]:


# task 3 sum of all digits 
t3sum = 0
t3i = 0
t3var = input("Enter num = ")
while t3i < len(t3var):
    t3sum += int(t3var[t3i])
    t3i += 1
print(t3sum)


# In[1]:


# task 4 fibonacci series until 21
num = int(input("Enter number"))
j = 1
k = 2
l = 0
while(l <= num):
    print(j)
    l = j + k
    j = k
    k = l


# In[16]:


# task 5 adding two objects and displaying their memory address
t1 = ()
t2 = ()
print(id(t1))
print(id(t2))
t1 = t1 + t2
print(id(t1))

# ID of t1 and t2 is same because both of them have the same value, ie. blank/ empty. After adding t2 to t1 the value remains same 
# because even after adding, the value remains the same, ie. blank/ empty.


# In[7]:


# task 6 adding values of set n in set m
m = {10, 20, 30, 40, 50}
n = {30, 40, 50, 60, 70}
m.update(n)
print(m)
# common elements got automatically omitted/ removed since a set in python cannot hold duplicate values


# In[10]:


# task 7 print even values from list
i = 0
port1 = {'FTP': 1, 'SSH': 2, 'telnet': 3, 'http': 4}
for i in port1.values():
    if(i % 2 == 0):
            print(i)


# In[11]:


# task 8 dictionary with keys and values as numbers and square between 1 and 15 + add 100:100000 element at the bottom 
t9dict = {}
i = 1
while i <= 15:
    t9dict[i] = i ** 2
    i += 1
print('before update', t9dict)
t9dict[100] = 100000
print('after update', t9dict)


# In[12]:


# task 9 
port1 = {21: 'FTP', 22: 'SSH', 23: 'telnet', 80: 'http'}
port2 = dict([value, key] for key, value in port1.items())
print('before reverse', port1)
print('after reverse', port2)


# In[21]:


# task 10, remove duplicate item from dictionary

Employee = {'Emp1': {'name': 'Sara', 'Dept': 'IT', 'Designation': 'Team Lead' },
            'Emp2': {'name': 'Anna', 'Dept': 'IT', 'Designation': 'Senior Software Engineer' }, 
            'Emp3': {'name': 'Andy', 'Dept': 'BioTech', 'Designation': 'Senior Software Engineer' }, 
            'Emp4': {'name': 'Andy', 'Dept': 'BioTech', 'Designation': 'Senior Software Engineer' } }
    
print('before deletion = ', Employee)
print('____________________________________________________________________________________________')
Employee.pop('Emp4')
print('after deletion = ', Employee)

