#!/usr/bin/env python
# coding: utf-8

# In[6]:


# task 1, prints the appropriate word
char = input("Enter either A, B or C   =  ")
char2 = char.upper()
if(char2 == "A"):
    print("Python")
elif(char2 == "B"):
    print("MySQL")
elif(char2 == "C"):
    print("Excel")
else:
    print("Holiday")


# In[8]:


# task 2, displays the largest
num1 = int(input("Enter number 1 = "))
num2 = int(input("Enter number 2 = "))
if(num1 > num2):
    print(num1, "is greater than", num2)
else:
    print(num2, "is greater than", num1)


# In[43]:


# task 3, calculates the final salary
basicSalary = float(input("Enter your basic salary = "))
if(basicSalary <= 4000 and basicSalary > 1):
    finalSalary = basicSalary + ((10 / 100) * basicSalary) + ((5 / 100) * basicSalary) # +10% HRA, 5% DA, 0% tax
    print(finalSalary, "is the final salary")
elif(basicSalary > 4000 and basicSalary <= 10000):
    finalSalary = basicSalary + ((20 / 100) * basicSalary) + ((10 / 100) * basicSalary) - ((15 / 100) * basicSalary) # +20% HRA, 10% DA, 15% tax
    print(finalSalary, "is the final salary")
elif(basicSalary > 10000):
    finalSalary = basicSalary + ((25 / 100) * basicSalary) + ((15 / 100) * basicSalary) - ((20 / 100) * basicSalary) # +25% HRA, 15% DA, 20% tax
    print(finalSalary, "is the final salary")
else:
    print("ERROR! Salary cannot be negative or 0")


# In[46]:


# task 4, checks the presence of substring
var = "Python is an interpreted high-level general-purpose programming language. It's design philosophy emphasizes code redability with its use of significant indentation. It's language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
var2 = input("Enter text to be checked = ")
if(var2 in var):
    print(var2, " exists in the variable")
else:
    print(var2, " does not exists in the variable")


# In[15]:


# task 5, checks the upper or lowercase
char = input("Enter the character = ")
if(char == char.upper()):
    print(char, "is uppercase")
else:
    print(char, "is lowercase")


# In[24]:


# task 6 alt 1 (checks if input is vowel)
set = {"a", "e", "i", "o", "u", "s"}
inp = input("nter the character = ")
if(inp.lower() in set):
    print(inp, "is a vowel")
else:
    print(inp, "is a consonant")


# In[31]:


# task 6 alt 2 (checks if input is vowel)
char = input("Enter the character = ").lower()
if(char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
    print(char, "is a vowel")
else:
    print(char, "Entered character is a consonant")

