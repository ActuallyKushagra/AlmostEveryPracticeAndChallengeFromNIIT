#!/usr/bin/env python
# coding: utf-8

# In[93]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics as st
import seaborn as sns
import scipy.stats as sts
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[37]:


# task 1

t1mean = 70
t1std = 11.35


# In[38]:


# 1.1 bill between 80 and 55

t1x1 = 80
t1x2 = 55
zscoreOne = (t1x1 - t1mean) / t1std
zscoreTwo = (t1x2 - t1mean) / t1std

pval80 = norm.cdf(zscoreOne)
pval55 = norm.cdf(zscoreTwo)

t1p = pval80 - pval55
print("Probability of a randomly selected monthly bill between 80 and 55 is", t1p)


# In[39]:


# t1.2 not greater than 40

t1x3 = 40
zscoreThree = (t1x3 - t1mean) / t1std
pval40 = norm.cdf(zscoreThree)

print('Probability of a randomly selected monthly bill being not greater than 40 is', pval40)


# In[40]:


# task 2
# a)

df = pd.read_csv('DS1_C5_S5_SmartCarRiding_Data_Practice.csv')
df


# In[69]:


# b)

q1 = df['fare_amount'].quantile(0.25)
q3 = df['fare_amount'].quantile(0.75)
std = df['fare_amount'].std()
iqr = q3-q1
uf = q3+1.5*iqr
lf = q1-1.5*iqr
mean = df['fare_amount'].mean()
median = df['fare_amount'].median()
mode = df['fare_amount'].mode()[0]
skew = sts.skew(df['fare_amount'])
kurt = sts.kurtosis(df['fare_amount'])
var = df['fare_amount'].var()

detdf = pd.DataFrame([mean, median, mode,std, var, q1, q3, iqr, uf, lf, skew, kurt], index = ['Mean', 'Median','Mode','Standard Deviation', 'Var', 'Q1', 'Q3', 'IQR', 'Upperfence', 'Lowerfence', 'Skewness', 'Kurtosis'])
detdf = detdf.T
detdf.insert(0, '', 'Fare Amount')
df.loc[df["fare_amount"] < lf, "fare_amount"] = mean
df.loc[df["fare_amount"] > uf, "fare_amount"] = mean
detdf


# In[ ]:





# In[49]:


plt.figure(figsize = (15, 8))
sns.histplot(df['fare_amount'], kde = True)
plt.title('Population Data for fare amount')
plt.xlabel('Count')
plt.ylabel('Fare amount');


# In[50]:


# c)

num = [10, 30, 1000, 5000, 10000, 50000, 100000, 150000]
data_s = []
data_smean = []
sample_df = pd.DataFrame()
k = 0



for i in num:
    sample_df = df.sample(i, replace = True, ignore_index = True, random_state = 1)
    data_s.append(sample_df['fare_amount'].tolist())
    data_smean.append(sample_df['fare_amount'].mean())
    
    
fig, ax = plt.subplots(2, 4, figsize = (15, 8))

for i in range(0, 2): # row
    for j in range(0, 4): # column
       # ax[i, j].hist(data_s[k], bins = 5, density = True)
        sns.histplot(data_s[k], ax = ax[i,j], kde = True)
        ax[i, j].set_title(label = 'sample size ' + str(len(data_s[k])))
        k+=1


# In[81]:


# d)

sam1 = pd.DataFrame()

for i in range(0, 20):
    sample_20 = pd.DataFrame(df[['fare_amount']].sample(400, replace = True, ignore_index = True))
    sam1.insert(i, 'Sample_' + str(i), sample_20)
    
sam1


# In[82]:


samname = sam1.columns
fig, ax = plt.subplots(5, 4, figsize = (18, 18))
k = 0

for i in range(0, 5):
    for j in range(0, 4):
        ax[i, j].hist(sam1[samname[k]], bins =  5, density = True, edgecolor = 'black')
        ax[i, j].set_title(label = 'Sample size' + samname[k])
        k+=1


# In[83]:


sameans = []

for i in samname:
    sameans.append(sam1[i].mean())
    
sameansdf = pd.DataFrame({'Sample names': samname, 'Sample means': sameans})
sameansdf


# In[107]:


finsammean = sameansdf['Sample means'].mean()
finsammed =  sameansdf['Sample means'].median()
finsammode =  sameansdf['Sample means'].mode()[0]
finsamstd =  st.stdev(sameansdf['Sample means'])
finsamvar =  sameansdf['Sample means'].var()
finsamrange =  sameansdf['Sample means'].max() -  sameansdf['Sample means'].min()
finsamq1 =  sameansdf['Sample means'].quantile(0.25)
finsamq3 =  sameansdf['Sample means'].quantile(0.75)
finsamiqr = finsamq3 - finsamq1
finsamlf = finsamq1 - 1.5 * finsamiqr
finsamuf = finsamq3 + 1.5 * finsamiqr
finsamskew = sts.skew( sameansdf['Sample means'])
finsamkurt = sts.kurtosis( sameansdf['Sample means'])


#detdf = pd.DataFrame([mean, median, mode, var, q1, q3, iqr, uf, lf, skew, kurt], index = ['Mean', 'Median','Mode', 'Var', 'Q1', 'Q3', 'IQR', 'Upperfence', 'Lowerfence', 'Skewness', 'Kurtosis'])
sammm = pd.DataFrame([finsammean, finsammed, finsammode, finsamstd, finsamvar, finsamq1, finsamq3, finsamiqr, finsamuf, finsamlf, finsamskew, finsamkurt], index = ['Mean', 'Median','Mode', 'Standard Deviation', 'Var', 'Q1', 'Q3', 'IQR', 'Upperfence', 'Lowerfence', 'Skewness', 'Kurtosis'])
sammm = sammm.T
sammm.insert(0, '', 'Sampled Data')
finaldf = sammm.append(detdf)
print('Sample std = ', st.stdev(df.fare_amount)/np.sqrt(400))
finaldf


# We can see that the mean of population data and mean of 20 samples (n=200) is very close.
# We can also see that the standard deviation of population and sampled data is also very close, hence, we can say that the samples follow central limit theorem
