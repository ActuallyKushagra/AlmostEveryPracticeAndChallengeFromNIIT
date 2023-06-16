#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[37]:


data = pd.read_csv('DS1_C4_S4_Test_Scores_Data_Practice.csv')


# In[38]:


# task 1 All duplicate values after their first occurance

t1dup = data.loc[:, data.columns!='student_id']
t1dup2 = t1dup[t1dup.duplicated(keep = 'first')]
t1dup2


# In[39]:


# task 2 duplicate rows for school type, teaching method, pretest and posttest score

t2dup = data[data.duplicated(['school_type', 'pretest', 'posttest'], keep = False)]
t2dup


# In[40]:


# task 3 Average pretest scores of all schools

t3 = data.groupby(by = ['school'])[['pretest']].mean()
t3


# In[41]:


# task 4 max and min males and females in each school setting


pd.crosstab(data.school_setting, [data.gender], values = data.student_id, aggfunc=['count'])


# In[42]:


# task 5 min and max postest scores of all schools

t5 = pd.pivot_table(data, index = ['school'], values = ['posttest'], aggfunc = ['min', 'max'])
t5


# In[43]:


# task 5 part 2 top 5 schools in accordance to part 1

t5.head()


# In[44]:


# task 6 part 1 sum and average of school wise pretest scores

t6 = pd.pivot_table(data ,index = ['school'], values = ['pretest'], aggfunc = ['mean','sum'])
t6


# In[45]:


# task 6 part 2 top 5 in accordance to task 6

t6.sort_values(('mean', 'pretest'), ascending = False).head()


# In[46]:


# task 7 Assigning scholarships to FBUMG school students with 5LQ class type

t7 = data[(data.school == "FBUMG") & (data.classroom == "5LQ")]
t7.insert(9, "Scholarship", np.nan)
t7.loc[:,"Scholarship"] = t7.posttest * 100
t7


# In[47]:


# task 8 Replace the values with Yes and NO

t8 = data.replace(['Does not qualify', 'Qualifies for reduced/free lunch'], ['No','Yes'])
t8


# In[48]:


# task 9 Count of different teaching methods by location

t9 = pd.crosstab(data.school_setting, data.teaching_method)  # by default cross table gives output count
t9


# In[49]:


# task 10 replacing pretest scores of students with 135 where it's 39.

t10 = data[(data.gender=="Male") & (data.posttest<39)]
t10.iloc[0:,8] = 135
t10


# In[50]:


# task 11 Average posttest score for urban and suburban male students with relative percentage
 
t11 = data[(data.school_setting == 'Urban') & (data.gender == 'Male') | (data.school_setting == 'Suburban') & (data.gender == 'Male')]
t11a = t11.groupby(by=['school_setting', 'gender'])[['posttest']].mean()
percDiff = (75.942529 - 62.421171) * 100 / 75.942529         # values taken from output of t11
print(percDiff)
t11a


# In[51]:


# task 12 part 1 find total missing values and replace them with appropriate values

data.isnull().sum()


# In[52]:


# task 12 part 2

data.gender.value_counts()


# In[53]:


# task 12 part 3

data.gender = data.gender.fillna('Male')
t12a = data.pretest.mean()  
t12b = data.posttest.mean()
print(t12a, 'Is pretest average')
print(t12b, 'Is posttest average')

data.pretest = data.pretest.fillna(t12a)
data.posttest = data.posttest.fillna(t12b)

data.isnull().sum()

