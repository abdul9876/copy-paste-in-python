#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pyclip')


# In[5]:


import pyclip
pyclip.copy("hello world")
cb_data = pyclip.paste()
print(cb_data)
cb_text = pyclip.paste(text=True)
print(cb_text)


# In[4]:


pyclip.clear()
assert not pyclip.paste()


# In[ ]:




