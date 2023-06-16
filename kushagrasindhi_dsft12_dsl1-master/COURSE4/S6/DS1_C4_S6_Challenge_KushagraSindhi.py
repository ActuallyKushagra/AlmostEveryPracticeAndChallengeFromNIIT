#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector as sql
from sqlalchemy import create_engine


# In[4]:


data = pd.read_csv('housing1.csv')
data


# In[9]:


# task 1 area > 6000 and corner 

t1 = data[(data.LotArea >= 6000) & (data.LotConfig=='Corner')][['Id','SalePrice','LotArea','LotConfig']]
t1


# In[12]:


# task 2 1 family and 1 storey

t2 = data[(data.BldgType=='1Fam')&(data.HouseStyle=='1Story')&(data.LandContour=='Lvl')][['Id','SalePrice', 'LotArea', 'LotConfig']]
t2


# In[14]:


# task 3 townhouses

t3 = data[(data.BldgType=='TwnhsE')|(data.BldgType=='Twnhs')][['Id','SalePrice','LotArea','BldgType', 'MSZoning']]
t3


# In[18]:


# task 4 bedrooms > 3, basement and cememt exterior a must-have

t4 = data[(data.BedroomAbvGr>=3)&(data.BsmtQual!='NA') & ((data.Exterior1st=='CemntBd')|(data.Exterior2nd=='CemntBd'))][['Id','SalePrice','MSZoning','BsmtQual','LotArea']]
t4


# In[19]:


# task 5 car space >= 2 and area >= 500

t5 = data[(data.GarageCars>=2)&(data.GarageArea>=500)][['Id','SalePrice','GarageCars','GarageArea', 'LotArea']]
t5


# In[21]:


# push to MySQL

hostname = "localhost"
dbname = "c4s6"
username = 'root'
password = 'Bastards'

engine=create_engine(f"mysql+pymysql://{username}:{password}@{hostname}/{dbname}")

t1.to_sql("t1",engine,index=False)
t2.to_sql("t2",engine,index=False)
t3.to_sql("t3",engine,index=False)
t4.to_sql("t4",engine,index=False)
t5.to_sql("t5",engine,index=False)


# In[ ]:





# In[ ]:




