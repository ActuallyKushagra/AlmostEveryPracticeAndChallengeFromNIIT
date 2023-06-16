#!/usr/bin/env python
# coding: utf-8

# # Creating variables

# In[11]:


# a
rollNo = 1
print(rollNo, "is the value,", id(rollNo), "is the memory address, and", type(rollNo), "is the datatype")


# In[12]:


# b
firstName = "Wruce"
print(firstName, "is the value,", id(firstName), "is the memory address, and", type(firstName), "is the datatype")


# In[13]:


# c
lastName = "Bayne"
print(lastName, "is the value,", id(lastName), "is the memory address, and", type(lastName), "is the datatype")


# In[14]:


# d
maxMarks = 50
print(maxMarks, "is the value,", id(maxMarks), "is the memory address, and", type(maxMarks), "is the datatype")


# # Naming variable

# In[15]:


# a
var1 = 2 #  (a) assigns the value since it follows the rules
print(var1)


# In[16]:


# b
2var = 2 # (b) does not assign since it does not follow the rules (variable name must not start with numeric value)
print(2var)


# In[17]:


# c
var 1 = 2 # (c) does not assign since it does not follow the rules (variable name must not contain empty space)
print(var 1)


# In[18]:


# d
var$2 = 2 # (d) does not assign since it does not follow the rules (variable name must not contain special characters)
print(var$2)


# # Assigning values to variables

# In[19]:


# a
Class = 15
print(Class, id(Class)) # assigns the variable, displays it's value and ID (memory address)


# In[20]:


# b
class = 14 
print(class, id(class)) # since class is a reserved keyword, it cannot be used name a variable


# In[21]:


# c 
DEF = 13
print(DEF, id(DEF)) # assigns the variable, displays it's value and ID (memory address)


# In[22]:


# d
def = 12
print(def, id(def)) # since def is a reserved keyword, it cannot be used name a variable


# In[23]:


# e
a = True
print(a, id(a)) # assigns the variable, displays it's value and ID (memory address)


# In[24]:


# f
b = False
print(b, id(b)) # # assigns the variable, displays it's value and ID (memory address)


# # Using id()

# In[25]:


marks = 49.5
print(marks, "is the value,", id(marks), "is the memory address, and", type(marks), "is the datatype")


# In[26]:


marks = 49.9
print(marks, "is the value,", id(marks), "is the memory address, and", type(marks), "is the datatype")


# '''The ID of marks before and after changing the value is different because the the memory address changes are we reassign the values'''

# # formatting output

# In[27]:


# a
percentage = (marks / maxMarks) * 100
print(percentage, "%")


# In[28]:


# b
fullName = firstName + " " + lastName
print(fullName) # b


# In[29]:


# c
print(fullName, " Scored ", percentage, "%")


# # Creating data structures

# In[31]:


# a
rollNameDict = {}
rollNameDict[rollNo] = fullName
print(rollNameDict)


# In[32]:


# b
studentDetailsList = [rollNo, fullName, marks]
print(studentDetailsList)


# # Arithmetic operations
# 

# In[33]:


#a
print(1 + "2") # strings and integer values cannot be added


# In[34]:


#b
print("1" + "2") # since both the values are strings, concatenation function is used


# In[35]:


#c
print(1/2) # the second value is divided by the first value


# In[36]:


#d
print(1//2) # the second value is divided by the first value and then floor function is used on the result. Result is rounded off to the nearest integer value


# # Logical Operations

# In[37]:


True and True   # if both values are true, return value is also true. "AND" must have all conditions true


# In[38]:


True and False # if either of the values are false, the return value is also false. "AND" must have all conditions true


# In[39]:


False or True # if one of the values are true and "OR" is used, the return value is also true. "OR" can have either conditions true


# In[40]:


False or False # if both values are false, the return value is also false. "OR" can have either conditions true


# # Identity and memebership operations

# In[41]:


#a
print(firstName in fullName)
# since firstname is present in the fullname, the output is true. "IN" also means contain


# In[42]:


#b
print(firstName is fullName)
# since the firstname is different from fullname, the output is false. "IS" can also mean same/ equal


# # Associativity

# In[43]:


a = 4 
b = 3 
c = 2 
d = a ** b + c 
e = a ** (b + c)


# In[44]:


# a
print(d)


# In[45]:


# b
print(e)


# In[46]:


'''Since Python follow pemdas, for d, the exponents are calculated first where as for e where brackets are present, backets are calculated frist. Therefore the result is also different for both'''


# # Basic program

# In[47]:


# area of a circle
import math as math
radius = 6
print(math.pi * (radius ** 2), "is the area of the circle")


# In[48]:


# final price
basePrice = 85
salesTaxPercent = 18
taxAmount = basePrice * (salesTaxPercent / 100)
finalPrice = basePrice + taxAmount
print(taxAmount, "is the tax charged,", finalPrice, "is the final amount")


# In[49]:


# rupee to dollar
oneDollar = 75
rupees = 3333
dollarToRupee = rupees / oneDollar
print(dollarToRupee, "dollars are in", rupees, "rupees")


# In[50]:


# purchaing power
inflationRate = 7
money = 500
amountChange = 500 * (7 / 100)
lastYearPurchasingPower = money + amountChange
print("Last year, people could buy products worth $", lastYearPurchasingPower, "in $500")

