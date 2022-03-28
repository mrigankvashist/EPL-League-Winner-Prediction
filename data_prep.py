
### Part I of the project

# Import all the necessary libraries

import numpy as np
import pandas as pd
from datetime import datetime as dt
import itertools


# Read data from the CSV into a dataframe, We have taken data for 2005-20 from http://football-data.co.uk
#We are reading the 16 files here

loc = "/content/drive/MyDrive/footy/" #location of the folder where all files are, I have uploaded it on my drive for easy access

raw_data_1 = pd.read_csv(loc + 'E0.csv') #2005, name of file is E0.csv
raw_data_2 = pd.read_csv(loc + 'E0-2.csv') 
raw_data_3 = pd.read_csv(loc + 'E0-3.csv')
raw_data_4 = pd.read_csv(loc + 'E0-4.csv')
raw_data_5 = pd.read_csv(loc + 'E0-5.csv')
raw_data_6 = pd.read_csv(loc + 'E0-6.csv')
raw_data_7 = pd.read_csv(loc + 'E0-7.csv')
raw_data_8 = pd.read_csv(loc + 'E0-8.csv')
raw_data_9 = pd.read_csv(loc + 'E0-9.csv')
raw_data_10 = pd.read_csv(loc + 'E0-10.csv')
raw_data_11 = pd.read_csv(loc + 'E0-11.csv')
raw_data_12 = pd.read_csv(loc + 'E0-12.csv')
raw_data_13 = pd.read_csv(loc + 'E0-13.csv')
raw_data_14 = pd.read_csv(loc + 'E0-14.csv')
raw_data_15 = pd.read_csv(loc + 'E0-15.csv')
raw_data_16 = pd.read_csv(loc + 'E0-16.csv') #2020

for i in range(len(raw_data_10)):                   #For one year, the format of date was not like other
    raw_data_10['Date'][i]=str(raw_data_10['Date'][i]) #changing the format like for others

raw_data_10=raw_data_10.iloc[:-1,:]   # Removing last row because it was empty for this file

def parse_date(date):  #this is a  function to get dates into standard format of DDMMYYYY
    if date == '':
        return None
    else:
        return dt.strptime(date, '%d/%m/%y').date()
    

def parse_date_other(date): #this is also the same date function but some dates are given like 20-02-21 and some like 20-02-2021 so separate functions to handle the,
    if date == '':
        return None
    else:
        return dt.strptime(date, '%d/%m/%Y').date()

# Parse data as time- here we apply above functions so that the datatype of date column is Date and not string

raw_data_1.Date = raw_data_1.Date.apply(parse_date)    
raw_data_2.Date = raw_data_2.Date.apply(parse_date)    
raw_data_3.Date = raw_data_3.Date.apply(parse_date)         
raw_data_4.Date = raw_data_4.Date.apply(parse_date)    
raw_data_5.Date = raw_data_5.Date.apply(parse_date)    
raw_data_6.Date = raw_data_6.Date.apply(parse_date)    
raw_data_7.Date = raw_data_7.Date.apply(parse_date)    
raw_data_8.Date = raw_data_8.Date.apply(parse_date)    
raw_data_9.Date = raw_data_9.Date.apply(parse_date)    
raw_data_10.Date = raw_data_10.Date.apply(parse_date)
raw_data_11.Date = raw_data_11.Date.apply(parse_date_other)
raw_data_12.Date = raw_data_12.Date.apply(parse_date)
raw_data_13.Date = raw_data_13.Date.apply(parse_date_other)
raw_data_14.Date = raw_data_14.Date.apply(parse_date_other)
raw_data_15.Date = raw_data_15.Date.apply(parse_date_other)
raw_data_16.Date = raw_data_16.Date.apply(parse_date_other)

#Gets all the statistics related to gameplay
                      
columns_req = ['Date','HomeTeam','AwayTeam','HTHG','HTAG','FTR','FTHG','FTAG'] # we are only using these columns as input

#Now, we are keeping only needed columns from the whole data for every year
playing_statistics_1 = raw_data_1[columns_req]                      
playing_statistics_2 = raw_data_2[columns_req]
playing_statistics_3 = raw_data_3[columns_req]
playing_statistics_4 = raw_data_4[columns_req]
playing_statistics_5 = raw_data_5[columns_req]
playing_statistics_6 = raw_data_6[columns_req]
playing_statistics_7 = raw_data_7[columns_req]
playing_statistics_8 = raw_data_8[columns_req]
playing_statistics_9 = raw_data_9[columns_req]
playing_statistics_10 = raw_data_10[columns_req]
playing_statistics_11 = raw_data_11[columns_req]   
playing_statistics_12 = raw_data_12[columns_req]
playing_statistics_13 = raw_data_13[columns_req]
playing_statistics_14 = raw_data_14[columns_req]
playing_statistics_15 = raw_data_15[columns_req]
playing_statistics_16 = raw_data_16[columns_req]

# Gets the goals scored agg arranged by teams and matchweek
#This function gives total goals scored by a team in a MW, so in 2nd MW, it will have goals scored in 1st and 2nd week
def get_goals_scored(playing_stat):
    # Create a dictionary with team names as keys
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []
    
    # the value corresponding to keys is a list containing the match location.
    for i in range(len(playing_stat)):
        HTGS = playing_stat.iloc[i]['FTHG']
        ATGS = playing_stat.iloc[i]['FTAG']
        teams[playing_stat.iloc[i].HomeTeam].append(HTGS)
        teams[playing_stat.iloc[i].AwayTeam].append(ATGS)
    
    # Create a dataframe for goals scored where rows are teams and cols are matchweek.
    #Note 1,39 range means 38 matchweeks
    GoalsScored = pd.DataFrame(data=teams, index = [i for i in range(1,39)]).T
    GoalsScored[0] = 0
    # Aggregate to get uptil that point
    for i in range(2,39):
        GoalsScored[i] = GoalsScored[i] + GoalsScored[i-1]
    return GoalsScored



# Gets the goals conceded agg arranged by teams and matchweek
#Similar to last function, this gets the goals conceded
def get_goals_conceded(playing_stat):
    # Create a dictionary with team names as keys
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []
    
    # the value corresponding to keys is a list containing the match location.
    for i in range(len(playing_stat)):
        ATGC = playing_stat.iloc[i]['FTHG']
        HTGC = playing_stat.iloc[i]['FTAG']
        teams[playing_stat.iloc[i].HomeTeam].append(HTGC)
        teams[playing_stat.iloc[i].AwayTeam].append(ATGC)
    
    # Create a dataframe for goals scored where rows are teams and cols are matchweek.
    GoalsConceded = pd.DataFrame(data=teams, index = [i for i in range(1,39)]).T
    GoalsConceded[0] = 0
    # Aggregate to get uptil that point
    for i in range(2,39):
        GoalsConceded[i] = GoalsConceded[i] + GoalsConceded[i-1]
    return GoalsConceded

#This is a function which combines the above two functions and return the GS and GC by home and away teams in the MWs
def get_gss(playing_stat):
    GC = get_goals_conceded(playing_stat)
    GS = get_goals_scored(playing_stat)
   
    j = 0
    HTGS = []
    ATGS = []
    HTGC = []
    ATGC = []

    for i in range(380):
        ht = playing_stat.iloc[i].HomeTeam
        at = playing_stat.iloc[i].AwayTeam
        HTGS.append(GS.loc[ht][j])
        ATGS.append(GS.loc[at][j])
        HTGC.append(GC.loc[ht][j])
        ATGC.append(GC.loc[at][j])
        
        if ((i + 1)% 10) == 0:
            j = j + 1
        
    playing_stat['HTGS'] = HTGS
    playing_stat['ATGS'] = ATGS
    playing_stat['HTGC'] = HTGC
    playing_stat['ATGC'] = ATGC
    
    return playing_stat

# Applyinf the above function to each dataset
playing_statistics_1 = get_gss(playing_statistics_1)
playing_statistics_2 = get_gss(playing_statistics_2)
playing_statistics_3 = get_gss(playing_statistics_3)
playing_statistics_4 = get_gss(playing_statistics_4)
playing_statistics_5 = get_gss(playing_statistics_5)
playing_statistics_6 = get_gss(playing_statistics_6)
playing_statistics_7 = get_gss(playing_statistics_7)
playing_statistics_8 = get_gss(playing_statistics_8)
playing_statistics_9 = get_gss(playing_statistics_9)
playing_statistics_10 = get_gss(playing_statistics_10)
playing_statistics_11 = get_gss(playing_statistics_11)
playing_statistics_12 = get_gss(playing_statistics_12)
playing_statistics_13 = get_gss(playing_statistics_13)
playing_statistics_14 = get_gss(playing_statistics_14)
playing_statistics_15 = get_gss(playing_statistics_15)
playing_statistics_16 = get_gss(playing_statistics_16)

#we use this function to calculate points of a team for every match
def get_points(result):
    if result == 'W':
        return 3
    elif result == 'D':
        return 1
    else:
        return 0
    
#Now we cummulate the points of every team for every MW
def get_cuml_points(matchres):
    matchres_points = matchres.applymap(get_points)
    for i in range(2,39):
        matchres_points[i] = matchres_points[i] + matchres_points[i-1]
        
    matchres_points.insert(column =0, loc = 0, value = [0*i for i in range(20)])
    return matchres_points

# This function creates a column with result of match, i.e. if Home Team won,it will show W for it and L for away team or D for both. We do this for all matchweeks.
def get_matchres(playing_stat):
    # Create a dictionary with team names as keys
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []

    # the value corresponding to keys is a list containing the match result
    for i in range(len(playing_stat)):
        if playing_stat.iloc[i].FTR == 'H':
            teams[playing_stat.iloc[i].HomeTeam].append('W')
            teams[playing_stat.iloc[i].AwayTeam].append('L')
        elif playing_stat.iloc[i].FTR == 'A':
            teams[playing_stat.iloc[i].AwayTeam].append('W')
            teams[playing_stat.iloc[i].HomeTeam].append('L')
        else:
            teams[playing_stat.iloc[i].AwayTeam].append('D')
            teams[playing_stat.iloc[i].HomeTeam].append('D')
            
    return pd.DataFrame(data=teams, index = [i for i in range(1,39)]).T

#Now using the result and points functions, we calculate the final points at end of MW for every team
def get_agg_points(playing_stat):
    matchres = get_matchres(playing_stat)
    cum_pts = get_cuml_points(matchres)
    HTP = []
    ATP = []
    j = 0
    for i in range(380):
        ht = playing_stat.iloc[i].HomeTeam
        at = playing_stat.iloc[i].AwayTeam
        HTP.append(cum_pts.loc[ht][j])
        ATP.append(cum_pts.loc[at][j])

        if ((i + 1)% 10) == 0:
            j = j + 1
            
    playing_stat['HTP'] = HTP
    playing_stat['ATP'] = ATP
    return playing_stat

# Apply to each dataset
playing_statistics_1 = get_agg_points(playing_statistics_1)
playing_statistics_2 = get_agg_points(playing_statistics_2)
playing_statistics_3 = get_agg_points(playing_statistics_3)
playing_statistics_4 = get_agg_points(playing_statistics_4)
playing_statistics_5 = get_agg_points(playing_statistics_5)
playing_statistics_6 = get_agg_points(playing_statistics_6)
playing_statistics_7 = get_agg_points(playing_statistics_7)
playing_statistics_8 = get_agg_points(playing_statistics_8)
playing_statistics_9 = get_agg_points(playing_statistics_9)
playing_statistics_10 = get_agg_points(playing_statistics_10)
playing_statistics_11 = get_agg_points(playing_statistics_11)
playing_statistics_12 = get_agg_points(playing_statistics_12)
playing_statistics_13 = get_agg_points(playing_statistics_13)
playing_statistics_14 = get_agg_points(playing_statistics_14)
playing_statistics_15 = get_agg_points(playing_statistics_15)
playing_statistics_16 = get_agg_points(playing_statistics_16)

#This function gets the form as per previous matches, this function is used below for other functions
def get_form(playing_stat,num):
    form = get_matchres(playing_stat)
    form_final = form.copy()
    for i in range(num,39):
        form_final[i] = ''
        j = 0
        while j < num:
            form_final[i] += form[i-j]
            j += 1           
    return form_final
# Adding the forw for num of weeks you want to consider
def add_form(playing_stat,num):
    form = get_form(playing_stat,num)
    h = ['M' for i in range(num * 10)] # if you are considering form for last weeks and in the 3rd MW you don't have results of previous years. It will show MM123, where 123 is W/L/D depending on result of last 3 MWs
    a = ['M' for i in range(num * 10)]
    
    j = num
    for i in range((num*10),380):
        ht = playing_stat.iloc[i].HomeTeam
        at = playing_stat.iloc[i].AwayTeam
        
        past = form.loc[ht][j]
        h.append(past[num-1])
        
        past = form.loc[at][j]
        a.append(past[num-1])
        
        if ((i + 1)% 10) == 0:
            j = j + 1

    playing_stat['HM' + str(num)] = h                 #this creates a column called HM1,HM2,HM3,HM4,HM5 which will have form of home team
    playing_stat['AM' + str(num)] = a #this does the same for away team

    
    return playing_stat


def add_form_df(playing_statistics): #using this function we are considering form of 5 weeks
    playing_statistics = add_form(playing_statistics,1)
    playing_statistics = add_form(playing_statistics,2)
    playing_statistics = add_form(playing_statistics,3)
    playing_statistics = add_form(playing_statistics,4)
    playing_statistics = add_form(playing_statistics,5)
    return playing_statistics

#Applying form function to all
playing_statistics_1 = add_form_df(playing_statistics_1)
playing_statistics_2 = add_form_df(playing_statistics_2)
playing_statistics_3 = add_form_df(playing_statistics_3)
playing_statistics_4 = add_form_df(playing_statistics_4)
playing_statistics_5 = add_form_df(playing_statistics_5)
playing_statistics_6 = add_form_df(playing_statistics_6)
playing_statistics_7 = add_form_df(playing_statistics_7)
playing_statistics_8 = add_form_df(playing_statistics_8)
playing_statistics_9 = add_form_df(playing_statistics_9)
playing_statistics_10 = add_form_df(playing_statistics_10)
playing_statistics_11 = add_form_df(playing_statistics_11)
playing_statistics_12 = add_form_df(playing_statistics_12)
playing_statistics_13 = add_form_df(playing_statistics_13)
playing_statistics_14 = add_form_df(playing_statistics_14)
playing_statistics_15 = add_form_df(playing_statistics_15)    
playing_statistics_16 = add_form_df(playing_statistics_16)

# Rearranging columns such taht we have input columns first and calculated columns later
cols = ['Date', 'HomeTeam', 'AwayTeam', 'HTHG','HTAG','FTHG', 'FTAG', 'FTR', 'HTGS', 'ATGS', 'HTGC', 'ATGC', 'HTP', 'ATP', 'HM1', 'HM2', 'HM3',
        'HM4', 'HM5', 'AM1', 'AM2', 'AM3', 'AM4', 'AM5' ]
#Applying re-arranging to all datasets
playing_statistics_1 = playing_statistics_1[cols]
playing_statistics_2 = playing_statistics_2[cols]
playing_statistics_3 = playing_statistics_3[cols]
playing_statistics_4 = playing_statistics_4[cols]
playing_statistics_5 = playing_statistics_5[cols]
playing_statistics_6 = playing_statistics_6[cols]
playing_statistics_7 = playing_statistics_7[cols]
playing_statistics_8 = playing_statistics_8[cols]
playing_statistics_9 = playing_statistics_9[cols]
playing_statistics_10 = playing_statistics_10[cols]
playing_statistics_11 = playing_statistics_11[cols]
playing_statistics_12 = playing_statistics_12[cols]
playing_statistics_13 = playing_statistics_13[cols]
playing_statistics_14 = playing_statistics_14[cols]
playing_statistics_15 = playing_statistics_15[cols]
playing_statistics_16 = playing_statistics_16[cols]

#We have a dataset created called eplstandings which have leaderboard positions of last year
Standings = pd.read_csv("/content/eplstandings.csv") #use location of where the file is in the computer
Standings.set_index(['Team'], inplace=True) #Each row is for 1 team and each column is a year
Standings = Standings.fillna(0) #If a team didn't play in a particular year, the position is 0

def get_last(playing_stat, Standings, year): #using this function to extract the leaderboard position of home and away team from the Standings file
    HomeTeamLP = []
    AwayTeamLP = []
    for i in range(380):
        ht = playing_stat.iloc[i].HomeTeam
        at = playing_stat.iloc[i].AwayTeam
        HomeTeamLP.append(Standings.loc[ht][year])
        AwayTeamLP.append(Standings.loc[at][year])
    playing_stat['HomeTeamLP'] = HomeTeamLP
    playing_stat['AwayTeamLP'] = AwayTeamLP
    return playing_stat

#Applying the function to all datasets, here 1 suggests results for EPL 2020, 2 is for EPL 2019, basically column numbers as per our Standings file
playing_statistics_1 = get_last(playing_statistics_1, Standings, 16)
playing_statistics_2 = get_last(playing_statistics_2, Standings, 15)
playing_statistics_3 = get_last(playing_statistics_3, Standings, 14)
playing_statistics_4 = get_last(playing_statistics_4, Standings, 13)
playing_statistics_5 = get_last(playing_statistics_5, Standings, 12)
playing_statistics_6 = get_last(playing_statistics_6, Standings, 11)
playing_statistics_7 = get_last(playing_statistics_7, Standings, 10)
playing_statistics_8 = get_last(playing_statistics_8, Standings, 9)
playing_statistics_9 = get_last(playing_statistics_9, Standings, 8)
playing_statistics_10 = get_last(playing_statistics_10, Standings, 7)
playing_statistics_11 = get_last(playing_statistics_11, Standings, 6)
playing_statistics_12 = get_last(playing_statistics_12, Standings, 5)
playing_statistics_13 = get_last(playing_statistics_13, Standings, 4)
playing_statistics_14 = get_last(playing_statistics_14, Standings, 3)
playing_statistics_15 = get_last(playing_statistics_15, Standings, 2)
playing_statistics_16 = get_last(playing_statistics_16, Standings, 1)

#Function to get the matchweek. As our data is in order, first 10 matches are for MW1, next 10 for MW2,and so on
def get_mw(playing_stat):
    j = 1
    MatchWeek = []
    for i in range(380):
        MatchWeek.append(j)
        if ((i + 1)% 10) == 0:
            j = j + 1
    playing_stat['MW'] = MatchWeek
    return playing_stat

#Getting MW for every match for every year
playing_statistics_1 = get_mw(playing_statistics_1)
playing_statistics_2 = get_mw(playing_statistics_2)
playing_statistics_3 = get_mw(playing_statistics_3)
playing_statistics_4 = get_mw(playing_statistics_4)
playing_statistics_5 = get_mw(playing_statistics_5)
playing_statistics_6 = get_mw(playing_statistics_6)
playing_statistics_7 = get_mw(playing_statistics_7)
playing_statistics_8 = get_mw(playing_statistics_8)
playing_statistics_9 = get_mw(playing_statistics_9)
playing_statistics_10 = get_mw(playing_statistics_10)
playing_statistics_11 = get_mw(playing_statistics_11)
playing_statistics_12 = get_mw(playing_statistics_12)
playing_statistics_13 = get_mw(playing_statistics_13)
playing_statistics_14 = get_mw(playing_statistics_14)
playing_statistics_15 = get_mw(playing_statistics_15)
playing_statistics_16 = get_mw(playing_statistics_16)

#Combining the data of 16 years into one dataset
playing_stat = pd.concat([playing_statistics_1,
                          playing_statistics_2,
                          playing_statistics_3,
                          playing_statistics_4,
                          playing_statistics_5,
                          playing_statistics_6,
                          playing_statistics_7,
                          playing_statistics_8,
                          playing_statistics_9,
                          playing_statistics_10,
                          playing_statistics_11,
                          playing_statistics_12,
                          playing_statistics_13,
                          playing_statistics_14,
                          playing_statistics_15,
                          playing_statistics_16], ignore_index=True)


# Gets the form points: WL would be given 3-0=3 points, WW= 3+3=6, etc
def get_form_points(string):
    sum = 0
    for letter in string:
        sum += get_points(letter)
    return sum

#Combining form results of last 5 weeks for every team to get the form points
playing_stat['HTFormPtsStr'] = playing_stat['HM1'] + playing_stat['HM2'] + playing_stat['HM3'] + playing_stat['HM4'] + playing_stat['HM5']
playing_stat['ATFormPtsStr'] = playing_stat['AM1'] + playing_stat['AM2'] + playing_stat['AM3'] + playing_stat['AM4'] + playing_stat['AM5']

#Applying form points function
playing_stat['HTFormPts'] = playing_stat['HTFormPtsStr'].apply(get_form_points)
playing_stat['ATFormPts'] = playing_stat['ATFormPtsStr'].apply(get_form_points)

# Identify Win/Loss Streaks if any.
def get_3game_ws(string):
    if string[-3:] == 'WWW':
        return 1
    else:
        return 0
    
def get_5game_ws(string):
    if string == 'WWWWW':
        return 1
    else:
        return 0
    
def get_3game_ls(string):
    if string[-3:] == 'LLL':
        return 1
    else:
        return 0
    
def get_5game_ls(string):
    if string == 'LLLLL':
        return 1
    else:
        return 0

#Adding winning and losing streak columns for both Home and Away teams. The value in the column would be 1 if there is a streak, else 0
playing_stat['HTWinStreak3'] = playing_stat['HTFormPtsStr'].apply(get_3game_ws)
playing_stat['HTWinStreak5'] = playing_stat['HTFormPtsStr'].apply(get_5game_ws)
playing_stat['HTLossStreak3'] = playing_stat['HTFormPtsStr'].apply(get_3game_ls)
playing_stat['HTLossStreak5'] = playing_stat['HTFormPtsStr'].apply(get_5game_ls)

playing_stat['ATWinStreak3'] = playing_stat['ATFormPtsStr'].apply(get_3game_ws)
playing_stat['ATWinStreak5'] = playing_stat['ATFormPtsStr'].apply(get_5game_ws)
playing_stat['ATLossStreak3'] = playing_stat['ATFormPtsStr'].apply(get_3game_ls)
playing_stat['ATLossStreak5'] = playing_stat['ATFormPtsStr'].apply(get_5game_ls)

# Get Goal Difference
playing_stat['HTGD'] = playing_stat['HTGS'] - playing_stat['HTGC']
playing_stat['ATGD'] = playing_stat['ATGS'] - playing_stat['ATGC']

# Diff in points
playing_stat['DiffPts'] = playing_stat['HTP'] - playing_stat['ATP']
playing_stat['DiffFormPts'] = playing_stat['HTFormPts'] - playing_stat['ATFormPts']

# Diff in last year positions
playing_stat['DiffLP'] = playing_stat['HomeTeamLP'] - playing_stat['AwayTeamLP']

# Scale DiffPts , DiffFormPts, HTGD, ATGD by Matchweek. Scaling is important for machine to understand the differences in rnages
cols = ['HTGD','ATGD','DiffPts','DiffFormPts','HTP','ATP']
playing_stat.MW = playing_stat.MW.astype(float) #converting MW column to float datatype

for col in cols: #dividing the columns to be scaled with the MW to have a standard value in 0 to 1 range
    playing_stat[col] = playing_stat[col] / playing_stat.MW

playing_stat.to_csv('full_data.csv') #Saving our data as an excel file for further operations

data=pd.read_csv('/content/full_data.csv') #Reading the full data, put location of the file in ''

data = data[data.MW > 3] # Remove first 3 matchweeks because it doesn't contribute much to results
data.drop(['Unnamed: 0','Date','HM4','HM5','AM4','AM5','HTFormPtsStr','ATFormPtsStr','MW','FTHG','FTAG'],1,inplace=True) #Dropping

# Separate into feature set and target variable
X_all = data.drop(['FTR'],1) #All other columns except FTR
y_all = data['FTR'] #Result is the column we have to predict

# Standardising the data.
from sklearn.preprocessing import scale

#necessary columns
cols =  ['HTHG', 'HTAG', 'HTGS', 'ATGS', 'HTGC','ATGC', 'HTP', 'ATP',
         'HomeTeamLP', 'AwayTeamLP', 'HTFormPts', 'ATFormPts', 'HTWinStreak3',
         'HTWinStreak5', 'HTGD', 'ATGD',
         'DiffPts', 'DiffFormPts', 'DiffLP']

#select the columns from data
for col in cols:
    X_all[col] = scale(X_all[col])

#converting data types of these columns
X_all.HM1 = X_all.HM1.astype('str')
X_all.HM2 = X_all.HM2.astype('str')
X_all.HM3 = X_all.HM3.astype('str')
X_all.AM1 = X_all.AM1.astype('str')
X_all.AM2 = X_all.AM2.astype('str')
X_all.AM3 = X_all.AM3.astype('str')

#preprocessing for One Hot encoding- a matrix of 20x20 where every row is for a team in the form of 1s and 0s
def preprocess_features(X):
    ''' Preprocesses the football data and converts catagorical variables into dummy variables. '''
    
    # Initialize new output DataFrame
    output = pd.DataFrame(index = X.index)
    
    # Investigate each feature column for the data
    for col, col_data in X.iteritems():
        
        # If data type is categorical, convert to dummy variables
        if col_data.dtype == object:
            col_data = pd.get_dummies(col_data, prefix = col)
        
        # Collect the revised columns
        output = output.join(col_data)
    
    return output

#Saving the proprocessed data as X_all
X_all = preprocess_features(X_all)

from sklearn.model_selection import train_test_split, cross_val_score

# Shuffle and split the dataset into training and testing set.
X_train= X_all.iloc[:-20,:]
X_test=X_all.iloc[-20:,:]
y_train=y_all[:-20]
y_test=y_all[-20:] #testing on last 20 matches

#all the models we are comparing
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

#function to get accuracy of algorithms
scores = {}
acc = []
cv_scores = []
def model(model):
    model.fit(X_train,y_train)
    score = model.score(X_test,y_test)
    print("Accuracy: {}".format(score))
    cv_score = cross_val_score(model,X_train,y_train,cv=5)
    print("Cross Val Score: {}".format(np.mean(cv_score)))
    acc.append(score)
    cv_scores.append(np.mean(cv_score))

#applying all algorithms
from xgboost import XGBClassifier
clf = XGBClassifier()
model(clf)
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
model(clf)
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
model(clf)
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
model(clf)
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()
model(clf)
from sklearn.svm import SVC
clf = SVC()
model(clf)
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
model(clf)
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier()
model(clf)
from sklearn.ensemble import GradientBoostingClassifier
clf = GradientBoostingClassifier()
model(clf)

#List of models with their accuracy
models = ["XGBClassifier","LogisticRegression","RandomForestClassifier","DecisionTreeClassifier","KNeighborsClassifier","SVC","GaussianNB","AdaBoostClassifier","GradientBoostingClassifier"]
scores = { "Model Name" : models , "Accuracy Score" : acc, "Cross val Score": cv_scores}
df1 = pd.DataFrame(scores)


#combining top 3 algorithms for efficiency

estimator=[]
estimator.append(('XGB',XGBClassifier()))
estimator.append(('LR',LogisticRegression()))
estimator.append(('GB',RandomForestClassifier()))

#Using the ensemble and checking its accuracy
from sklearn.ensemble import VotingClassifier

ensemble=VotingClassifier(estimators=estimator, voting='hard',n_jobs=-1)

ensemble.fit(X_train,y_train)
y_pred=ensemble.predict(X_test)
score = ensemble.score(X_test,y_test)
print("Accuracy: {}".format(score))

### This model I have not deployed on a FLask application beacause it is difficult to automate getting form of matches and performance of a team in every matchweek for year 2021 as every MW does not have 10 matches but this model can be quoted in the research paper and how we imporoved accuracy by adding more feaures
