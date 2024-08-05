#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(*n):
    return sum(n)


# In[2]:


def mul(*n):
    m = 1 
    for i in n :
        m = m * i
    return m 


# In[3]:


def odd(lst):
    return list(filter(lambda x : x % 2 != 0  , lst))


# In[4]:


def even(lst):
    return list(filter(lambda x : x % 2 == 0  , lst))


# In[ ]:




