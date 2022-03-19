#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import autoreload
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# In[2]:



import Boxnovel_scrapper as bsp


# In[2]:


name = input("enter Novel name as copied from boxnovel.com:")


# In[5]:


start= input("enter start chapter:")
end= input("enter end chapter to download:")
print("download {} chapters from {} to {}".format(name, start, end))


# In[3]:


outFile=bsp.BoxNovelScrape(start, end, name= name)


# In[9]:





# In[ ]:





# In[ ]:




