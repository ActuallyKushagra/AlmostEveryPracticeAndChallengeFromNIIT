#!/usr/bin/env python
# coding: utf-8

# In[51]:


import numpy as np
import pandas as pd
import warnings
import matplotlib as mlt
import matplotlib.pyplot as plt
from importlib import reload
warnings.filterwarnings('ignore')


# In[70]:


data = pd.read_excel('DS1_C4_S5_Car_Data_Challenge.xlsx')
data


# In[71]:


# task 1 Manufacturer wise Max city mileage and it's bar graph

t1 = pd.pivot_table(data, index=['Make'], values=['City_Mileage_km_litre'], aggfunc=['max'])
t1


# In[72]:


# task 1 part 2

t1a = t1.reindex(t1['max'].sort_values(by = 'City_Mileage_km_litre', ascending = False).index)
t1a.plot.bar(title = 'City Wise Mileage of Manufacturers', xlabel = 'Manufactures', ylabel = 'Mileage', figsize = (15, 5))
plt.xticks(rotation=45, ha='right');


# In[73]:


# task 2 Next top 10 makers with highest mileage

t2 = pd.pivot_table(data, index = ['Make'], values = ['City_Mileage_km_litre'], aggfunc = ['max'])
t2b = t2.reindex(t2['max'].sort_values(by = 'City_Mileage_km_litre').index)
t2c = t2b.iloc[10:20,0:]
t2c.plot.bar(title = 'City Mileage according to manufactures', xlabel = 'Manufactures', ylabel = 'Mileage', figsize = (15, 5))
plt.xticks(rotation=45, ha='right');


# In[74]:


# task 3 part 1 Count of cars by body type and it's pie chart representing the market share

t3 = data.groupby(by='Body_Type')[['Body_Type']].count()
t3.columns=['Body Type']
t3b = t3.sort_values(by='Body Type',ascending=False).head(10)
t3b


# In[75]:


# task 3 part 2

plt.pie(t3b['Body Type'],labels=t3b.index, autopct='%.2f%%',shadow=True, explode=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1], radius = 2)
plt.legend();


# In[76]:


# task 4 part 1 Comparing mileage of cars from hyundai, mahindra, renault and skoda using bar graph

data['Highway_Mileage_km_litre']=data['Highway_Mileage_km_litre'].fillna(data['Highway_Mileage_km_litre'].mean())
data['Highway_Mileage_km_litre'].isnull().sum()


# In[77]:


t4=data[((data.Make=='Hyundai')|(data.Make=='Mahindra')|(data.Make=='Renault')|(data.Make=='Skoda'))][['Make','City_Mileage_km_litre','Highway_Mileage_km_litre']]
t4mean = pd.pivot_table(t4,index=['Make'],values=['City_Mileage_km_litre','Highway_Mileage_km_litre'],aggfunc=['mean'])
t4med=pd.pivot_table(t4,index=['Make'],values=['City_Mileage_km_litre','Highway_Mileage_km_litre'],aggfunc=['median'])
t4b = pd.concat([t4mean, t4med], axis=1)
t4b


# In[78]:


# task 4 part 2

t4b.plot.bar(xlabel = 'Manifactures', ylabel = 'Mileage', title = 'Mean & Median of City and Highway Mileage', figsize = (20, 5));
plt.xticks(rotation=45, ha='right');


# In[79]:


# task 5 part 1 Comparing mileage of cars from hyundai, mahindra, Volkswagen and Toyota using bar graph

t5=data[((data.Make=='Hyundai')|(data.Make=='Mahindra')|(data.Make=='Volkswagen')|(data.Make=='Toyota'))][['Make','City_Mileage_km_litre','Highway_Mileage_km_litre']]
t5mean = pd.pivot_table(t5,index=['Make'],values=['City_Mileage_km_litre','Highway_Mileage_km_litre'],aggfunc=['mean'])
t5med=pd.pivot_table(t5,index=['Make'],values=['City_Mileage_km_litre','Highway_Mileage_km_litre'],aggfunc=['median'])
t5b = pd.concat([t5mean, t5med], axis=1)
t5b


# In[80]:


# task 5 part 2

t5b.plot.bar(stacked=True, ylabel = 'Mileage', xlabel = 'Manufacturer', figsize = (10, 5));
plt.xticks(rotation=45, ha='right');


# In[81]:


# task 6 Comparing fuel economy of different cars with bar graph

data['City_Mileage_km_litre']=data['City_Mileage_km_litre'].fillna(data['City_Mileage_km_litre'].mean())
t6 = pd.pivot_table(data,index=['Make'],values=['City_Mileage_km_litre','Highway_Mileage_km_litre'],aggfunc=['mean'])
t6mean = t6.reindex(t6['mean'].sort_values(by='City_Mileage_km_litre',ascending=False).index)
t6mean


