#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd


# In[3]:


#period, short description, temperature and


# In[4]:


page = requests.get("https://forecast.weather.gov/MapClick.php?lon=-122.40731529128576&lat=37.77610140364207#.YJdgFbUzZPa")


# In[5]:


page


# In[6]:


soup = BeautifulSoup(page.content)
soup


# In[7]:


#extracting period
period1 = soup.find_all('div',class_ = 'col-sm-2 forecast-label')


# In[8]:


period = []
for i in period1:
    for j in i.find_all("b"):
        period.append(j.text)
period  


# In[9]:


#all periods extracted


# In[10]:


#short description


# In[11]:


description1 = soup.find_all('div',class_ = "col-sm-10 forecast-text")


# In[12]:


description = []
for i in description1:
    description.append(i.text)


# In[13]:


description


# In[32]:


short_description = description.copy()


# In[33]:


short_description


# In[35]:


short_description[0] = short_description[0].replace(', with a low around 53. West wind 7 to 9 mph. ','')


# In[36]:


short_description


# In[34]:


short_description[1] = short_description[1].replace(', with a high near 72. West wind 7 to 15 mph, with gusts as high as 20 mph. ','')


# In[37]:


short_description[2] = short_description[2].replace(', with a low around 53. West wind 6 to 14 mph, with gusts as high as 18 mph. ','')


# In[54]:


short_description[3] = short_description[3].replace(', with a high near 75. Light west northwest wind becoming west 10 to 15 mph in the afternoon. Winds could gust as high as 20 mph. ','')  


# In[39]:


short_description[4] = short_description[4].replace(', with a low around 52. West wind 5 to 14 mph. ','')


# In[40]:


short_description[5] = short_description[5].replace(', with a high near 72.','')


# In[41]:


short_description[6] = short_description[6].replace(', with a low around 51.','')


# In[42]:


short_description[7] = short_description[7].replace(' with a high near 70.','')


# In[43]:


short_description[8] = short_description[8].replace(', with a low around 51.','')


# In[44]:


short_description[9] = short_description[9].replace(', with a high near 66.','')


# In[45]:


short_description[10] = short_description[10].replace(', with a low around 50.','')


# In[46]:


short_description[11] = short_description[11].replace(', with a high near 66.','')


# In[47]:


short_description[12] = short_description[12].replace(', with a low around 51.','')


# In[48]:


short_description[13] = short_description[13].replace(', with a high near 66.','')


# In[55]:


short_description


# In[56]:


#short description done


# In[65]:


#lower temperature
temperature= description.copy()


# In[66]:


temperature


# In[67]:


temperature[0] = temperature[0].replace('Clear, with a ','').replace(' around','').replace('. West wind 7 to 9 mph. ','')


# In[68]:


temperature[1] = temperature[1].replace('Sunny, with a ','').replace('near ','').replace('. West wind 7 to 15 mph, with gusts as high as 20 mph. ','')


# In[69]:


temperature[2] = temperature[2].replace('Mostly clear, with a ','').replace('around ','').replace('. West wind 6 to 14 mph, with gusts as high as 18 mph. ','')


# In[71]:


temperature[3] = temperature[3].replace('Sunny, with a ','').replace('near ','').replace('. Light west northwest wind becoming west 10 to 15 mph in the afternoon. Winds could gust as high as 20 mph. ','')


# In[72]:


temperature[4] = temperature[4].replace('Clear, with a ','').replace('around ','').replace('. West wind 5 to 14 mph. ','')


# In[73]:


temperature[5] = temperature[5].replace('Sunny, with a ','').replace('near ','')


# In[74]:


temperature[6] = temperature[6].replace('Mostly clear, with a ','').replace('around ','')


# In[75]:


temperature[7] = temperature[7].replace('Sunny, with a ','').replace('near ','')


# In[76]:


temperature[8] = temperature[8].replace('Partly cloudy, with a ','').replace('around ','')


# In[77]:


temperature[9] = temperature[9].replace('Mostly sunny, with a ','').replace('near ','')


# In[79]:


temperature[10] = temperature[10].replace('Partly cloudy, with a ','').replace(' around','')


# In[80]:


temperature[11] = temperature[11].replace('Mostly sunny, with a ','').replace('near ','')


# In[81]:


temperature[12] = temperature[12].replace('Partly cloudy, with a ','').replace('around ','')


# In[82]:


temperature[13] = temperature[13].replace('Sunny, with a ','').replace('near ','')


# In[83]:


temperature


# In[94]:


for i in range(5,14):
    temperature[i] = temperature[i].replace('. ','')


# In[96]:


temperature


# In[97]:


#temperature extracted


# In[106]:


Forecast1 = pd.DataFrame({})


# In[107]:


Forecast1["Period(From 9pm ,8th May)"] = period
Forecast1["Short Description"] = short_description
Forecast1["Temperature (in Fahrenheit)"] = temperature
Forecast1["Detailed Description"] = description


# In[108]:


Forecast1


# In[ ]:




