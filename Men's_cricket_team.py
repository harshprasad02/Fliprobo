#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd


# In[320]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
page


# In[321]:


soup = BeautifulSoup(page.content)


# In[322]:


team_name1 = soup.find_all('span',class_="u-hide-phablet")


# In[323]:


team_name1


# In[324]:


team_name2 = []
for i in team_name1:
    team_name2.append(i.text)
team_name2


# In[325]:


team_name2 =team_name2[0:10]


# In[326]:


team_name2


# In[327]:


team_matches = soup.find('td',class_="rankings-block__banner--matches")


# In[328]:


team_matches.text            #matches of number 1 team


# In[329]:


#points of number 1 team
point1 = soup.find('td',class_="rankings-block__banner--points")
point1


# In[330]:


point1.text


# In[331]:


team_matches1 = soup.find_all('td',class_="table-body__cell u-center-text")


# In[332]:


team_matches1                    #contains both matches and rating 


# In[333]:


#seperating extra tags
matches1 = []
for i in team_matches1:
    matches1.append(i.text)
matches1


# In[334]:


#separating team points and matches
matches2 = matches1[0:18:2]
points = matches1[1:18:2]


# In[335]:


matches2.insert(0,'37')


# In[336]:


matches2                       #total number of matches


# In[337]:


points.insert(0,'4,455')


# In[338]:


points                #points of all teams


# #### Ratings of teams

# In[339]:


#rating of team at number 1 position
rating1 = soup.find('td',class_= "rankings-block__banner--rating u-text-right")
rating1.text.replace('\n','').replace('                            ','')


# In[340]:


#rating of other teams
rating2 = soup.find_all('td',class_ = "table-body__cell u-text-right rating")
rating2


# In[341]:


#extracting ratings
ratings = []
for i in rating2:
    ratings.append(i.text)
ratings


# In[345]:


#adding all ratings together
ratings.insert(0,'121')


# In[ ]:





# In[350]:


ratings1 = ratings[0:10]


# In[351]:


ratings1


# In[353]:


Mens_team = pd.DataFrame({})
Mens_team['Team Name'] = team_name2


# In[354]:


Mens_team['Matches'] = matches2
Mens_team['Points'] = points
Mens_team['Ratings'] = ratings1


# In[355]:


Mens_team


# In[356]:


Mens_team.to_csv("Men's top 10 ODI Team.csv",index = False)


# ## Men's ODI Player Rankings(Batsman)

# In[142]:


page2 = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")
page2


# In[143]:


soup1 = BeautifulSoup(page2.content)


# In[144]:


# Batsman name
name1 = soup1.find_all('div', class_ = "rankings-block__banner--name")
name1


# In[145]:


#extracting only batsmen name
name2 = name1[0]
name2.text


# In[113]:


name3 = soup1.find_all('td',class_ ="table-body__cell name")
name3


# In[114]:


player_name = []
for i in name3:
    for j in i.find_all("a"):
        player_name.append(j.text)
player_name                                             #contains names of all player


# In[120]:


Batsman_name = player_name[0:9]


# In[121]:


Batsman_name


# In[122]:


Batsman_name.insert(0,'Babar Azam')


# In[123]:


Batsman_name                     #contains names of all batsman


# In[151]:


#country name
country_name = soup1.find_all('span', class_ = "table-body__logo-text")
country_name


# In[158]:


def extract(category,class_name,main_matrics):
    matrix_name = soup1.find_all(category, class_ = class_name)
    for i in matrix_name:
        main_matrics.append(i.text)
    return main_matrics


# In[159]:


country_name1 = []
country_name_sorted = []
extract('span',"table-body__logo-text",country_name1)


# In[160]:


country_name1


# In[161]:


country_name = country_name1[0:9]
country_name


# In[164]:


#extracting country name of number 1 player
country_name2 = soup1.find('div', class_ ="rankings-block__banner--nationality")
country_name2.text


# In[167]:


c2=country_name2.text.replace('\n','').replace('                            ','').replace('865','')
c2


# In[168]:


country_name.insert(0,c2) 


# In[169]:


country_name                                #all the countries extracted


# In[170]:


#Ratings of the player


# In[205]:


#rating of number first player.
ratings1 = soup1.find('div', class_ ="rankings-block__banner--rating")
rat1 =ratings1.text
rat1                                   


# In[174]:


#ratings of other players
ratings2 = []
extract('td',"table-body__cell u-text-right rating",ratings2)


# In[178]:


#extracting top ten ratings
ratings = ratings2[0:9]
ratings


# In[179]:


#combining all ratings
ratings.insert(0,rat1)


# In[180]:


ratings


# In[181]:


#extracting rankings


# In[188]:


#ranking of number 1 player
rank1 = soup1.find('div',class_ = "rankings-block__banner--pos")
rank2=rank1.text.replace('This player has moved up in the rankings since the previous rankings update','').replace('\n','').replace('                        ','').replace('        ','')


# In[189]:


rank2


# In[204]:


#extracting others rating
ranking1 = soup1.find_all('td',class_ ="table-body__cell table-body__cell--position u-text-right")


# In[215]:


ranking2 = []
for i in ranking1:
    ranking2.append(i.text)
ranking2[0].replace('This player has moved down in the rankings since the previous rankings update\n\n','')


# In[218]:


ranking3 = ranking2[0:9]


# In[219]:


ranking3


# In[221]:


for i in range(0,9):
    ranking3[i] = ranking3[i].replace('This player has moved down in the rankings since the previous rankings update','')


# In[222]:


ranking3


# In[223]:


def filterfunc(elem1,elem2):
    for i in range(0,9):
        ranking3[i] = ranking3[i].replace(elem1,elem2)


# In[224]:


filterfunc('This player has moved up in the rankings since the previous rankings update','')


# In[226]:


ranking3


# In[228]:


filterfunc('\n','')
ranking3


# In[229]:


filterfunc('                                    ','')
ranking3


# In[230]:


filterfunc('        ','')


# In[231]:


ranking3


# In[246]:


ranking3[6] = '8'


# In[247]:


ranking3[8] = '10'


# In[248]:


ranking3


# In[256]:


ranking3.insert(0,rank2)


# In[257]:


ranking3


# In[259]:


ranking = ranking3


# In[261]:


ranking.remove('1')


# In[262]:


ranking


# In[264]:


#creating data frame for batsmen ranking


# In[265]:


Batsmen = pd.DataFrame({})
Batsmen["Rankings"] = ranking
Batsmen["Player Name"] = Batsman_name
Batsmen["Country"] = country_name
Batsmen["Ratings"] = ratings


# In[266]:


Batsmen


# ## Top bowlers

# In[267]:


#players Name


# In[269]:


#extracting only batsmen name
Bowlers_name1 = name1[1]
Bowlers_name1.text


# In[272]:


Bowlers_name = player_name[9:18]


# In[273]:


Bowlers_name


# In[274]:


Bowlers_name.insert(0,Bowlers_name1.text)


# In[275]:


Bowlers_name


# In[276]:


#bowlers name extracted


# In[277]:


#Bowlers Country


# In[284]:


bowlers_country1 = soup1.find_all('div', class_ ="rankings-block__banner--nationality")


# In[285]:


bowlers_count = []
for i in bowlers_country1:
    bowlers_count.append(i.text)
bowlers_count


# In[286]:


bowlers_count1 = bowlers_count[1]


# In[288]:


bowlers_count1=bowlers_count1.replace('\n','').replace('                            ','').replace('737','')
bowlers_count1


# In[289]:


Bowlers_country = country_name1[9:18]
Bowlers_country.insert(0,bowlers_count1)


# In[290]:


Bowlers_country


# In[291]:


#bowlers country extracted


# In[292]:


#Extracting bolwers rating


# In[293]:


bowlers_ratings = ratings2[9:18]
bowlers_ratings


# In[295]:


bowlers_rating1 = soup1.find_all('div', class_ ="rankings-block__banner--rating")
bowlers_rat = []
for i in bowlers_rating1:
    bowlers_rat.append(i.text)
bowlers_rat


# In[296]:


bowlers_rat1 = bowlers_rat[1]
bowlers_rat1


# In[297]:


bowlers_ratings.insert(0,bowlers_rat1)


# In[298]:


bowlers_ratings


# In[299]:


#bowlers rating extracted


# In[300]:


#bowlers ranking


# In[302]:


#ranking of number 1 bowler
rank1_bowler = soup1.find('div',class_ = "rankings-block__banner--pos")
rank2_bowler=rank1_bowler.text.replace('This player has moved up in the rankings since the previous rankings update','').replace('\n','').replace('                        ','').replace('        ','')


# In[303]:


rank2_bowler


# In[304]:


ranking2_bowler = []
for i in ranking1:
    ranking2_bowler.append(i.text)
ranking2_bowler[9:18]


# In[305]:


ranking_bowler = ranking2_bowler[9:18]


# In[306]:


ranking_bowler


# In[307]:


def filterfunc(elem1,elem2):
    for i in range(0,9):
        ranking_bowler[i] = ranking_bowler[i].replace(elem1,elem2)


# In[308]:


filterfunc('This player has moved up in the rankings since the previous rankings update','')


# In[309]:


ranking_bowler


# In[311]:


filterfunc('This player has moved down in the rankings since the previous rankings update','')
ranking_bowler


# In[312]:


filterfunc('\n','')
ranking_bowler


# In[313]:


filterfunc('                                    ','')
filterfunc('        ','')


# In[314]:


ranking_bowler


# In[315]:


ranking_bowler.insert(0,rank2_bowler)


# In[316]:


ranking_bowler


# In[317]:


#creating dataframe for bowlers


# In[318]:


Bowler = pd.DataFrame({})
Bowler["Rankings"] = ranking_bowler
Bowler["Player Name"] = Bowlers_name
Bowler["Country"] = Bowlers_country
Bowler["Ratings"] = bowlers_ratings


# In[319]:


Bowler


# In[ ]:




