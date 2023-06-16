#!/usr/bin/env python
# coding: utf-8

# In[23]:


import mysql.connector as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import warnings
warnings.filterwarnings('ignore')


# In[11]:


db = sql.connect(host = 'localhost', user = 'root', password = 'Bastards', database = 'hr')


# In[12]:


mycursor = db.cursor()


# In[ ]:





# In[13]:


# task 1 python + SQL query to fetch the names and regions of countries

mycursor.execute("select country_name, region_name from countries join regions on countries.region_id = regions.region_id")
mycursor.fetchall()


# In[14]:


# task 2 part 1 Visualize city and countrywise count  of emplyees without using joins and push the generated dataframe to MySQL

DF1 = pd.read_sql_query("select employee_id, department_id from employees", db)
DF2 = pd.read_sql_query("select department_id, location_id from departments", db)
DF3 = pd.read_sql_query("select location_id, country_id from locations", db)
DF4 = pd.read_sql_query("select country_id, country_name from countries", db)


# In[15]:


# task 2 part 2

DFA = pd.merge(DF1, DF2)
DFA


# In[16]:


# task 2 part 3

DFAB = pd.merge(DFA, DF3)
DFAB


# In[17]:


# task 2 part 4

DFALL = pd.merge(DFAB, DF4)

DFF = DFALL.groupby(by = 'country_name')[['employee_id']].count()
DFF


# In[18]:


# task 2 part 5

hostname = "localhost"
dbname = "hr"
username = 'root'
password = 'Bastards'

engine=create_engine(f"mysql+pymysql://{username}:{password}@{hostname}/{dbname}")

DFF.to_sql("CountryWiseEmpCount" , engine, index = False)


# In[36]:


# task 3 Visual representation of employee count according to city and country

t3 = pd.read_sql_query("select city,location_id from locations", db)
t3a = pd.merge(DFALL, t3)
t3b = t3a.groupby(by='city')[['employee_id']].count().sort_values(by='employee_id',ascending=False)
t3b.plot(kind = 'bar', figsize = (10, 5), ylabel = 'Employee Count', title = 'Employee count by city')
plt.xticks(rotation=45, ha='right');


# In[35]:


t3c = t3a.groupby(by='country_name')[['employee_id']].count().sort_values(by='employee_id',ascending=False)
t3c.plot(kind = 'bar', figsize = (10, 5), ylabel = 'Employee count', title = 'Employee count by country')
plt.xticks(rotation=45, ha='right');


# In[ ]:





# In[ ]:




