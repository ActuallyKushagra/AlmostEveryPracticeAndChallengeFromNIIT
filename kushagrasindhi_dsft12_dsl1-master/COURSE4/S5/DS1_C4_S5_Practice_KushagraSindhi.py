#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
import matplotlib as mlt
import matplotlib.pyplot as plt


# In[11]:


data = pd.read_excel('DS1_C4_S5_Employee_Data_Practice.xlsx')
data


# In[12]:


# task 1 Cost incurred to the company by each department

t1 = data.groupby(by = 'Department')[['Annual Salary ($)']].sum()
t1


# In[13]:


# task 1 part 2 

t1.plot.bar(title = ' Department-Wise Annual Expenditure')
plt.xticks(rotation = 45, ha = 'right');

# this graph suggests that the IT department has the highest annual salary and finance has the lowest


# In[14]:


# task 2 Department wise total number of males and females

t2 = data.groupby(by = ['Department', 'Gender'])[['Gender']].count()
t2


# In[16]:


# task 3 Salary possibly offered to new recruits with 0 experience

t3 = data[(data.Department == 'IT ') & (data.Work_Experience == 0)][['Annual Salary ($)']]
print(t3.mean())
t3


# In[17]:


# task 4 Departent wise cost to the company using pie chart

t4 = data.groupby(by = ['Department'])[['Annual Salary ($)']].sum()
t4.plot.pie(y = 'Annual Salary ($)', title = 'Department Expenditure Proportion', autopct = '%0.2f%%');

# this graph suggests that the IT department has the highest annual salary share of 30.92% followed by sales at 26.25%, 
# HR at 23.79% and Finance has the lowest share at 19.04%


# In[18]:


# task 5 Age group with the highest number of employees

plt.hist(data['Age'], edgecolor = 'black');

# age group 25 to 30 has the highest number of employees


# In[19]:


# task 6 Trend of salary and experience.

plt.scatter(data['Work_Experience'], data['Annual Salary ($)']);

# this upward trend suggests that the salary of an employee increases has it gains more experience


# In[23]:


# task 7 Department wise spread of annual salary

IT = data[data.Department == 'IT '][['Annual Salary ($)']]
Finance = data[data.Department == 'Finance'][['Annual Salary ($)']]
HR = data[data.Department == 'HR'][['Annual Salary ($)']]
sales = data[data.Department == 'Sales'][['Annual Salary ($)']]

data.plot.box(by='Department', column = 'Annual Salary ($)', title = 'Spread of Annual Salaries by departments');

# this graph suggests that the IT department has the highest salary spread followed by the HR department


# In[ ]:




