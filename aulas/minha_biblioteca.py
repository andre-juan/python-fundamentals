#!/usr/bin/env python
# coding: utf-8

# In[1]:


def cumprimenta(nome):
    
    print("Olá,", nome)


# In[2]:


def soma(n1, n2):
    
    return n1 + n2


# In[3]:


def fatorial(n):
    
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)

