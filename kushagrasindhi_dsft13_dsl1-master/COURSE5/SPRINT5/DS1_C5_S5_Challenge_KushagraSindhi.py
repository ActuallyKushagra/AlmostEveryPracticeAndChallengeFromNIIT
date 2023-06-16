#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sts
import warnings
from scipy.stats import norm
warnings.filterwarnings('ignore')


# In[2]:


# task 1

t1mean= 1332
t1std = 725


# In[3]:


# a

t1x = 2000

zscore1= (t1x-t1mean)/t1std
pval2000 = 1 - norm.cdf(zscore1)
pval2000


# In[4]:


# b

t1x2 = 0

zscore2 = (t1x2 - t1mean) / t1std
pval0 = 1 - norm.cdf(zscore2)
pval0


# In[5]:


# c

t1x3 = 100
t1x4  = 700

zscore3 = (t1x3 - t1mean) / t1std
zscore4 = (t1x4 - t1mean) / t1std

pvalx3 = norm.cdf(zscore3)
pvalx4 = norm.cdf(zscore4)

pvalc = pvalx4 - pvalx3
pvalc


# In[8]:


#d

lower = t1mean - 4*t1std
upper = t1mean + 4*t1std

d = np.arange(lower,upper)

plt.plot(d, norm.pdf(d,t1mean,t1std))


# In[10]:


# task 2

df = pd.read_csv('DS1_C5_S5_Computers_Data_Challenge.csv')
df


# In[11]:


df2 = df[df['price'] < 4000]
df2


# In[12]:


# a)

sampledf = df2.sample(50, replace = True, random_state = 1, ignore_index = True)
sampledf


# In[16]:


# b)

popmean = df2['price'].mean()
popstd = df2['price'].std()
popmed = df2['price'].median()
popmode = df2['price'].mode()[0]
poprange = df2['price'].max() - df2['price'].min()
popq1 = df2['price'].quantile(0.25)
popq3 = df2['price'].quantile(0.75)
popiqr = popq3 - popq1
popskew = sts.skew(df2['price'], bias = False)
popkurt = sts.kurtosis(df2['price'], bias = False)
popvar = popstd**(0.5)

sampmean = sampledf['price'].mean()
sampstd = sampledf['price'].std()
sampmed = sampledf['price'].median()
sampmode = sampledf['price'].mode()[0]
samprange = sampledf['price'].max() - sampledf['price'].min()
sampq1 = sampledf['price'].quantile(0.25)
sampq3 = sampledf['price'].quantile(0.75)
sampiqr = sampq3 - sampq1
sampskew = sts.skew(sampledf['price'])
sampkurt = sts.kurtosis(sampledf['price'])
sampvar = sampstd**(0.5)

comptab = pd.DataFrame({'Population': [popmean, popmed, popmode, popstd, popvar, poprange, popq1, popq3, popiqr, popskew, popkurt],
                       'Sample Size 50': [sampmean, sampmed, sampmode, sampstd, sampvar, samprange, sampq1, sampq3, sampiqr, sampskew, sampkurt]},
                      index = ['Mean', 'Median', 'Mode', 'STD', 'Var', 'Range', 'Q1', 'Q3', 'IQR', 'Skewness', 'Kurtosis'])

comptab


# In[24]:


# c) and d)

poplower = popmean - 4*popstd
popupper = popmean + 4*popstd
c = np.arange(poplower,popupper)

samplower = sampmean - 4 * sampstd
sampupper = sampmean + 4 * sampstd
cc = np.arange(poplower,popupper)


plt.plot(c, norm.pdf(c,popmean,popstd), color = 'blue', label = 'Population data')
plt.plot(cc, norm.pdf(cc,sampmean,sampstd), color = 'red',  label = 'Sample data')

plt.legend();


# The central limit theorem states that if you have a population with mean and standard deviation and take sufficiently large random samples from the population, then the distribution of the sample means will be approximately normally distributed.
# 
# Since, the standard deviation of population and sample data is similar, we can say that the sample follows the central limit theorem.

# In[33]:


# e) and f)

#

zscor1 = []
for i in c:
    zsc1 = (i-popmean)/popstd
    zscor1.append(zsc1)

for i in zscor1:
    print(f'Pval for {i} is {norm.pdf(i)}')


# In[37]:


# g)

plt.plot(zscor1, norm.pdf(zscor1,st.mean(zscor1),st.stdev(zscor1)));


# In[38]:


# h)

x = 2700

zcorrr = (x-popmean ) / popstd
p1 = 1-norm.cdf(zcorrr)
print(p1, f'is the pvalue of {x}')


# In[39]:


# i)

x1 = 1301

zco = (x1 - popmean) / popstd
p2 = norm.cdf(zco)
print(p2, f'is the pval of {x1}')


# In[41]:


# j)

xx1 = 2000
xx2 = 2900

zs1 =( xx1 - popmean) / popstd
zs2 = (xx2 - popmean) / popstd

p1 = norm.cdf(zs1)
p2 = norm.cdf(zs2)

print('pval of value lying between 2000 and 2900 is', p2-p1)