# In[82]:


# task 6 part 2

t6mean.plot.bar(figsize = (20, 10), xlabel = 'Manufacturer', ylabel = 'Mileage')
plt.xticks(rotation=45, ha='right');


# In[83]:


# task 7 Scatterplot for the fuel tank capacity and displacement

data['Displacement'] = data['Displacement'].fillna(data['Displacement'].mean())
data['Fuel_Tank_Capacity_litre'] = data['Fuel_Tank_Capacity_litre'].fillna(data['Fuel_Tank_Capacity_litre'].mean())
t7 = data.groupby(by = ['Make'])[['Displacement','Fuel_Tank_Capacity_litre']].mean().sort_values('Fuel_Tank_Capacity_litre',ascending=False).head(10)
t7


# In[84]:


# task 7 part 2

plt.figure(figsize=(10, 5))
plt.scatter(t7['Displacement'], t7['Fuel_Tank_Capacity_litre']); #, figsize = (10, 5)) *x/y labels not working*


# In[85]:


# task 8 fuel tank capacity and average mileage

data.insert(20, 'Average_Mileage', np.nan)
Average_Mileage = (data.City_Mileage_km_litre + data.Highway_Mileage_km_litre)/ 2
data['Average_Mileage'] = Average_Mileage
t8 = pd.pivot_table(data, index = ['Average_Mileage'], values = ['Fuel_Tank_Capacity_litre'], aggfunc=['mean'])
t8b = t8.reindex(t8['mean'].sort_values(by='Fuel_Tank_Capacity_litre',ascending=False).index)
t8b


# In[ ]:





# In[86]:


# task 8 part 2

plt.scatter(t8b.index, t8b.values)


# In[18]:


# task 9 Bar garph for manufacturers of safe cars and their mileage

data['Central_Locking'] = data['Central_Locking'].fillna('Yes')
data['Child_Safety_Locks'] = data['Child_Safety_Locks'].fillna('Yes')
data['Hill_Assist'] = data['Hill_Assist'].fillna('No')        
data['High_Speed_Alert_System'] = data['High_Speed_Alert_System'].fillna('No')   
data['Passenger_Side_Seat-Belt_Reminder'] = data['Passenger_Side_Seat-Belt_Reminder'].fillna('No')
t9 = data[((data.Central_Locking=='Yes')&(data.Child_Safety_Locks=='Yes')&(data.Hill_Assist=='Yes')&(data.High_Speed_Alert_System=='Yes')&(data['Passenger_Side_Seat-Belt_Reminder']=='Yes'))][['Make','Average_Mileage']]
t9b = t9.sort_values(by='Average_Mileage',ascending=False).head(10)
t9b


# In[19]:


# task 9 part 2

t9b.plot.bar(x = 'Make', ylabel = 'Mileage', figsize = (10, 5))
plt.xticks(rotation=45, ha='right');


# In[20]:


# task 10 Cars with Normal, Comfort, Eco, Sport, Power driving modes

data['Drive_Modes'] = data['Drive_Modes'].fillna('Normal')
t10 = data[(data.Drive_Modes == 'Normal, Comfort, Eco, Sport, Power Mode')]
t10


# In[87]:


# task 11 Histograms representing spread of fuel economy for Hyundai, Suzuki, TATA and BMW

t11a=data[data.Make=='Hyundai'][['Make','Model','Average_Mileage']]
t11a


# In[88]:


# task 11 part 2

plt=reload(plt)
plt.hist(t11a.Average_Mileage, range = [10, 25], edgecolor = 'black')
plt.title('Hyundai'); # giving error


# In[89]:


# task 11 part 3

t11b = data[data.Make=='Maruti Suzuki'][['Make','Model','Average_Mileage']]
t11b


# In[90]:


# task 11 part 4 

plt=reload(plt)
plt.hist(t11b.Average_Mileage, range = [10, 25], edgecolor = 'black')
plt.title('Maruti Suzuki'); # giving error


# In[91]:


# task 11 part 5

t11c = data[data.Make=='Tata'][['Make','Model','Average_Mileage']]
t11c


# In[92]:


# task 11 part 6

plt=reload(plt)
plt.hist(t11c.Average_Mileage, range = [10, 25], edgecolor = 'black')
plt.title('TATA'); # giving error


# In[93]:


# task 11 part 7

t11d = data[data.Make=='Bmw'][['Make','Model','Average_Mileage']]
t11d


# In[94]:


# task 11 part 7

plt=reload(plt)
plt.hist(t11d.Average_Mileage, range = [10, 25], edgecolor = 'black')
plt.title('BMW');


# In[ ]:





# In[ ]:




