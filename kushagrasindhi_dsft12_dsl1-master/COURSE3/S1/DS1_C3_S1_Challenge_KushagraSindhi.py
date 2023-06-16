#!/usr/bin/env python
# coding: utf-8

# In[1]:


# task 1, calculate area of circle
import math as math
radius = 6
print(math.pi * (radius ** 2), "is the area of the circle")


# In[2]:


# task 2, calculate tax amount and final amount
basePrice = 85
salesTaxPercent = 18
taxAmount = 85 * (18 / 100)
finalPrice = basePrice + taxAmount
print(finalPrice, "is the final price after tax")


# In[3]:


# task 3, usd to inr conversion
oneDollar = 75
rupees = 3333
dollarToRupee = rupees / oneDollar
print(dollarToRupee, "dollars are in", rupees, "rupees")


# In[4]:


# task 4, calculate purchasing power for last year
inflationRate = 7
money = 500
amountChange = 500 * (7 / 100)
lastYearPurchasingPower = money + amountChange
print("Last year, people could buy products worth $", lastYearPurchasingPower, "in $500")


# In[7]:


# task 5, print name and language currently learning
name = input()
language = input()
print("Hello I'm", name,'.', "I'm learning", language,'.')


# In[2]:


# task 6, calculate simple interest
principleAmount = float(input("amount = "))
interestRate = float(input("interest = "))
time = float(input("time = "))
simpleInterest = (principleAmount * time * interestRate) / 100
print("Simple interest is = ", simpleInterest)


# In[6]:


# task 7, calculate simple interest #2
principleAmount = float(input("principle amount = "))
interestRate = float(input("interest = "))
time = float(input("time = "))
amount = principleAmount * (1 + interestRate/ 100) ** time
simpleInterest = amount - principleAmount
print("Simple interest is = ",simpleInterest)


# In[18]:


# task 8, swap two numbers
num_var1 = 1
num_var2 = 2
print("Before changing = ", num_var1,"&", num_var2)
num_var1 = num_var1 + num_var2
num_var2 = num_var1 - num_var2
num_var1 = num_var1 - num_var2
print("After changing = ", num_var1,"&", num_var2)


# In[19]:


# task 9, km to miles
kmDistance = float(input("Distance in Kilometre = "))
milesDistance = float(kmDistance / 1.6)
print(kmDistance, 'km is', milesDistance, "in miles")


# In[20]:


# task 10, table of input number
num = int(input("Enter number for table calculation = "))
for i in range(1, 11):
    print(num, "X", i, "=", num * i)


# In[ ]:




