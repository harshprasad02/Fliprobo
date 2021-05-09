#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[3]:


import pandas as pd
import numpy as np


# In[28]:


page = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
page


# In[29]:


soup = BeautifulSoup(page.content)


# In[30]:


titles1 = soup.find_all('td', class_ = 'titleColumn')


# In[31]:


titles1


# In[32]:


movie_title = []
for i in titles1:
    for j in i.find_all("a"):
        movie_title.append(j.text)
movie_title


# In[33]:


ratings = soup.find_all('strong')


# In[34]:


rating_of_movies = []
for i in ratings:
    rating_of_movies.append(i.text)
rating_of_movies


# In[35]:


year = soup.find_all('span',class_="secondaryInfo")


# In[36]:


movie_year1 = []
for i in year:
    movie_year1.append(i.text)
movie_year1 


# In[46]:


#extracting details pf top 100 movies only
movie_title100 = []
def top_movies(feature_name):
    for i in range(0,100):
        movie_title100.append(feature_name[i])
    return movie_title100


# In[44]:


movie_rating100 = []
def top_rating(feature_name):
    for i in range(0,100):
        movie_rating100.append(feature_name[i])
    return movie_rating100


# In[45]:


movie_year100 = []
def top_year(feature_name):
    for i in range(0,100):
        movie_year100.append(feature_name[i])
    return movie_year100


# In[47]:


top_movies(movie_title)


# In[48]:


top_rating(rating_of_movies)


# In[49]:


top_year(movie_year1)


# In[50]:


#removing extra brackets from year
def remove_brackets(list_name,e1,e2):
    for i in range(0,100):
        list_name[i] = list_name[i].replace(e1,'').replace(e2,'')
    return list_name


# In[51]:


remove_brackets(movie_year100,'(',')')


# In[52]:


#storing data in data frame


# In[57]:


Movie_details = pd.DataFrame({})
Movie_details["Movie Name"] = movie_title100
Movie_details["IMDb Rating"] = movie_rating100
Movie_details["Year of release"] = movie_year100


# In[58]:


Movie_details


# In[59]:


Movie_details.to_csv('Indian Top 100 Movies.csv', index=False)


# In[ ]:




