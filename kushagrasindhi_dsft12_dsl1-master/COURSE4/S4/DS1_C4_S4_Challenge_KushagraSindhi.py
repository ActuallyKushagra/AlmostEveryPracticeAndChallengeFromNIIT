#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from datetime import date


# In[2]:


data = pd.read_csv('DS1_C4_S4_Car_Prices_Data_Challenge.csv')


# In[14]:


# task 1 top 5 manufacturers with lowest car prices of 2014

t1 = data[data.year == 2014]
t1b = t1.groupby(by='make')[['sellingprice']].mean()
t1b.sort_values(by='sellingprice',ascending=True).head()


# In[5]:


# task 2  Price of BMW in 2010 and 2015

t22010 = data[(data.year==2010)&(data.make=='BMW')&(data.condition>4.5)][["sellingprice"]].mean()
t22015 = data[(data.year==2015)&(data.make=='BMW')&(data.condition>4.5)][["sellingprice"]].mean()

t2perc = (t22015 - t22010) * (100 / t22015)
print(t2perc)


# In[6]:


# task 3 difference between average wholesale price of black and gray interiored cars

t3black = data[data.interior=='black'][["mmr"]].mean()
t3gray = data[data.interior=='gray'][["mmr"]].mean()

t3perc = (t3black - t3gray) * (100 / t3black)
print(t3perc)


# In[7]:


# task 4 colors of cars sold between 2013 and 2015

t4a = data[data.year.between(2013,2015)] 
t4b = t4a.groupby(by='interior')[["make"]].count()

t4b.sort_values(by="make",ascending=False)


# In[8]:


# task 5 total sale of cars in specified timeframe + %+- during the same time of SUV type

from datetime import date
data["saledate"]=pd.to_datetime(data["saledate"],utc=True)

t5a=data[(data.body=="SUV")&(data.saledate=="Fri Dec 19 2014 09:00:00 GMT-0800")][["body"]]
temp1 = t5a.value_counts()
print(temp1)
print("________________________________________________________________________________________________________")

t5b=data[(data.body=="SUV")&(data.saledate=="Thu Jan 15 2015 04:30:00 GMT-0800 (PST)")][["body"]]
temp2 = t5b.value_counts()
print(temp2)
print("________________________________________________________________________________________________________")

percDiff=(temp1-temp2) * 100 / temp1
print(percDiff)


# In[9]:


# task 6 Adding discount column with values of 10% for for forst and chevrolet and 20% for rest

data.insert(15, "Discounted Price", np.nan)
data.loc[(data.make == 'Ford') | (data.make == 'Chevrolet'),"Discounted Price"] = data.sellingprice * 0.9
data.loc[(data.make != 'Ford') & (data.make != 'Chevrolet'), "Discounted Price"] = data.sellingprice * 0.8

data


# In[10]:


# task 7 dropping two columns and filling in missing values

data=data.drop(["saledate","vin"],axis=1)


data.make=data.make.fillna("Manufacturer")
data


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




