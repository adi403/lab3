#!/usr/bin/env python
# coding: utf-8

# In[4]:


def factorial(n):
     
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 
 
num = 10

print("Factorial of",num,"is",factorial(num))


# In[ ]:




