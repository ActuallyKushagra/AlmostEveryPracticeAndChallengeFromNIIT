#!/usr/bin/env python
# coding: utf-8

# In[1]:


from itertools import permutations as perm, combinations as com, product as pro, combinations_with_replacement as cr


# In[ ]:





# In[24]:


# task 1



men = ['man1', 'man2', 'man3', 'man4', 'man5', 'man6']
women = ['woman1', 'woman2', 'woman3', 'woman4']


# In[25]:



# a) 3 men and 2 women

print(len(list(com(men, 3))) * len(list(com(women, 2))))


# In[27]:



# b) Men only

print(len(list(com(men, 5))))


# In[39]:



# c) Majority women

print(len(list(com(women, 3))) * len(list(com(men, 2))) + len(list(com(women, 4))) * len(list(com(men, 1))))


# In[45]:


# task 2

deck = []
for i in range(52):
    deck.append('Card'+str(i+1))
    i+=1

len(list(com(deck, 5)))


# In[50]:


# task 3

contestants = ['Alice', 'Ava', 'Charlie', 'David', 'Eve', 'Frank', 'George', 'Mia']

len(list(perm(contestants, 3)))


# ### task 4
# 
# ![IMG_20221220_200557198.jpg](attachment:IMG_20221220_200557198.jpg)

# In[8]:


len(list(perm(students, 2)))


# ### task 5
# 
# favourable_outcomes = [[1, 3], [2, 6], [6, 2], [3, 1]]
# 
# totot_number_of_outcomes = 36
# 
# favourable_outcomes             =      4
# 
# total_number_of_outcomes        =     36
# 
# 4/36 
# 
# => 1/9

# In[72]:


# task 6

conso = []
vovel = []

for i in range(7):
    conso.append('Consonant' + str(i+1))
    i+=1
for i in range(4):
    vovel.append('Vovel' + str(i+1))
    i+=1

print(len(list(com(conso, 3))) * len(list(com(vovel, 2))))


# In[81]:


# task 7

bulbs = []

for i in range(25):
    bulbs.append('Bulb' + str(i+1))
    i+=1
    
# 25% is defective, one bulb is drown which is not defective.
bulbs.pop()
bulbs

# 25% is defective
total = len(bulbs)
defect = total * 0.25
good = total - defect

print(f'{defect} are bad out of {total}, that means {good} are not defective')

print('Probability that the bulb is good is ', int(good), '/', total)

