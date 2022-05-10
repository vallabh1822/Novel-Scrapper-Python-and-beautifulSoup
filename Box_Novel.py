#!/usr/bin/env python
# coding: utf-8

# In[14]:



import Boxnovel_scrapper as bsp


# In[9]:


name = input("enter Novel name as copied from boxnovel.com:")


# In[11]:


start= int(input("enter start chapter:"))
end= int(input("enter end chapter to download:"))
delay=  int(input("enter your acceptable delay time is sec :"))
print("download {} chapters from {} to {}".format(name, start, end))


# In[16]:


outFile=bsp.BoxNovelScrape(start, end+1, name= name,delay=delay)


# In[9]:





# In[ ]:




