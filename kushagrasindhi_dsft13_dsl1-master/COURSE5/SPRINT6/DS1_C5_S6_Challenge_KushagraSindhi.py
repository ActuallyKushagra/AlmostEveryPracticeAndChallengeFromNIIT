#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import statistics as st
import scipy.stats as sts


# In[4]:


# task 1

t1mean = 4.30
t1std = 0.574

alpha = 0.1

sampdat = [3, 4, 5, 5, 4, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 3, 3, 3, 4, 3, 5, 4, 4, 5, 4, 4, 4, 5]
sampmean = st.mean(sampdat)
sampstd = st.stdev(sampdat)
sampvar2 = sampstd**(0.5)
sampsize = len(sampdat)
print(f'Sample mean = {sampmean} and sample standard deviaion = {sampstd} and \n sample variance = {sampvar2} and sample size = {sampsize}')


# ##### a)
# 
# Ho: mean > 4.3
# 
# Ha: mean < 4.3
# 
# Since a lesser value is in the test, we will use left tailed test

# In[5]:


# b)


crval = sts.norm.ppf(1 - alpha)
print(f'The zcritical value is {crval}')


# In[6]:


# c) and d)

zstat = (sampmean - t1mean) / (t1std / st.sqrt(sampsize))
print('The value of z-statistics is',zstat)

pval = sts.norm.sf(abs(zstat))
print(f'The value of p-value is {pval}')


# ##### e)
# 
# As per, decision rule:
# 
# i. If p-value < alpha : Rejection of Null Hypothesis(H0)
# 
# ii. If -z-critical > z-statistics > +z-critical : Rejection of Null Hypothesis(H0)
# 
# In our analysis, p_value < alpha and -z-critical < z-statistics < +z-critical, hence, The alternate hypothesis is accepted

# In[7]:


# task 2

df = pd.read_csv('DS1_C5_S6_CityPrice_Data_Challenge.csv')
df


# ###### a)
# 
# Ho: mean1 = mean2
# 
# Ha: mean1 != mean2

# In[8]:


# b c and d

alpha = 0.01
calimean = df['California'].dropna().mean()
florimean = df['Florida'].dropna().mean()
calisize = len(df['California'].dropna())
florisize = len(df['Florida'].dropna())
calivar = df['California'].dropna().var()
florivar = df['Florida'].dropna().var()

zcrit = sts.norm.ppf(1 - alpha/2)
zstat = ((calimean - florimean) - 0) / (st.sqrt(calivar/calisize + florivar/florisize))
pval = sts.norm.sf(abs(zstat))*2

print(f'The zcritical value is {zcrit} \n The zstat value is {zstat} \n The pval is {pval}')


# In[9]:


# e)

if pval < alpha and zstat > zcrit:
    print('Null hypothesis rejected')
else:
    print('Null hypothesis accepted')


# ###### task 3
# 
# a)
# 
# Ho: mean = 44
# 
# Ha: mean != 44
# 
# Since the question is of equals and not-equals of two values, we we use two tailed test

# In[11]:


# b, c, d


alpha = 0.05

popmean = 44
sampmean = 45.1

popstd = 8.7

n = 68


zstat = (sampmean - popmean) / (popstd/ st.sqrt(n))
zcrit = sts.norm.ppf(1 - alpha/2)
pval = sts.norm.sf(abs(zstat))*2
print(f"""zstat is {zstat}
zcrit is {zcrit}
pval is {pval}""")


# In[12]:


# e)

if pval < alpha and zstat > zcrit:
    print('Null hypothesis rejected')
else:
    print('Null hypothesis accepted')

