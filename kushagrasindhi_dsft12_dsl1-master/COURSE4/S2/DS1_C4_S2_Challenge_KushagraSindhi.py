#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[ ]:





# In[2]:


# task 1 Generate random prices of 20 cars with index values ranging from 101 to 120

carprice = pd.Series(np.random.randint(30000, 50000, 20), index = np.arange(101, 121))
print(carprice)


# In[3]:


# task 2 count of cars with price greater than 40000

smithcar40k = carprice[carprice > 40000]
print(np.size(smithcar40k))


# In[12]:


# task 3 car prices for model numbers between 111 and 116

smithcarmod = carprice[10:16]
print(smithcarmod,'\n', max(smithcarmod), "is the highest price")


# In[5]:


# task 4 count of cars and their records of cars with price between 30000 and 40000

carbwt = carprice.between(30000, 40000)
print(f"""
There are {carbwt.size} cars priced between 30000 and 40000, 
they are 
{carprice[carbwt]}""")


# In[6]:


# task 5 cars with price greater than the average car price

cargrtavg = carprice[carprice > carprice.mean()]
print(f"""
There are a total of {cargrtavg.size} cars with price higher than average that is {carprice.mean()}
They are,
{cargrtavg}""")


# In[7]:


# task 6 add 3 new cars to the list with specified model numbers and prices

new = pd.Series([34000, 45000, 54000], index = [201, 202, 203])
carprice = pd.concat([carprice, new])
print('Updated car price list \n', carprice)


# In[8]:


# task 7 Offering 10% discount

f = pd.DataFrame(carprice)
ori = f[0]
f[0] = ori
disc = ori * 0.9
f[1] = disc
f.columns=["Original", "Discounted"]
f


# In[11]:


# task 8 number of cars before and after the discount between 30000 and 40000

pricebwt1 = f[((f.Original > 30000) & (f.Original < 40000))]
pricebwt2 = f[((f.Discounted > 30000) & (f.Discounted < 40000))]
print(f'There are {pricebwt1.size} cars before the discount has been applied')
print(f'There are {pricebwt2.size} cars after the discount has been applied')


# In[34]:


# task 9 5 least expensive cars

srt = carprice.sort_values()
print(srt[0:5])


# In[ ]:




