#!/usr/bin/env python
# coding: utf-8

# In[50]:


from numpy import genfromtxt
import numpy as np


# ## Part 1

# In[49]:


empdat = genfromtxt("DS1_C4_S1_Employee_Data_Challenge.csv", delimiter = ",", dtype = int, skip_header = 1)


# In[51]:


# task 1 average age of all employees

avage = np.mean(empdat[:, 1])
print(avage)


# In[52]:


# task 2 employees with age > 25 with total number

totem = np.where(empdat[:,1] > 25)
print('total number employees with age greater than 25 = ', np.size(totem))
print('List of employees with age greater than 25 \n', empdat[totem])


# In[31]:


# task 3  employee age => 35 > age > 30

age35 = np.where((empdat[:, 1] > 30) & (empdat[:, 1] < 35))
print('Employees with age greater than 30 but less than 35 \n', empdat[age35])


# ## part 2

# In[53]:


cusdat = genfromtxt('DS1_C4_S1_Shopping_Data_Challenge.csv', delimiter = ',', skip_header = 1, dtype = int)


# In[55]:


# task 1 customers with spending scores greater than 80

spscore = np.where(cusdat[0:, 3] > 80)
print('These are the customers with spending scores greater than 80 \n',cusdat[spscore])


# In[64]:


# task 2 rows with age between 20 and 24

cus = np.where((cusdat[0:, 1] >= 20) & (cusdat[0:, 1] <= 24))
print('Rows with age bweteen 20 and 24 \n', cusdat[cus,0:])


# In[71]:


# task 3 lowest and highest annual income

minin = np.where(cusdat[:,2] == (min(cusdat[:, 2])))
maxin = np.where(cusdat[:, 2] == (max(cusdat[:, 2])))

print("Lowest annual income  \n ", cusdat[minin,0:3:2])
print("_______________________________________________________________")
print("Highest annual income  \n", cusdat[maxin, 0:3:2])


# In[83]:


# task 4 customers with spending score > 75, min annual sal > 35000, age < 45

spagesal = np.where((cusdat[0:,3] > 75) & (cusdat[0:,2] > 35) & (cusdat[0:,1] < 45))
print(f"There are {np.size(spagesal)} customers eligible for discount, they are: \n {cusdat[spagesal]}")


# In[93]:


# task 5 new column with discount between 10 and 50%

discount = np.random.randint(10,51,200)
temp = discount.reshape(200,1)
cusdat = np.concatenate((cusdat, temp), axis = 1)
print('After discount is added \n', cusdat)


# In[92]:


# task 6 Customers with discount > 45

cu = cusdat[cusdat[0:, 4] > 45]
print('count of Customers with discount > 45 = ', cusdat[cu].size)
print('Customers with discount > 45 \n', cu)

