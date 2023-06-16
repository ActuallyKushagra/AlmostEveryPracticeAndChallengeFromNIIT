#!/usr/bin/env python
# coding: utf-8

# In[25]:


from itertools import combinations as com


# In[20]:


# task 1

members = ['Ava']
for i in range(11):
    members.append('Member' + str(i+2))

len(list(com(members, 1))) * len(list(com(members, 4)))


# In[3]:


# task 2

total = 150
car = 80
van = 50
lorry = 20

print(f"""
a) Probability of car leaving first = {van}/{total}
b) Probability of lorry leaving first = {lorry}/{total}
c) Probability of car leaving second if either lorry or van left first = ({van}/{total} + {lorry}/{total}) * {car}/{total}""")


# # task 3
# 
# ![image.png](attachment:image.png)

# ### a) 2 left handed children
# 
# probability that there are two left handed children =  8/30
#                                                     => 4/15

# ### b) probability that there are at least 3 left handed children
# 
# probability that there are at least 3 left handed children =  (5+12+2)/30
#                                                            => 19/30

# # Task 4
# 
# ![image.png](attachment:image.png)

# 

# ![IMG_20221220_192850166-2.jpg](attachment:IMG_20221220_192850166-2.jpg)

# # task 5
# 
# a) Since the the smallest number on a dice is 1 and 2 dices are being rolled, the probability of the getting sum as 1 is 0
#  
#  
#  
# b) favourable_outcomes = [[1, 3], [2, 2], [3, 1]]
#  
#     total_outcomes   = 36
#     probability      = 3/36
#     
#     
#     
# c) Since hightest number on a dice is 6 and 2 are being rolled, maximum number possible to achieve through sum is 12 and the question's requirement is less than 13.
# 
# Therefore, the favourable outcomes are 36 and total possible outcomes are also 36. 
# 
# Hence, probability is 36/36, ie, 1.

# # task 6
# 
# 20 tickets from number 1 to 20
# 
# a) probability that the ticket selected is even = 10/20 (Since there are 10 even numbers till 20)
# 
# b) probability of selecting a number divisible by 3 
#     
#     numbers divisible by 3 range 1 to 20 = [3, 6, 9, 12, 15, 18]     = 6 numbers
#     probability of selecting a number divisible by 3                 = 6/20
# 
# c) probability of selecting a prime number
# 
#     prime numbers between 1 and 20 = [2, 3, 5, 7, 11, 13, 17, 19]    = 8 numbers
#     probability of selecting a prime number                          = 8/20
#                                                                      = 4/10
#                                                                      = 2/5
#                                                                      
# d) probability of selecting a number divisible by 5
# 
#     numbers divisible by 5 = [5, 10, 15, 20]                         = 4 numbers
#     probability of selecting a number divisible by 5                 = 4/20
#                                                                      = 2/10
#                                                                      = 1/5

# # task 7
# 
# 
# 3 dice
# 
# 11 or 12 as sum more likely
# 
# all possible outcomes = 6^3 = 216
# 
# 
# probability of 11 => 27/216
# 
# probability of 12 => 25/216
# 
# Sum of 11 from a rolling of 3 dices is more likely to occur

# In[ ]:




