#!/usr/bin/env python
# coding: utf-8

# In[88]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[14]:


df = pd.read_excel('DS1_C4_S5_Car_Data_Challenge.xlsx')
df


# In[15]:


# column names
l = []
for i in df:
    l.append(i)
l = sorted(l)
print(*l, sep = '\n')


# In[53]:


# task 1

t1 = df.loc[:,['Make','Displacement','Fuel_Tank_Capacity_litre','City_Mileage_km_litre','Highway_Mileage_km_litre','Minimum_Turning_Radius']].dropna()
t1


# In[131]:


# groupby make with mean, median, std

t1a = t1.groupby(by='Make').agg({'Displacement':{'mean','median','std'},'Fuel_Tank_Capacity_litre':{'mean','median','std'},'City_Mileage_km_litre':{'mean','median','std'},'Minimum_Turning_Radius':{'mean','median','std'}})
t1a


# In[130]:


Suzuki=t1[t1['Make']=='Suzuki'][['Displacement']]
Toyota=t1[t1['Make']=='Toyota'][['Displacement']]
Mahindra=t1[t1['Make']=='Mahindra'][['Displacement']]

plt.figure(figsize = (14, 10))

plt.subplot(2, 2, 1)
plt.hist(Suzuki, edgecolor = 'black')
plt.title('Suzuki')

plt.subplot(2, 2, 2)
plt.hist(Toyota, edgecolor = 'black')
plt.title('Toyota')

plt.subplot(2, 2, 3)
plt.hist(Mahindra, edgecolor = 'black')
plt.title('Mahindra')

plt.subplot(2, 2, 4)
plt.boxplot([Suzuki['Displacement'],Toyota['Displacement'],Mahindra['Displacement']])
plt.title('Spread of data for Suzuki, Toyota and Mahindra')
plt.xticks([1, 2, 3], ['Suzuki', 'Toyota', 'Mahindra']);


# ## Conclusion:
#         - Mean, median and std is determined for each manufacturer's each model
#         - Data of suzuki is left skewed, Toyota is right skewed and Mahindra is left skewed

# In[ ]:





# In[85]:


# task 2

t2 = t1.copy()
t2.insert((len(t2.columns)), 'AverageMileage', np.nan)
t2['AverageMileage'] = (t2['City_Mileage_km_litre'] + t2['Highway_Mileage_km_litre']) / 2
t2


# In[110]:


sns.heatmap(t2.drop('Make', axis = 1));


# In[132]:


plt.figure(figsize=(20, 15))

plt.subplot(2, 2, 1)
plt.scatter(t2['AverageMileage'], t2['Displacement'], color = 'green')
plt.title('Relation of Average Mileage and Displacement', fontdict = {'fontsize' : 20})

plt.subplot(2, 2, 2)
plt.scatter(t2['AverageMileage'], t2['Fuel_Tank_Capacity_litre'],  color = 'orange')
plt.title('Relation of Average Mileage and Fuel tank capacity (Litre)', fontdict = {'fontsize' : 20})

plt.subplot(2, 2, 3)
plt.scatter(t2['AverageMileage'], t2['Minimum_Turning_Radius'])
plt.title('Relation of Average Mileage and Minimum turning radius (mm)', fontdict = {'fontsize' : 20})

plt.subplot(2, 2, 4)
plt.scatter(t2['AverageMileage'], t2['Make'])
plt.title('Relation of Average Mileage and Make', fontdict = {'fontsize' : 20});


# In[135]:


print(f"""
Correlation coefficient of:
        Average mileage and displacement       = {t2['AverageMileage'].corr(t2['Displacement'])}
        Average mileage and Fuel tank capacity = {t2['AverageMileage'].corr(t2['Fuel_Tank_Capacity_litre'])}
        Average mileage and Fuel tank capacity = {t2['AverageMileage'].corr(t2['Minimum_Turning_Radius'])}""")


# ## Conclusion:
#            -  * Average mileage and displacement       = -0.689474497116413
#               * Average mileage and Fuel tank capacity = -0.7145034450182565
#               * Average mileage and Fuel tank capacity = -0.35620940763419057
