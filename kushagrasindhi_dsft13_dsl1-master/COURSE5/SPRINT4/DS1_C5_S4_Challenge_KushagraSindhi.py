#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import numpy as np
from scipy.stats import binom, poisson
import matplotlib.pyplot as plt
import math
import seaborn as sns


# In[2]:


# task1

X =   [6   ,    7,    8,    9,   10,   11,   12,   13,   14]
p_x = [0.03, 0.08, 0.15, 0.20, 0.19, 0.16, 0.10, 0.07, 0.02]

tab = pd.DataFrame({'Days lost': X, 'Probability': p_x})
tab


# In[3]:


# a) number of days does not exceed 9


print("Probability that number of days does not exceed 9 is ", tab['Probability'][:4].sum())


# In[4]:


# b) number of days lost will be between 7 to 13

print('Probability that the number of days lost will be between 7 to 13 days is ' , tab['Probability'][1:8].sum())


# In[6]:


# c) 0 days will be lost


print('Probability that 0 days will be lost is', 1-sum(tab['Probability']))


# In[41]:


# d) Expected Value/ Mean & standard deviation

mean = 0
var = 0

for i, j in zip(X, p_x):
    mean += i*j
        
for i, j in zip(X, p_x):
    var += ((i-mean)**2)*j
    
std = math.sqrt(var)

print(f'Expected Value/ Mean is {mean} and Standard Deviation is {std}')


# In[58]:


# e)

plt.figure(figsize=(15, 5))
sns.barplot(x = X, y = p_x )
plt.xlabel('Probability')
plt.ylabel('Number of days')
plt.title('Probability of days lost');


# In[64]:


# task 2

p = 0.20
n = 15


# In[74]:


# a

k = 5
a = poisson.pmf(k, p)
a

print('Probability of exactly 5 companies = ', a)


# In[70]:


# b

k2 = 9

b = 1 - poisson.cdf(k2, p)
print('Probability of more than 9 campanies = ', b)


# In[79]:


# c)

k3 = 0

c = poisson.pmf(k3, p)
print('Probability of none of the companies using = ', c)


# In[71]:


# d

k4 = np.arange(4, 8)

d = poisson.pmf(k4, p)
print('Probability of companies ranging from 4 to 7 = ', d)


# In[86]:


# e)

plt.figure(figsize=(15, 10))


plt.subplot(2, 2, 1)
plt.plot(a, 'o-')
plt.title('Probability of exactly 5 companies')
plt.xlabel('Number of companies')
plt.ylabel('Probability')

plt.subplot(2, 2, 2)
plt.plot(b, 'o-')
plt.title('Probability of more than 9 campanies')
plt.xlabel('Number of companies')
plt.ylabel('Probability')

plt.subplot(2, 2, 3)
plt.plot(c, 'o-')
plt.title('Probability of none of the companies using')
plt.xlabel('Number of companies')
plt.ylabel('Probability')

plt.subplot(2, 2, 4)
plt.plot(d, 'o-')
plt.title('Probability of companies ranging from 4 to 7')
plt.xlabel('Number of companies')
plt.ylabel('Probability');


# In[87]:


# 3

rate = 0.548


# In[90]:


# a) no trip last year

n1 = 0
a = poisson.pmf(n1, rate)
print('Probability that family did not make the trips is', a)


# In[91]:


# b) exactly one trips

n2 = 1
b = poisson.pmf(n2, rate)
print('Probability that family took exactly one trips is', b)


# In[93]:


# c) more than 2 trips

n3 = 1
c = 1 - poisson.cdf(n3, rate)
print('Probability that family took more than 2 trips is', c)


# In[115]:


# d) 3 or less trips in 3 years

n4 = np.arange(0, 4)
d = poisson.pmf(n4, (rate*3))
print('Probability that family 3 or less trips in 3 years', d)


# In[110]:


# e) exactly 4 trips in 6 years

n5 = 4
e = poisson.pmf(n5, (rate*6))
print('Probability that family took exactly 4 trips in 6 years', e)


# In[117]:


# f)

plt.figure(figsize=(20, 15))

plt.subplot(3, 2, 1)
plt.plot(a, 'o-')
plt.title('family did not make the trips')
plt.xlabel('Number of Trips')
plt.ylabel('Probability')

plt.subplot(3, 2, 2)
plt.plot(b, 'o-')
plt.title('exactly one trip')
plt.xlabel('Number of Trips')
plt.ylabel('Probability')

plt.subplot(3, 2, 3)
plt.plot(c, 'o-')
plt.title('more than 2 trips')
plt.xlabel('Number of Trips')
plt.ylabel('Probability')

plt.subplot(3, 2, 4)
plt.plot(d, 'o-')
plt.title('3 or less trips in 3 years')
plt.xlabel('Number of Trips')
plt.ylabel('Probability')

plt.subplot(3, 2, 5)
plt.plot(e, 'o-')
plt.title('exactly 4 trips in 6 years')
plt.xlabel('Number of Trips')
plt.ylabel('Probability');

