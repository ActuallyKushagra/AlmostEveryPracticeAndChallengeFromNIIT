#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import warnings
import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv('DS1_C5_S3_Mtcars_Data_Practice.csv')
df


# In[5]:


# task 1.1 random sampling without replacement

t3a = df.sample(20, replace = False, random_state = 1, ignore_index = True)
t3a


# In[6]:


# t1.2 with replacement

t3b = df.sample(20, replace = True, random_state = 1, ignore_index = True)
t3b


# In[9]:


# t1.3 systematic sampling with step 5

t3bindex = np.arange(0, len(df), 5)
df.iloc[t3bindex]


# In[16]:


# t1.4 stratified sampling

t34 = df.groupby('vs')
vsgrp = df['vs'].unique()
ndf = pd.DataFrame()

for i in vsgrp:
    data = t34.get_group(i)
    sample = data.sample(20, replace = True, random_state = 1)
    ndf = ndf.append(sample, ignore_index = True)
    
ndf


# In[17]:


# task 1.5 clustered sampling

t35 = df.groupby('vs')
vsgrp2 = [0, 1]
ndf2 = pd.DataFrame()

for i in vsgrp2:
    data2 = t35.get_group(i)
    sample2 = data2.sample(20, replace = True, random_state = 1)
    ndf2 = ndf2.append(sample2, ignore_index = True)
    
ndf2


# In[24]:


# task 2

pop = df['hp']
sam10 = pop.sample(10, replace = True, random_state = 1, ignore_index = True)
sam20 = pop.sample(20, replace = True, random_state = 1, ignore_index = True)
sam30 = pop.sample(30, replace = True, random_state = 1, ignore_index = True)


# In[80]:


# t2.1 mean, median and standard deviation of sample sizes 10, 20 and 30

sam10mean = st.mean(sam10)
sam10med = st.median(sam10)
sam10std = st.stdev(sam10)

sam20mean = st.mean(sam20)
sam20med = st.median(sam20)
sam20std = st.stdev(sam20)

sam30mean = st.mean(sam30)
sam30med = st.median(sam30)
sam30std = st.stdev(sam30)

print(f"""
Mean, Median and standard deviation of sample size 10 are {sam10mean}, {sam10med} and {sam10std} respectively
_____________________________________________________________________________________________________________
Mean, Median and standard deviation of sample size 20 are {sam20mean}, {sam20med} and {sam20std} respectively
_____________________________________________________________________________________________________________
Mean, Median and standard deviation of sample size 30 are {sam30mean}, {sam30med} and {sam30std} respectively""")


# In[81]:


# t2.2 mean, median and standard deviation of entire population data

popmean = st.mean(pop)
popmed = st.median(pop)
popstd = st.stdev(pop)

print(f"""
Mean, Median and standard deviation of entire population data are {popmean}, {popmed} and {popstd} respectively""")


# In[82]:


# t2.3 present the shape of the distribution of population and sample data

plt.figure(figsize = (20, 20))

plt.subplot(3, 2, 1)
sns.histplot(pop, kde = True, color = 'red')
plt.title('Population Data')

plt.subplot(3, 2, 2)
sns.histplot(sam10, kde = True, color = 'green')
plt.title('Sample size 10 Data')

plt.subplot(3, 2, 3)
sns.histplot(sam20, kde = True, color = 'blue')
plt.title('Sample size 20 Data')

plt.subplot(3, 2, 4)
sns.histplot(sam30, kde = True, color = 'pink')
plt.title('Sample size 30 Data')

plt.subplot(3, 2, 5)
sns.boxplot(pop)
plt.title('Population Data')

plt.subplot(3, 2, 6)
sns.boxplot(data = [sam10, sam20, sam30])
plt.xticks([0, 1, 2], ['Sample size 10', 'Sample Size 20', 'Sample Size 30']);


# #### T2.4
# 
# It can be observed that as the sample size grows bigger, it starts to get closer and closer to the population data.
# 
# Larger samples more closely approximate the population
# 
# 
# 
# for comparison
# 
# 
# - sample size 30 against population
# 
#     -- mean, 211.3125 for population and 211.2 for sample size 30
#     
#     -- median, 210 for population and 207.5 for sample size 30
#     
#     -- std, 68.5134493507332 for population and 62.313667067893505 for sample size 30
#     
#     
#     
# - sample size 10 against population
# 
#     -- mean, 180.2 for sample size 10 and 211.3125 for population
#     
#     -- median, 192.5 for sample size 10 and 210 for population
#     
#     -- mode, 44.08275046873651 for sample size 10 and 68.5134493507332 for population
# 
