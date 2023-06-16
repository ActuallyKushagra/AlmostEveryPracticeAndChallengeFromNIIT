#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import warnings 
warnings.filterwarnings('ignore')


# In[2]:


data = pd.read_csv('DS1_C4_S3_Loan_Data_Practice.csv.csv')


# In[3]:


# task 1 Number of male customers who are gratuates & have loan approved

t1 = data[(data.Education == 'Graduate') & (data.Loan_Status == 'Y') & (data.Gender == 'Male')]
print(f"There are a total of \n {t1.count()} \n customers who have graduated, are male and have a loan status as YES, they are:- ")
t1


# In[4]:


# task 2 female customers who are self employed and have income greater than 4000

t2 = data[(data.Gender == 'Female') & (data.Self_Employed == 'Yes') & (data.ApplicantIncome > 4000)]
t2


# In[5]:


# task 3 Customers from rural area with approved loan and dependants  "3+"

t3 = data[(data.Property_Area == 'Rural') & (data.Loan_Status == 'Y') & (data.Dependents == '3+')]
print(f"There are a total of \n {t3.count()} \n customers with matching profile")
t3


# In[6]:


# task 4 average applicant's income whose loan of 290000 or above was  approved

t4 = data[(data.LoanAmount >= 290) & (data.Loan_Status == 'Y')][['ApplicantIncome']]
t4avg = np.mean(t4)
t4avg
# to be checked at debrief 


# In[9]:


# task 5 customers who are self employed whose loan was rejected and their total numbers according to gender

t5 = data[(data.Loan_Status == 'N') & (data.Married == 'No') & (data.Self_Employed == 'Yes')]

print(t5.value_counts("Gender"))
t5


# In[25]:


# task 6 Part 1 income by property area comparsison

t6rur = data[data.Property_Area == "Rural"][["ApplicantIncome"]]
t6urb = data[data.Property_Area == "Urban"][["ApplicantIncome"]]
t6sem = data[data.Property_Area == "Semiurban"][["ApplicantIncome"]]


# In[27]:


# Task 6 Part 2 -  rural income

t6rur


# In[28]:


# Task 6 Part 3 - urban income

t6urb


# In[29]:


# Task 6 Part 4 - semi-urban income

t6sem


# In[54]:


# task 7 Details and total number of customers whose coapplicants earn less than average of all coapplicant income

avgcoi = np.mean(data.CoapplicantIncome)
t7 = data[(data.Married == 'Yes') & (data.CoapplicantIncome < avgcoi)]
print(f"There are {t7.count()} customers whose coapplicant's income is less than average of income of all coapplicants")
t7


# In[44]:


# task 8 total number of Customers who are graduate and have income between 10256 and 150000

t8 = data[(data.Education == "Graduate" ) & (data.ApplicantIncome.between(10256,150000))]
print(f"There are a total of \n {t8.count()} \n customers who are graduates and have income between 10256 and 150000")

