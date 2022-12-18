#!/usr/bin/env python
# coding: utf-8

# In[1]:


l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l1 = []
def flatten(n):
    for i in n :
        if isinstance(i,list):
            flatten(i)
        else:
            l1.append(i)

flatten(l)
print(l1)


# In[ ]:




