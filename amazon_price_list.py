#!/usr/bin/env python
# coding: utf-8

# In[17]:


from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd


# In[22]:


page = requests.get("https://www.amazon.in/s?k=mobile+phones+under+20000+rupees&ref=nb_sb_noss")


# In[23]:


page


# In[24]:


soup = BeautifulSoup(page.content)


# In[29]:


names1 = soup.find_all('span',class_ = "a-size-medium a-color-base a-text-normal")
names1


# In[30]:


phone_names = []
for i in names1:
        phone_names.append(i.text)
phone_names


# In[77]:


np.count_nonzero(phone_names)


# In[32]:


#extracting prices
price = soup.find_all('span',class_ ="a-price-whole")
price


# In[33]:


phone_price = []
for i in price:
        phone_price.append(i.text)
phone_price


# In[79]:


phone_price1 = phone_price[4:20]


# In[80]:


phone_price1


# In[76]:


np.count_nonzero(phone_price)


# In[34]:


#extracting ratings
ratings = soup.find_all('span',class_ ="a-icon-alt")
ratings


# In[41]:


np.count_nonzero(phone_price)


# In[42]:


ratings1 = []
for i in ratings:
    ratings1.append(i.text)
ratings1


# In[43]:


np.count_nonzero(ratings1)


# In[46]:


phone_ratings = ratings1[0:20]


# In[81]:


phone_ratings1 = phone_ratings[4:20]
phone_ratings1


# In[82]:


np.count_nonzero(phone_ratings1)


# In[64]:


#image link
images = soup.find_all('img')
images


# In[69]:


image_link1 = []
for i in images:
    link = i['src']
    image_link1.append(link)
image_link1


# In[68]:


np.count_nonzero(image_link)


# In[87]:


image_link = image_link1[3:23]


# In[90]:


image_link2 = image_link[4:20]


# In[92]:


image_link2


# In[93]:


Amazon_phones_list = pd.DataFrame({})


# In[95]:


Amazon_phones_list["Phone Name"] = phone_names
Amazon_phones_list["Price of phone"] = phone_price1
Amazon_phones_list["Ratings of phone"] = phone_ratings1
Amazon_phones_list["Image link"] = image_link2


# In[96]:


Amazon_phones_list


# In[ ]:




