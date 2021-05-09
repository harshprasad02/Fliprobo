#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


page = requests.get("https://bookpage.com/reviews/26195-rivers-solomon-sorrowland-fiction#.YJJItbUzZPY")
page


# In[5]:


soup = BeautifulSoup(page.content)


# In[6]:


soup


# In[7]:


#first book title
title = soup.find('h1',class_="italic")
title.text


# In[60]:


titleS=title.text.replace('\n★ ','').replace('\n','')
titleS


# In[9]:


#first book author name 
author1  = soup.find('h4',class_="sans")
author1.text


# In[10]:


authorS = author1.text.replace('\n','')
authorS


# In[11]:


#first book genre
genre1 = soup.find('p',class_="genre-links")
genre1.text


# In[12]:


genreS = genre1.text.replace('\n','')
genreS


# In[13]:


#first book review
review1 = soup.find('div',class_="article-body")
review1.text


# In[14]:


reviewS = review1.text.replace('\n','')
reviewS


# In[15]:


#Book 2
#title
page1 = requests.get("https://bookpage.com/reviews/26191-maggie-shipstead-great-circle-fiction#.YJJMrLUzZPY")
page1


# In[16]:


soup1 = BeautifulSoup(page1.content)


# In[17]:


title1 = soup1.find('h1',class_="italic")
title1.text


# In[18]:


titleG=title1.text.replace('\n★ ','').replace('\n','')
titleG


# In[19]:


#author
author2  = soup1.find('h4',class_="sans")
author2.text


# In[20]:


authorG = author2.text.replace('\n','')
authorG


# In[21]:


#genre
genre2 = soup1.find('p',class_="genre-links")
genre2.text


# In[22]:


genreG = genre2.text.replace('\n','')
genreG


# In[23]:


#review
review2 = soup1.find('div',class_="article-body")
review2.text


# In[24]:


reviewG = review2.text.replace('\n','').replace("\xa0\nALSO IN BOOKPAGE: Maggie Shipstead may not want to be a pilot, but she can’t help but explore that skyward impulse.",'').replace('\xa0','')
reviewG


# In[25]:


#Book 3
#title
page2 = requests.get("https://bookpage.com/reviews/26201-jhumpa-lahiri-whereabouts-fiction#.YJJxO7UzZPY")
page2


# In[26]:


soup2 = BeautifulSoup(page2.content)


# In[27]:


title2 = soup2.find('h1',class_="italic")
title2.text


# In[28]:


titleW=title2.text.replace('\n★ ','').replace('\n','')
titleW


# In[29]:


#author
author3  = soup2.find('h4',class_="sans")
author3.text


# In[30]:


authorW = author3.text.replace('\n','')
authorW


# In[31]:


#genre
genre3 = soup2.find('p',class_="genre-links")
genre3.text


# In[32]:


genreW = genre2.text.replace('\n','')
genreW


# In[33]:


#review
review3 = soup2.find('div',class_="article-body")
review3.text


# In[34]:


reviewW = review3.text.replace('\n','')
reviewW


# In[35]:


#book 4
page4 = requests.get("https://bookpage.com/reviews/26192-fiona-mozley-hot-stew-fiction#.YJJ0zbUzZPY")
page4


# In[37]:


soup4 = BeautifulSoup(page4.content)


# In[38]:


title4 = soup4.find('h1',class_="italic")
title4.text


# In[39]:


titleH=title4.text.replace('\n','')
titleH


# In[40]:


#author
author4  = soup4.find('h4',class_="sans")
author4.text


# In[41]:


authorH = author4.text.replace('\n','')
authorH


# In[42]:


#genre
genre4 = soup4.find('p',class_="genre-links")
genre4.text


# In[43]:


genreH = genre4.text.replace('\n','')
genreH


# In[44]:


#review
review4 = soup4.find('div',class_="article-body")
review4.text


# In[45]:


reviewH = review3.text.replace('\n','').replace('\xa0','')
reviewH


# In[46]:


#book 5
page5 = requests.get("https://bookpage.com/reviews/26198-chanel-cleeton-most-beautiful-girl-cuba-fiction#.YJd067UzZPY")
page5


# In[47]:


soup5 = BeautifulSoup(page5.content)


# In[49]:


title5 = soup5.find('h1',class_="italic")
title5.text


# In[51]:


titleTM=title5.text.replace('\n','')
titleTM


# In[52]:


#author
author5  = soup5.find('h4',class_="sans")
author5.text


# In[53]:


authorTM = author5.text.replace('\n','')
authorTM


# In[54]:


#genre
genre5 = soup5.find('p',class_="genre-links")
genre5.text


# In[55]:


genreTM = genre5.text.replace('\n','')
genreTM


# In[56]:


#review
review5 = soup5.find('div',class_="article-body")
review5.text


# In[57]:


reviewTM = review5.text.replace('\n','')
reviewTM


# In[63]:


Titles1 = [titleS,titleG,titleW,titleH,titleTM]


# In[64]:


Titles1


# In[65]:


Author = [authorS,authorG,authorW,authorH,authorTM]


# In[66]:


Genre = [genreS,genreG,genreW,genreH,genreTM]


# In[69]:


Review = [reviewS,reviewG,reviewW,reviewH,reviewTM]


# In[68]:


Books = pd.DataFrame({})


# In[70]:


Books["Title of the Book"] = Titles1
Books["Author Name"] = Author
Books["Book Genre"] = Genre
Books["Book Review"] = Review


# In[71]:


Books


# In[ ]:




