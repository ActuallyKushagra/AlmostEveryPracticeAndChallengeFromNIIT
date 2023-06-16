#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[22]:


# task 1 Generate student id for 40 students

student_id=pd.Series(index=np.arange(1001,1041))
student_id


# In[52]:


# t2 assign marks for those students

MathL1Marks=np.random.randint(50,95,size=40)
mathRC=pd.Series(MathL1Marks,index=np.arange(1001,1041))
mathRC


# In[53]:


# t3 assign physics marks

PhyL1Marks=np.random.randint(40,95,size=40)
phyRC=pd.Series(PhyL1Marks,index=np.arange(1001,1041))
phyRC


# In[54]:


# t4 students who are eligible for level 2

L1Total=(mathRC.add(phyRC))
L1Total

L1Eligible=L1Total[L1Total>150]
print(L1Eligible)
np.size(L1Eligible)


# In[56]:


# task 5 part 1 -  assign marks for students in level 2 for maths and physcis

MathL2Marks=np.random.randint(50,100,size=10)
mathRC2=pd.Series(MathL2Marks,index=L1Eligible.index)
print(mathRC2)
np.size(mathRC2)


# In[58]:


# task 5 part 2

phyRC2=np.random.randint(30,100,size=10)
phyRC2=pd.Series(phyRC2,index=L1Eligible.index)
phyRC2


# In[59]:


# task 5 part 3 - Totalling scores of level 1 and level 2

L2Total=(mathRC2.add(phyRC2))
L2Total
L1L2Eligible=L1Eligible+L2Total
L1L2Eligible


# In[60]:


# task 6 students who are eligible for the screening test, marks > 300

TestEligible = L1L2Eligible[L1L2Eligible>300]
print(TestEligible)
np.size(TestEligible)


# In[62]:


# task 7 Assign marks scored in the screening test and evaluate 40% of level 2 score + 60% of screening

MathTest=np.random.randint(50,95,size=9)
PhysicsTest=np.random.randint(50,95,size=9)


mathST=pd.Series(MathTest,index=TestEligible.index)
physicsST=pd.Series(PhysicsTest,index=TestEligible.index)

STtotal=(mathST+physicsST)

temp= (TestEligible.mul(0.4))

temp2=(STtotal*0.6)

marks=(temp.add(temp2))
print(marks)
np.size(marks)


# In[66]:


# task 8 Students who are eligible for test, marks > 75%
# This cell and beyond not working on anaconda/ jupyter. Works on google collab

MathL1L2Marks=(mathRC[TestEligible.index] + mathRC2[TestEligible.index])


MathFinal=(MathL1L2Marks + MathTest)

PassMarks =(MathFinal.mul(0.75))
EligibleMarks=marks[MathFinal>PassMarks]
print(EligibleMarks)
np.size(EligibleMarks)


# In[65]:


# task 9 push the calculated data into the dataframe

data = pd.DataFrame(EligibleMarks)
EligibleMarks
data[0] = EligibleMarks
data.columns = ["EligibleMarks"]
print("lowest marks =  ", min(data.EligibleMarks))
print("highest marks = ", max(data.EligibleMarks))
print("____________________________________________________")
data


# In[ ]:




