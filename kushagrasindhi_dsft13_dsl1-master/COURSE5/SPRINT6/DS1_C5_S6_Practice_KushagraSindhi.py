#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import statistics as st
import math
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts


# In[1]:


# task 1


alpha = 0.05
t1popmean = 33.88
t1sammean = 32.18
t1samsize = 49
t1popstd = 1.28
t1popvar = t1popstd**2


# #### a)
# 
# Ha: μ >= 33.38 
# 
# Ha: μ < 33.38
# 
# According to the information provided in the question, A two-tailed test is best suited for this but since the size of population is unknown, a left tailed test will be used.

# In[3]:


# b)

zcrit1 = norm.ppf(1 - alpha)

print('The z-critical value is ', zcrit1)


# In[5]:


# c) and d)

z_statistic = (t1sammean-t1popmean) / (t1popstd/np.sqrt(t1samsize)) 
print("The Z statistics is ", z_statistic)

p_value = norm.sf(abs(z_statistic))
print("The p_value is ", p_value)

z_critical = norm.ppf(1-alpha)
print("The z-critical value is ", z_critical)


# ##### e)
# 
# As per, decision rule:
# 
# i. If p-value < alpha : Rejection of Null Hypothesis(H0)
# 
# ii. If -z-critical > z-statistics > +z-critical : Rejection of Null Hypothesis(H0)
# 
# In our analysis, p_value > alpha and -z-critical > z-statistics > +z-critical, hence, the null hypothesis is accepted

# In[6]:


lowr = t1popmean - 4 * t1popstd
uppr = t1popmean + 4 * t1popstd
normp = np.arange(lowr, uppr)
plt.plot(normp, sts.norm.pdf(normp, t1popmean, t1popstd))


# In[7]:


# task 2

alpha = 0.05

t2mean1 = 85
t2std = 2.1


t2mean2 = 87.5
t2n2 = 32


# #### a)
# 
# Ho: μ = 85
# 
# Ha: μ > 85
# 
# According to the information provided in the question, a One-tailed test, ie, a right-tailed test is best suited.

# In[8]:


# b)

zcrit2 = norm.ppf(1-alpha)
print('The z-critical value is', zcrit2)


# In[41]:


# c) and d)

zstat2 = (t2mean2 - t2mean1) / (t2std / math.sqrt(t2n2))
pval2 = norm.sf(abs(zstat2))
print(f'The value pf z-statistics is {zstat2} and probability value is {pval2}')


# In[45]:


print(f"""
The value of alpha is {alpha}
The mean is {t2mean}
The Standard Deviation is {t2std}
The Null hypothesis is {t2mean}
The Alternate hypothesis is {t2mean2}
The Sample Size is {t2n2}
The Z-statistic value is {zstat2}
The Z-critical value is {zcrit2}
The P-Value is {pval2}""")


# In[27]:


# e)

lower = t2mean1 - 4 * t2std
upper = t2mean1 + 4 * t2std
norm_p = np.arange(lower, upper)
plt.plot(norm_p, sts.norm.pdf(norm_p, t2mean1, t2std))


# As per, decision rule:
# 
# i. If p-value < alpha : Rejection of Null Hypothesis(H0)
# 
# ii. If -z-critical > z-statistics > +z-critical : Rejection of Null Hypothesis(H0)
#     
# In out analysis, we can observe that pval > alpha and -zcritical < zstatistic > +zcritical, hence, alternate hypothesis is accepted

# In[ ]:




