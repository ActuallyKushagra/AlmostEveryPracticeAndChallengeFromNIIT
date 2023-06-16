#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[3]:


data = pd.read_csv('DS1_C4_S3_Loan_Data_Challenge.csv.csv')


# In[4]:


# task 1 Total number of males and females 

t1 = data[(data.LoanAmount > 200) & (data.ApplicantIncome < 6000) & (data.Loan_Status == 'Y')][['Loan_ID', 'Gender']]
counter = t1.value_counts("Gender")
print(counter)
t1


# In[5]:


# task 2 Difference and relative percentage of people with urban and semi-urban properties

t2sem = data[(data.Property_Area == "Semiurban")][["Loan_ID"]]
t2urb = data[(data.Property_Area == "Urban")][["Loan_ID"]]

t2semcount = t2sem.shape[0]
t2urbcount = t2urb.shape[0]

absdiff = t2semcount - t2urbcount
avgsemurb = (t2semcount + t2urbcount) / 2
percdiff = ((t2semcount - t2urbcount) / avgsemurb) * 100

print(f"""
The difference between Semi-Urban and Urban is = {absdiff}
The percentage difference between Semi-Urban and Urban is {percdiff}""")


# In[6]:


# task 3 top 5 customers with highest income and approved loan

t3 = data[data.Loan_Status == "Y"].sort_values("ApplicantIncome", ascending = False).head()
t3


# In[7]:


# task 4 income and loan amount of females with two dependents

t4 = data[(data.Gender == 'Female') & (data.Dependents == '2')][['ApplicantIncome', 'LoanAmount']]
t4


# In[8]:


# task 5 update loan_amount_term to 180 for females whose loan amount is greater than 180

t5 = data[(data.Gender == "Female") & (data.LoanAmount > 200)]
t5.loc[t5.Gender == 'Female', 'Loan_Amount_Term'] = 180
t5


# In[9]:


# task 6 rename loan_amount_term, replace values 12 and 36 with 60

t6  = data.rename(columns={"Loan_Amount_Term": "LoanAmountTerm"})
t6['LoanAmountTerm'] = t6.LoanAmountTerm.replace([12, 36], 60)
t6


# In[17]:


# task 7 calculate and assign credit limits of customers with income greater than 10000

CreditLimit = pd.DataFrame(data.ApplicantIncome*2)
CreditLimit=CreditLimit.rename(columns={"ApplicantIncome":"CreditLimit"})

newData = pd.concat([data,CreditLimit],axis=1)
newData.rename(columns={"ApplicantIncome":"CreditLimit"})

newData[(newData.Education == "Graduate") & (newData.Self_Employed == "Yes") & (newData.ApplicantIncome > 10000)][["Loan_ID","ApplicantIncome","CreditLimit"]]


# In[13]:


# task 8 part 1 delete records of customers with 3+ dependents, - credit history and no education

t8 = data[(data.Dependents == "3+") & (data.Credit_History == 0) & (data.Education == "Not Graduate")]
t8b = t8
t8


# In[14]:


# task 8 part 2

t8b.drop([73, 338, 466]) # inserting the index for the rows to be dropped, values taken from task 8 part 1


# In[20]:


# task 9 Compare graduates with non-graduates

totGraduates = newData[(newData.Education == "Graduate")][["ApplicantIncome"]].sum()
avgGraduates = newData[(newData.Education == "Graduate")].loc[:,["ApplicantIncome"]].mean()
medGraduates = newData[(newData.Education == "Graduate")].iloc[0:,[6]].median()

totNonGrad=newData[(newData.Education == "Not Graduate")][["ApplicantIncome"]].sum()
avgNonGrad=newData[(newData.Education == "Not Graduate")].loc[:,["ApplicantIncome"]].mean()
medNonGrad=newData[(newData.Education == "Not Graduate")].iloc[0:,[6]].median()

print(f"Total of graduates {totGraduates}, Total of non-graduates {totNonGrad}")
print("___________________________________________________________________________________________")
print(f"Average of graduates {avgGraduates}, Average of non-graduates {avgNonGrad}")
print("___________________________________________________________________________________________")
print(f"Median of graduates {medGraduates}, Median of non-graduates {medNonGrad}")

