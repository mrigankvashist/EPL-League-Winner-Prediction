"""### Part 2-Week wise prediction"""
import pandas as pd
import numpy as np 

data=pd.read_csv('/Users/KillSwitch/Downloads/footy 2/full_data.csv') #Loading the complete data we created in part 1

data=data.loc[:,['MW','HomeTeam','AwayTeam','HTGS','ATGS','HTGC','ATGC','HTP','ATP','HTFormPts','ATFormPts']] #selecting the columns that are needed

data['Year']=(2004 + (data.index / 380 + 1)).astype(int) #To get year when the match was played. Every season has 380 matches, we start from EPL 2005.

home=data.loc[:,['Year','MW','HomeTeam','HTGS','HTGC','HTP','HTFormPts']] #selecting columns relevant to home team
away=data.loc[:,['Year','MW','AwayTeam','ATGS','ATGC','ATP','ATFormPts']] #selecting columns relevant to away team
home.columns=['Year','MW','Team','GS','GC','Points','FormPts'] #renaming for similarity of two datasets-home and away
away.columns=['Year','MW','Team','GS','GC','Points','FormPts']

data=pd.concat([home,away]).drop_duplicates().reset_index(drop=True)   #combining the data of home and away teams into one. Did this to have uniform naming of columns irrespective of match played at home/away

data=data.groupby(['Year','Team','MW']).sum().reset_index() #Grouping data by year, team and MW and summing it, this means every row of the dataset will look like this
# 2020, Chelsea, MW-10, GS (till 10th week), GC (till 10th week), Points(till 10th week), FormPts (for last 5 weeks)

data['Win']=0 #creating a column win to identify if the team won in a particular year or not. Initially it is set to 0.
for i in range(len(data)):
    if (data['Team'][i]=='Chelsea') & (data['Year'][i]==2005):   #Hard-coding, Chelsea won EPL in 2005 so against 2005, Chelsea, win value will be 1, all other teams will have 0. This will help model understand which team won which year and how it performed that year to win the league
        data['Win'][i]=1
    if (data['Team'][i]=='Man Utd') & (data['Year'][i]==2006):
        data['Win'][i]=1
    if (data['Team'][i]=='Man Utd') & (data['Year'][i]==2007):
        data['Win'][i]=1
    if (data['Team'][i]=='Man Utd') & (data['Year'][i]==2008):
        data['Win'][i]=1
    if (data['Team'][i]=='Chelsea') & (data['Year'][i]==2009):
        data['Win'][i]=1
    if (data['Team'][i]=='Man Utd') & (data['Year'][i]==2010):
        data['Win'][i]=1
    if (data['Team'][i]=='Man City') & (data['Year'][i]==2011):
        data['Win'][i]=1
    if (data['Team'][i]=='Man Utd') & (data['Year'][i]==2012):
        data['Win'][i]=1
    if (data['Team'][i]=='Man City') & (data['Year'][i]==2013):
        data['Win'][i]=1
    if (data['Team'][i]=='Chelsea') & (data['Year'][i]==2014):
        data['Win'][i]=1
    if (data['Team'][i]=='Leicester') & (data['Year'][i]==2015):
        data['Win'][i]=1
    if (data['Team'][i]=='Chelsea') & (data['Year'][i]==2016):
        data['Win'][i]=1
    if (data['Team'][i]=='Man City') & (data['Year'][i]==2017):
        data['Win'][i]=1
    if (data['Team'][i]=='Man City') & (data['Year'][i]==2018):
        data['Win'][i]=1
    if (data['Team'][i]=='Liverpool') & (data['Year'][i]==2019):
        data['Win'][i]=1
    if (data['Team'][i]=='Man City') & (data['Year'][i]==2020):
        data['Win'][i]=1

#We will one-hot encode the data now, i.e. convert team names into binary representation of 0 and 1.
data=pd.get_dummies(data,columns=['Team'])
data=data.drop(columns=['Year']) #Dropping the year column because it was only needed to mark which team won when, to predict who will win the league in a year, the year doesn't contribute, other features do
data.to_csv('epl_week.csv') #saving the file as epl_week. It gets saved in the main folder where this python script is saved



	


