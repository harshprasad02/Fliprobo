#!/usr/bin/env python
# coding: utf-8

# In[156]:


import numpy as np
import pandas as pd


# In[3]:


from bs4 import BeautifulSoup
import requests


# In[7]:


page = requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")
page


# In[11]:


soup = BeautifulSoup(page.content)


# In[12]:


soup


# In[56]:


titles1 = soup.find_all('h3', class_="lister-item-header")


# In[57]:


titles1


# In[145]:


movie_title = []
for i in titles1:
    for j in i.find_all("a"):
          movie_title.append(j.text)
movie_title


# In[32]:


ratings1 = soup.find_all('strong')


# In[33]:


ratings1


# In[34]:


rating_of_movies = []
for i in ratings1:
    rating_of_movies.append(i.text)
rating_of_movies


# In[30]:


year1 = soup.find_all('span', class_="lister-item-year text-muted unbold")


# In[31]:


year1


# In[117]:


movie_year1 = []
for i in year1:
    movie_year1.append(i.text)
movie_year1   


# In[60]:


page2 = requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt")
page2


# In[61]:


soup1 = BeautifulSoup(page2.content)


# In[62]:


title2 = soup1.find_all('h3', class_="lister-item-header")


# In[134]:


title2


# In[146]:


for i in title2:
    for j in i.find_all("a"):
          movie_title.append(j.text)
movie_title


# In[164]:


rating2 = soup.find_all("strong")


# In[66]:


for i in rating2:
    rating_of_movies.append(i.text)
rating_of_movies


# In[81]:


rating_of_movies.remove('User Rating')
rating_of_movies.remove('User Rating')
rating_of_movies.remove('Detailed')


# In[83]:


final_rating=rating_of_movies


# In[84]:


final_rating


# In[113]:


np.count_nonzero(final_rating)


# In[85]:


year2 = soup.find_all('span', class_="lister-item-year text-muted unbold")


# In[86]:


year2


# In[114]:


year2


# In[118]:


for i in year2:
    movie_year1.append(i.text)
movie_year1   


# In[119]:


np.count_nonzero(movie_year1)


# In[121]:


def remove_brackets(list_name,e1,e2):
    for i in range(0,100):
        list_name[i] = list_name[i].replace(e1,'').replace(e2,'')
    return list_name


# In[122]:


remove_brackets(movie_year1,'(',')')


# In[148]:


movie_title


# In[153]:


movie_year1


# In[154]:


final_rating


# In[161]:


Movie_details = pd.DataFrame({})
Movie_details["Movie Name"] = movie_title
Movie_details["IMDb Rating"] = final_rating
Movie_details["Year of release"] = movie_year1


# In[162]:


Movie_details


# In[163]:


Movie_details.to_csv('IMDb Top 100 Movies.csv', index=False)


# In[ ]:




