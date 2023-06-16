#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import scipy.stats as sts
import warnings
import numpy as np
import seaborn as sns
warnings.filterwarnings('ignore')


# # task 1

# p(female) = 0.46
# 
# p(female/parttime) = 0.25
# 
# p(parttime) = 0.174
# 
# p(parttime + female) = (p(female) * p(female/ parttime) )/ p(parttime)
# 
#                      = (0.46 * 0.25) / 0.174
#                      
#                      = 0.66

# # task 2

# p(noise) = 0.70
# 
# p(storage and noise) = 0.56
# 
# p(storage/noise) = p(storage and noise) / p(noise) 
# 
#                  = 0.56 / 0.70
#                 
#                  = 0.8

# In[2]:


# task 3

df = pd.read_csv('DS1_C5_S3_GamesSales_Data_Challenge.csv')
df


# In[4]:


# task 1.1

sample_without_rep = df.sample(30, random_state = 1, replace = False, ignore_index = True)
sample_without_rep


# In[5]:


# task 1.2

sample_with_rep = df.sample(30, random_state = 1, replace = True, ignore_index = True)
sample_with_rep


# In[10]:


# task 1.3

j = np.arange(0, len(df), 5)
sys_sample = df.iloc[j]
sys_sample


# In[12]:


# task 1.4 a

strat_sample = pd.DataFrame()
grp = df.groupby('Year')
grpname = df['Year'].unique()

for i in grpname:
    dat = grp.get_group(i)
    sample = dat.sample(30, replace = True, random_state = 1)
    strat_sample = strat_sample.append(sample, ignore_index = True)
strat_sample


# In[24]:


# task 1.4 b

strat_sample = pd.DataFrame()
grp = df.groupby('Genre')
grpname = df['Genre'].unique()

for i in grpname:
    dat = grp.get_group(i)
    sample = dat.sample(30, replace = True, random_state = 1)
    strat_sample = strat_sample.append(sample, ignore_index = True)
strat_sample


# In[86]:


# 1.5 a) clustered sampling with year

t = df.groupby('Year')
grp2 = [2018, 2019]
ndf2 = pd.DataFrame()

for i in grp2:
    data2 = t.get_group(i)
    sample2 = data2.sample(20, replace = True, random_state = 1)
    ndf2 = ndf2.append(sample2, ignore_index = True)
    
ndf2


# In[87]:


# 1.5 b) clustered sampling with genre

t2 = df.groupby('Genre')
grp2 = ['Action', 'Shooter']
ndf2 = pd.DataFrame()

for i in grp2:
    data2 = t2.get_group(i)
    sample2 = data2.sample(20, replace = True, random_state = 1)
    ndf2 = ndf2.append(sample2, ignore_index = True)
    
ndf2


# In[85]:


# task 2.1 + task 2.2

popdata = df['Global_Sales_M$']
sam10 = popdata.sample(10, replace = True, random_state = 1, ignore_index = True)
sam20 = popdata.sample(20, replace = True, random_state = 1, ignore_index = True)
sam30 = popdata.sample(30, replace = True, random_state = 1, ignore_index = True)
sam40 = popdata.sample(40, replace = True, random_state = 1, ignore_index = True)

popmean = st.mean(popdata)
popmed = st.median(popdata)
popstd = st.stdev(popdata)

sam10mean = st.mean(sam10)
sam10med = st.median(sam10)
sam10std = st.stdev(sam10)

sam20mean = st.mean(sam20)
sam20med = st.median(sam20)
sam20std = st.stdev(sam20)

sam30mean = st.mean(sam30)
sam30med = st.median(sam30)
sam30std = st.stdev(sam30)

sam40mean = st.mean(sam40)
sam40med = st.median(sam40)
sam40std = st.stdev(sam40)


# In[84]:


table = pd.DataFrame({'Population Data': [popmean, popmed, popstd],
                     'Sample Size 10': [sam10mean, sam10med, sam10std],
                     'Sample Size 20': [sam20mean, sam20med, sam20std],
                     'Sample Size 30': [sam30mean, sam30med, sam30std],
                     'Sample Size 40': [sam40mean, sam40med, sam40std]},
                    index = ['Mean', 'Median', 'Standard Deviation'])
table


# In[83]:


# task 2.3

plt.figure(figsize=(20, 30))

plt.subplot(5, 2, 1)
sns.distplot(popdata, kde = True, color = 'purple')
plt.title('Population Data')

plt.subplot(5, 2, 2)
sns.boxplot(popdata, color = 'red')
plt.title('Population Data')

plt.subplot(5, 2, 3)
sns.distplot(sam10, kde = True, color = 'purple')
plt.title('Sample Size 10')

plt.subplot(5, 2, 4)
sns.boxplot(sam10, color = 'red')
plt.title('Sample Size 10')

plt.subplot(5, 2, 5)
sns.distplot(sam20, kde = True, color = 'purple')
plt.title('Sample Size 20')

plt.subplot(5, 2, 6)
sns.boxplot(sam20, color = 'red')
plt.title('Sample Size 20')

plt.subplot(5, 2, 7)
sns.distplot(sam30, kde = True, color = 'purple')
plt.title('Sample Size 30')

plt.subplot(5, 2, 8)
sns.boxplot(sam30, color = 'red')
plt.title('Sample Size 30')

plt.subplot(5, 2, 9)
sns.distplot(sam40, kde = True, color = 'purple')
plt.title('Sample Size 40')

plt.subplot(5, 2, 10)
sns.boxplot(sam40, color = 'red')
plt.title('Sample Size 40');


# #### task 2.4
# 
# It can be observed that as the sample size grows bigger, it starts to get closer and closer to the population data.
# 
# 
# Larger samples more closely approximate the population.
# 
# 
# Comparing the graphs alone for population data and sample data 40, it can be seen that they are closely related, ie, the sample data 40 is almost similar/ same as the population data
