#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


get_ipython().system('pip install requests')


# In[3]:


from bs4 import BeautifulSoup
import requests


# In[6]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page


# We can extract data from this page

# In[7]:


soup = BeautifulSoup(page.content)


# In[8]:


soup


# In[14]:


headings = soup.find_all('h2', class_ = 'mp-h2')


# In[15]:


headings


# In[16]:


#extracting all headings


# In[17]:


all_headings = []
for i in headings:
    all_headings.append(i.text)
all_headings


# In[18]:


head = soup.find('h1', class_ = 'firstHeading')


# In[19]:


head.text


# In[20]:


all_headings.append(head.text)


# In[21]:


all_headings


# In[25]:


all_headings[1] = all_headings[1].replace('\xa0','')


# In[26]:


all_headings


# In[27]:


import pandas as pd


# In[28]:


Headers = pd.DataFrame({})
Headers["Heading"] = all_headings


# In[29]:


Headers


# In[ ]:




