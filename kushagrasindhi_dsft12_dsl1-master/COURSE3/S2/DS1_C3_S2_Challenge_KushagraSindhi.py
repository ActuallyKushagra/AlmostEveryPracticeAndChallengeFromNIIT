#!/usr/bin/env python
# coding: utf-8

# In[35]:


# task 1, checks the leap year
year = int(input("Enter the year between 1900 and 2100 = "))
if(year % 4 == 0):
    if(year % 100 != 0): # should be divisible by 4 and 100 with remainder as 0 and "not 0" respectively for leap year
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# In[4]:


# task 2, alt method 1, prints the month name and total days in the month
monthNumberDict = {1: 'January', 2: 'Feburary', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: "July", 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
monthNumDaysDict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
num = int(input("Enter number between 1 and 12 = "))
if(num in monthNumberDict and num in monthNumDaysDict):
    print("number", num, "corresponds to ", monthNumberDict[num], "which has ", monthNumDaysDict[num], "days")
else:
    print("error")


# In[8]:


# task 3, determines the discount applicable on purchase
amt = float(input("Enter the purchase amount = "))
if(amt < 100):
    print("No discount")
elif(amt >= 100 and amt < 150):
    print("Discount is 10%")
elif(amt >= 150 and amt < 200):
    print("Discount is 15%")
elif(amt >= 200 and amt < 250):
    print("Discount is 20%")
else:
    print("Discount is 25%")


# In[38]:


# task 4,
# Waiting for the debrief
ques = int(input("What's 5 times 2? "))
if(ques == 10):
    print("Correct!! ")
else:
    print("Incorrect! Please try again. ")

ques2 = int(input("What's 56 - 6? "))
if(ques2 == 50):
    print("Correct!! ")
else:
    print("Incorrect! Please try again. ")

ques3 = int(input("What's 8 times 9 plus 2? "))
if(ques3 == 74):
    print("Correct!! ")
else:
    print("Incorrect! Please try again. ")


# In[33]:


# task 5, rock-paper-scissor. rock > scissor > paper > rock
import random

uc = input("Enter as rock, paper or scissor = ").lower()
playdict = {1: "rock", 2: "paper", 3: "scissor"}
randval = random.randint(1, 3) # chooses a random value between 1 and 3
cc = playdict[randval].lower() # substitutes the random value in the playdict dictionary
if(uc == cc):
    print("You chose", uc, ',', "Computer chose", cc, ',', "Its a Draw")
elif(uc == "rock" and cc == "paper"):
    print("You chose", uc, ',', "Computer chose", cc, ',', "Computer wins")
elif(uc == "rock" and cc == "scissor"):
    print("You chose", uc, ',', "Computer chose", cc, ',', "You win")
elif(uc == "paper" and cc == "rock"):
    print("You chose", uc, ',', "Computer chose", cc, ',', "You win")
elif(uc == "paper" and cc == "scissor"):
    print("You chose", uc, ',', "Computer chose", cc, ',', "Computer wins")
elif(uc == "scissor" and cc == "paper"):
    print("You chose", uc, ',', "Computer chose", cc, ',', "You win")
elif(uc == "scissor" and cc == "rock"):
    print("You chose", uc, ',', "Computer chose", cc, ',', "Computer wins")
else:
    print("error")

