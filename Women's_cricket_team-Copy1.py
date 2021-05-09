#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd


# In[2]:


page = requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
page


# In[3]:


soup = BeautifulSoup(page.content)


# In[4]:


team_name1 = soup.find_all('span',class_="u-hide-phablet")


# In[5]:


team_name1


# In[6]:


team_name2 = []
for i in team_name1:
    team_name2.append(i.text)
team_name2


# In[7]:


team_name2 =team_name2[0:10]


# In[8]:


team_name2


# In[9]:


team_matches = soup.find('td',class_="rankings-block__banner--matches")


# In[10]:


team_matches.text            #matches of number 1 team


# In[11]:


#points of number 1 team
point1 = soup.find('td',class_="rankings-block__banner--points")
point1


# In[12]:


point1.text


# In[13]:


team_matches1 = soup.find_all('td',class_="table-body__cell u-center-text")


# In[14]:


team_matches1                    #contains both matches and rating 


# In[15]:


#seperating extra tags
matches1 = []
for i in team_matches1:
    matches1.append(i.text)
matches1


# In[16]:


#separating team points and matches
matches2 = matches1[0:18:2]
points = matches1[1:18:2]


# In[18]:


matches2.insert(0,'18')


# In[20]:


matches2.remove('37')                       #total number of matches


# In[21]:


matches2


# In[22]:


points.insert(0,'2955')


# In[23]:


points                #points of all teams


# #### Ratings of teams

# In[24]:


#rating of team at number 1 position
rating1 = soup.find('td',class_= "rankings-block__banner--rating u-text-right")
rating1.text.replace('\n','').replace('                            ','')


# In[25]:


#rating of other teams
rating2 = soup.find_all('td',class_ = "table-body__cell u-text-right rating")
rating2


# In[26]:


#extracting ratings
ratings = []
for i in rating2:
    ratings.append(i.text)
ratings


# In[27]:


#adding all ratings together
ratings.insert(0,'164')


# In[28]:


ratings


# In[29]:


Woman_team = pd.DataFrame({})
Woman_team['Team Name'] = team_name2


# In[30]:


Woman_team['Matches'] = matches2
Woman_team['Points'] = points
Woman_team['Ratings'] = ratings


# In[32]:


Woman_team


# In[33]:


Woman_team.to_csv("Women's top 10 ODI Team.csv",index = False)


# ## WoMen's ODI Player Rankings(Batsman)

# In[34]:


page2 = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")
page2


# In[35]:


soup1 = BeautifulSoup(page2.content)


# In[36]:


# Batsman name
name1 = soup1.find_all('div', class_ = "rankings-block__banner--name")
name1


# In[37]:


#extracting only batsmen name
name2 = name1[0]
name2.text


# In[38]:


name3 = soup1.find_all('td',class_ ="table-body__cell name")
name3


# In[39]:


player_name = []
for i in name3:
    for j in i.find_all("a"):
        player_name.append(j.text)
player_name                                             #contains names of all player


# In[40]:


Batsman_name = player_name[0:9]


# In[41]:


Batsman_name


# In[42]:


Batsman_name.insert(0,name2.text)


# In[43]:


Batsman_name                     #contains names of all batsman


# In[44]:


#country name
country_name = soup1.find_all('span', class_ = "table-body__logo-text")
country_name


# In[45]:


def extract(category,class_name,main_matrics):
    matrix_name = soup1.find_all(category, class_ = class_name)
    for i in matrix_name:
        main_matrics.append(i.text)
    return main_matrics


# In[46]:


country_name1 = []
country_name_sorted = []
extract('span',"table-body__logo-text",country_name1)


# In[47]:


country_name1


# In[48]:


country_name = country_name1[0:9]
country_name


# In[49]:


#extracting country name of number 1 player
country_name2 = soup1.find('div', class_ ="rankings-block__banner--nationality")
country_name2.text


# In[50]:


c2=country_name2.text.replace('\n','').replace('                            ','').replace('765','')
c2


# In[51]:


country_name.insert(0,c2) 


# In[52]:


country_name                                #all the countries extracted


# In[53]:


#Ratings of the player


# In[54]:


#rating of number first player.
ratings1 = soup1.find('div', class_ ="rankings-block__banner--rating")
rat1 =ratings1.text
rat1                                   


# In[55]:


#ratings of other players
ratings2 = []
extract('td',"table-body__cell u-text-right rating",ratings2)


# In[56]:


#extracting top ten ratings
ratings = ratings2[0:9]
ratings


# In[57]:


#combining all ratings
ratings.insert(0,rat1)


# In[58]:


ratings


# In[59]:


#extracting rankings


# In[60]:


#ranking of number 1 player
rank1 = soup1.find('div',class_ = "rankings-block__banner--pos")
rank2=rank1.text.replace('This player has moved up in the rankings since the previous rankings update','').replace('\n','').replace('                        ','').replace('        ','')


# In[61]:


rank2


# In[62]:


#extracting others rating
ranking1 = soup1.find_all('td',class_ ="table-body__cell table-body__cell--position u-text-right")


# In[63]:


ranking2 = []
for i in ranking1:
    ranking2.append(i.text)
ranking2[0].replace('This player has moved down in the rankings since the previous rankings update\n\n','')


# In[64]:


ranking3 = ranking2[0:9]


# In[65]:


ranking3


# In[66]:


for i in range(0,9):
    ranking3[i] = ranking3[i].replace('This player has moved down in the rankings since the previous rankings update','')


# In[67]:


ranking3


# In[68]:


def filterfunc(elem1,elem2):
    for i in range(0,9):
        ranking3[i] = ranking3[i].replace(elem1,elem2)


# In[69]:


filterfunc('This player has moved up in the rankings since the previous rankings update','')


# In[70]:


ranking3


# In[71]:


filterfunc('\n','')
ranking3


# In[72]:


filterfunc('                                    ','')
ranking3


# In[73]:


filterfunc('        ','')


# In[74]:


ranking3


# In[75]:


ranking3.insert(0,rank2)


# In[76]:


ranking3


# In[77]:


ranking = ranking3


# In[78]:


ranking


# In[79]:


#creating data frame for batsmen ranking


# In[80]:


Batsmen = pd.DataFrame({})
Batsmen["Rankings"] = ranking
Batsmen["Player Name"] = Batsman_name
Batsmen["Country"] = country_name
Batsmen["Ratings"] = ratings


# In[81]:


Batsmen


# ## Top bowlers

# In[82]:


#players Name


# In[83]:


#extracting only batsmen name
Bowlers_name1 = name1[1]
Bowlers_name1.text


# In[84]:


Bowlers_name = player_name[9:18]


# In[85]:


Bowlers_name


# In[86]:


Bowlers_name.insert(0,Bowlers_name1.text)


# In[87]:


Bowlers_name


# In[88]:


#bowlers name extracted


# In[89]:


#Bowlers Country


# In[90]:


bowlers_country1 = soup1.find_all('div', class_ ="rankings-block__banner--nationality")


# In[91]:


bowlers_count = []
for i in bowlers_country1:
    bowlers_count.append(i.text)
bowlers_count


# In[92]:


bowlers_count1 = bowlers_count[1]


# In[94]:


bowlers_count1=bowlers_count1.replace('\n','').replace('                            ','').replace('808','')
bowlers_count1


# In[95]:


Bowlers_country = country_name1[9:18]
Bowlers_country.insert(0,bowlers_count1)


# In[96]:


Bowlers_country


# In[97]:


#bowlers country extracted


# In[98]:


#Extracting bolwers rating


# In[99]:


bowlers_ratings = ratings2[9:18]
bowlers_ratings


# In[114]:


bowlers_rating1 = soup1.find_all('div', class_ ="rankings-block__banner--rating")
bowlers_rat2 = []
for i in bowlers_rating1:
    bowlers_rat2.append(i.text)
bowlers_rat2


# In[115]:


bowlers_rat2 = bowlers_rat2[1]
bowlers_rat2


# In[116]:


bowlers_rat2


# In[117]:


bowlers_ratings.insert(0,bowlers_rat2)


# In[121]:


bowlers_ratings.remove('765')


# In[122]:


bowlers_ratings


# In[123]:


#bowlers rating extracted


# In[124]:


#bowlers ranking


# In[125]:


#ranking of number 1 bowler
rank1_bowler = soup1.find('div',class_ = "rankings-block__banner--pos")
rank2_bowler=rank1_bowler.text.replace('This player has moved up in the rankings since the previous rankings update','').replace('\n','').replace('                        ','').replace('        ','')


# In[126]:


rank2_bowler


# In[127]:


ranking2_bowler = []
for i in ranking1:
    ranking2_bowler.append(i.text)
ranking2_bowler[9:18]


# In[128]:


ranking_bowler = ranking2_bowler[9:18]


# In[129]:


ranking_bowler


# In[130]:


def filterfunc(elem1,elem2):
    for i in range(0,9):
        ranking_bowler[i] = ranking_bowler[i].replace(elem1,elem2)


# In[131]:


filterfunc('This player has moved up in the rankings since the previous rankings update','')


# In[132]:


ranking_bowler


# In[133]:


filterfunc('This player has moved down in the rankings since the previous rankings update','')
ranking_bowler


# In[134]:


filterfunc('\n','')
ranking_bowler


# In[135]:


filterfunc('                                    ','')
filterfunc('        ','')


# In[136]:


ranking_bowler


# In[137]:


ranking_bowler.insert(0,rank2_bowler)


# In[138]:


ranking_bowler


# In[139]:


#creating dataframe for bowlers


# In[140]:


Bowler = pd.DataFrame({})
Bowler["Rankings"] = ranking_bowler
Bowler["Player Name"] = Bowlers_name
Bowler["Country"] = Bowlers_country
Bowler["Ratings"] = bowlers_ratings


# In[141]:


Bowler


# In[ ]:




