#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as ny
import random


# ## Part 1

# In[14]:


# task 1 generate employee codes

hr_empcode = ny.arange(1, 501)
fin_empcode = ny.arange(501, 1001)
it_empcode = ny.arange(1001, 1501)
sales_empcode = ny.arange(1501, 2001)


# In[15]:


# task 2 generate salary

hr_sal = ny.random.randint(25000, 50001, 500)
fin_sal = ny.multiply(hr_sal, 1.25)
sales_sal = ny.multiply(fin_sal, 0.5)
it_sal = ny.add(hr_sal, 5000)


# In[16]:


# task 3 cost of each department

totexpense_hr = ny.sum(hr_sal)
totexpense_sales = ny.sum(sales_sal)
totexpense_fin = ny.sum(fin_sal)
totexpense_it = ny.sum(it_sal)
print(f"""
HR department: {totexpense_hr}
Sales department: {totexpense_sales}
Finance department: {totexpense_fin}
IT department: {totexpense_it}""")


# In[17]:


# task 4 top 10 highest salaries in hr and finance department

higsalhr = ny.sort(hr_sal)
higsalfin = ny.sort(fin_sal)
print("Highest HR Salaries", higsalhr[-1:-11:-1])
print("_______________________________________________________________________________")
print("Highest Finance Salaries", higsalfin[-1:-11:-1])


# In[23]:


# task 5 Increase salary by 10% where salary is >45000 and count no of employees in IT and Sales with salary >45000

salessalinc = ny.where(sales_sal > 45000, sales_sal * 1.1, sales_sal)
itsalinc = ny.where(it_sal > 45000, it_sal * 1.1, it_sal)
finsalinc = ny.where(fin_sal > 45000, fin_sal * 1.1, fin_sal)
hrsalinc = ny.where(hr_sal > 45000, hr_sal * 1.1, hr_sal)
print("Updated salaries of Sales department \n", salessalinc)
print("________________________________________________________________________________")
print("Updated salaries of IT department \n", itsalinc)
print("________________________________________________________________________________")
print("Updated salaries of Finance department \n", finsalinc)
print("________________________________________________________________________________")
print("Updated salaries of HR department \n", hrsalinc)

salecount = ny.where(sales_sal > 45000)
itcount = ny.where(it_sal > 45000)
print("________________________________________________________________________________")
print(ny.size(salecount), 'employees earn more than 45000 in sales')
print(ny.size(itcount), 'employees earn more than 45000 in it')
# revist before submission


# In[24]:


# task 6 increase salaries of sales by 10% where salary <45000

salsalinc2 = ny.where(sales_sal < 45000, sales_sal * 1.1, sales_sal)

# update in main record
print("Before increase by 10% \n", sales_sal)
print("___________________________________________________________________________________________________")
sales_sal = ny.where(sales_sal < 45000, sales_sal * 1.1, sales_sal)
print("After increase by 10% \n", sales_sal)


# ## Part 2

# In[4]:


from numpy import genfromtxt

data = genfromtxt("DS1_C4_S1_AdmissionPredict_Data_Practice (1).csv", delimiter = ",", skip_header = 1)


# In[20]:


# task 1 number of students with GRE score above 320

grescore = ny.where(data[0:400, 1:2] > 320)
print(data[grescore].size)


# In[8]:


# task 2 Chance of admission for students with toefl scoe above 110

tof = ny.where(data[0:, 2:3] > 110)
print("Chances of admission for students with toefl score above 110")
print(data[tof, 0:9:8])


# In[11]:


# task 3 

scholars = ny.where((data[:,1:2]>315) & (data[:,2:3]>115 ) & (data[:,7:8]>=1))
print(data[scholars].size, 'Students are eligible for the scholarship')
print('These are the serial numbers for the students who are eligible \n', data[scholars])

