"""### Part 2- II : Creating test data"""

### This file will run everytime when the Flask application is run to create the updated dataset, then ML is performed later on in the app.py file.
### Basic idea is we have training data of last 15 years. We know how a team performed every week when it won the league (it is called train data because model has results to learn from)
### So we create a similar week wise dataset for the current year also to predict which team will win this year (we call it test data as we don't have results for it)


#essential librarires
import numpy as np
import pandas as pd
from datetime import datetime as dt
import itertools

# %matplotlib inline

url="https://www.football-data.co.uk/mmz4281/2122/E0.csv" #Taking data from this URL everytime the application is run so that updated data is given to the model (EPL 21-22)
data=pd.read_csv(url,index_col=0).reset_index(drop=True) #Reading data as CSV, with the first column being the index.

def parse_date(date):  #Making all dates in one single format of YYYY/MM/DD
    return data['Date'][i].split('/')[2] + "/" + data['Date'][i].split('/')[1] + "/" + data['Date'][i].split('/')[0]

for i in range(len(data)):      #changing all dates to string type and applying the above function
    data['Date'][i]=str(data['Date'][i])
    data['Date'][i]=parse_date(data['Date'][i])

columns_req = ['Date','HomeTeam','AwayTeam','FTR','FTHG','FTAG']  #only columns needed from main data, we will calculate other important features from the data below. We are considering full time goals for this part as we have to predict league winner not match winner

playing_statistics = data[columns_req] #selecting needed columns

playing_statistics['Date']=pd.to_datetime(playing_statistics['Date']) #converting date to Python datetime object
playing_statistics['MW']=0  #creating a column to add matchweek as this year every matchweek doesn't have 10 matches, they are scattered, so we create MWs according to the date


for i in range(len(playing_statistics)):
  if playing_statistics['Date'][i]<pd.to_datetime('2021-08-21'):
      playing_statistics['MW'][i]=0                               #note: We mark the first MW as 0 because in Python range start from 0, it is easy for calculations
  if playing_statistics['Date'][i]>pd.to_datetime('2021-08-20') and playing_statistics['Date'][i]<pd.to_datetime('2021-08-28'):
    playing_statistics['MW'][i]=1
  if playing_statistics['Date'][i]>pd.to_datetime('2021-08-27') and playing_statistics['Date'][i]<pd.to_datetime('2021-09-11'):
    playing_statistics['MW'][i]=2
  if playing_statistics['Date'][i]>pd.to_datetime('2021-09-10') and playing_statistics['Date'][i]<pd.to_datetime('2021-09-18'):
    playing_statistics['MW'][i]=3
  if playing_statistics['Date'][i]>pd.to_datetime('2021-09-17') and playing_statistics['Date'][i]<pd.to_datetime('2021-09-25'):
    playing_statistics['MW'][i]=4
  if playing_statistics['Date'][i]>pd.to_datetime('2021-09-24') and playing_statistics['Date'][i]<pd.to_datetime('2021-10-02'):
    playing_statistics['MW'][i]=5
  if playing_statistics['Date'][i]>pd.to_datetime('2021-10-01') and playing_statistics['Date'][i]<pd.to_datetime('2021-10-16'):
    playing_statistics['MW'][i]=6
  if playing_statistics['Date'][i]>pd.to_datetime('2021-10-15') and playing_statistics['Date'][i]<pd.to_datetime('2021-10-23'):
    playing_statistics['MW'][i]=7
  if playing_statistics['Date'][i]>pd.to_datetime('2021-10-22') and playing_statistics['Date'][i]<pd.to_datetime('2021-10-30'):
    playing_statistics['MW'][i]=8
  if playing_statistics['Date'][i]>pd.to_datetime('2021-10-29') and playing_statistics['Date'][i]<pd.to_datetime('2021-11-06'):
    playing_statistics['MW'][i]=9
  if playing_statistics['Date'][i]>pd.to_datetime('2021-11-05') and playing_statistics['Date'][i]<pd.to_datetime('2021-11-20'):
    playing_statistics['MW'][i]=10
  if playing_statistics['Date'][i]>pd.to_datetime('2021-11-19') and playing_statistics['Date'][i]<pd.to_datetime('2021-11-27'):
    playing_statistics['MW'][i]=11
  if playing_statistics['Date'][i]>pd.to_datetime('2021-11-26') and playing_statistics['Date'][i]<pd.to_datetime('2021-12-01'):
    playing_statistics['MW'][i]=12
  if playing_statistics['Date'][i]>pd.to_datetime('2021-11-30') and playing_statistics['Date'][i]<pd.to_datetime('2021-12-04'):
    playing_statistics['MW'][i]=13
  if playing_statistics['Date'][i]>pd.to_datetime('2021-12-03') and playing_statistics['Date'][i]<pd.to_datetime('2021-12-11'):
    playing_statistics['MW'][i]=14
  if playing_statistics['Date'][i]>pd.to_datetime('2021-12-10') and playing_statistics['Date'][i]<pd.to_datetime('2021-12-15'):
    playing_statistics['MW'][i]=15
  if playing_statistics['Date'][i]>pd.to_datetime('2021-12-14') and playing_statistics['Date'][i]<pd.to_datetime('2021-12-18'):
    playing_statistics['MW'][i]=16
  if playing_statistics['Date'][i]>pd.to_datetime('2021-12-17') and playing_statistics['Date'][i]<pd.to_datetime('2021-12-26'):
    playing_statistics['MW'][i]=17
  if playing_statistics['Date'][i]>pd.to_datetime('2021-12-25') and playing_statistics['Date'][i]<pd.to_datetime('2021-12-28'):
    playing_statistics['MW'][i]=18
  if playing_statistics['Date'][i]>pd.to_datetime('2021-12-27') and playing_statistics['Date'][i]<pd.to_datetime('2022-01-01'):
    playing_statistics['MW'][i]=19
  if playing_statistics['Date'][i]>pd.to_datetime('2021-12-31') and playing_statistics['Date'][i]<pd.to_datetime('2022-01-04'):
    playing_statistics['MW'][i]=20
  if playing_statistics['Date'][i]>pd.to_datetime('2022-01-11') and playing_statistics['Date'][i]<pd.to_datetime('2022-01-14'):
    playing_statistics['MW'][i]=17
  if playing_statistics['Date'][i]==pd.to_datetime('2022-01-20'):
    playing_statistics['MW'][i]=16
  if playing_statistics['Date'][i]==pd.to_datetime('2022-01-19') and playing_statistics['HomeTeam'][i]=='Burnley':
    playing_statistics['MW'][i]=16
  if playing_statistics['Date'][i]==pd.to_datetime('2022-01-19') and playing_statistics['HomeTeam'][i]=='Brighton':
    playing_statistics['MW'][i]=23
  if playing_statistics['Date'][i]>pd.to_datetime('2022-01-14') and playing_statistics['Date'][i]<pd.to_datetime('2022-01-19'):
    playing_statistics['MW'][i]=21
  if playing_statistics['Date'][i]>pd.to_datetime('2022-01-21') and playing_statistics['Date'][i]<pd.to_datetime('2022-02-05'):
    playing_statistics['MW'][i]=22
  if playing_statistics['Date'][i]==pd.to_datetime('2022-02-05'):
    playing_statistics['MW'][i]=16
  if playing_statistics['Date'][i]>pd.to_datetime('2022-02-08') and playing_statistics['Date'][i]<pd.to_datetime('2022-02-12'):
    playing_statistics['MW'][i]=23
  if playing_statistics['Date'][i]>pd.to_datetime('2022-02-11') and playing_statistics['Date'][i]<pd.to_datetime('2022-02-19'):
    playing_statistics['MW'][i]=24
  if playing_statistics['Date'][i]==pd.to_datetime('2022-02-16'):
    playing_statistics['MW'][i]=17
  if playing_statistics['Date'][i]>pd.to_datetime('2022-02-18') and playing_statistics['Date'][i]<pd.to_datetime('2022-02-26'):
    playing_statistics['MW'][i]=25
  if playing_statistics['Date'][i]==pd.to_datetime('2022-02-24') and playing_statistics['HomeTeam'][i]=='Burnley':
    playing_statistics['MW'][i]=12
  if playing_statistics['Date'][i]==pd.to_datetime('2022-02-24') and playing_statistics['HomeTeam'][i]=='Watford':
    playing_statistics['MW'][i]=17
  if playing_statistics['Date'][i]==pd.to_datetime('2022-02-24') and playing_statistics['HomeTeam'][i]=='Liverpool':
    playing_statistics['MW'][i]=18
  if playing_statistics['Date'][i]==pd.to_datetime('2022-02-25'):
    playing_statistics['MW'][i]=19
  if playing_statistics['Date'][i]>pd.to_datetime('2022-02-25') and playing_statistics['Date'][i]<pd.to_datetime('2022-02-28'):
    playing_statistics['MW'][i]=26
  if playing_statistics['Date'][i]==pd.to_datetime('2022-03-02'):
    playing_statistics['MW'][i]=21
  if playing_statistics['Date'][i]>pd.to_datetime('2022-03-04') and playing_statistics['Date'][i]<pd.to_datetime('2022-03-12'):
    playing_statistics['MW'][i]=27
  if playing_statistics['Date'][i]==pd.to_datetime('2022-03-11') and playing_statistics['HomeTeam'][i]=='Wolves':
    playing_statistics['MW'][i]=18
  if playing_statistics['Date'][i]==pd.to_datetime('2022-03-11') and playing_statistics['HomeTeam'][i]=='Leeds United':
    playing_statistics['MW'][i]=19
  if playing_statistics['Date'][i]==pd.to_datetime('2022-03-11') and playing_statistics['HomeTeam'][i]=='Southampton':
    playing_statistics['MW'][i]=20
  if playing_statistics['Date'][i]==pd.to_datetime('2022-03-11') and playing_statistics['HomeTeam'][i]=='Norwich City':
    playing_statistics['MW'][i]=29
  if playing_statistics['Date'][i]>pd.to_datetime('2022-03-11') and playing_statistics['Date'][i]<pd.to_datetime('2022-03-16'):
    playing_statistics['MW'][i]=28
  if playing_statistics['Date'][i]==pd.to_datetime('2022-03-16') and playing_statistics['HomeTeam'][i]=='Brighton':
    playing_statistics['MW'][i]=15
  if playing_statistics['Date'][i]==pd.to_datetime('2022-03-16') and playing_statistics['HomeTeam'][i]=='Arsenal':
    playing_statistics['MW'][i]=26
  if playing_statistics['Date'][i]==pd.to_datetime('2022-03-17') and playing_statistics['HomeTeam'][i]=='Everton':
    playing_statistics['MW'][i]=19
  if playing_statistics['Date'][i]>pd.to_datetime('2022-03-17') and playing_statistics['Date'][i]<pd.to_datetime('2022-04-02'):
    playing_statistics['MW'][i]=29
  if playing_statistics['Date'][i]>pd.to_datetime('2022-04-01') and playing_statistics['Date'][i]<pd.to_datetime('2022-04-09'):
    playing_statistics['MW'][i]=30
  if playing_statistics['Date'][i]>pd.to_datetime('2022-04-08') and playing_statistics['Date'][i]<pd.to_datetime('2022-04-16'):
    playing_statistics['MW'][i]=31
  if playing_statistics['Date'][i]>pd.to_datetime('2022-04-15') and playing_statistics['Date'][i]<pd.to_datetime('2022-04-23'):
    playing_statistics['MW'][i]=32
  if playing_statistics['Date'][i]>pd.to_datetime('2022-04-22') and playing_statistics['Date'][i]<pd.to_datetime('2022-04-30'):
    playing_statistics['MW'][i]=33
  if playing_statistics['Date'][i]>pd.to_datetime('2022-04-29') and playing_statistics['Date'][i]<pd.to_datetime('2022-05-07'):
    playing_statistics['MW'][i]=34
  if playing_statistics['Date'][i]>pd.to_datetime('2022-05-06') and playing_statistics['Date'][i]<pd.to_datetime('2022-05-15'):
    playing_statistics['MW'][i]=35
  if playing_statistics['Date'][i]>pd.to_datetime('2022-05-14') and playing_statistics['Date'][i]<pd.to_datetime('2022-05-22'):
    playing_statistics['MW'][i]=36
  if playing_statistics['Date'][i]>pd.to_datetime('2022-05-21'):
    playing_statistics['MW'][i]=37


# Gets the goals scored agg arranged by teams and matchweek
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

    for i in teams.keys():     #This function gets the cummulative goals scored by team at the end of a MW, made some changes to the original code to fit the issue of inconsistent number of matches in a wek
        teams[i]=teams[i] + [-1] * (38 - len(teams[i]))
    GoalsScored = pd.DataFrame(data=teams, index = [i for i in range(1,39)]).T
    GoalsScored[0] = 0
    # Aggregate to get uptil that point
    for i in range(2,39):
        GoalsScored[i] = GoalsScored[i] + GoalsScored[i-1]
    return GoalsScored



# Gets the goals conceded agg arranged by teams and matchweek
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

    for i in teams.keys():
      teams[i]=teams[i] + [-1] * (38 - len(teams[i]))
    # Create a dataframe for goals scored where rows are teams and cols are matchweek.
    GoalsConceded = pd.DataFrame(data=teams, index = [i for i in range(1,39)]).T
    GoalsConceded[0] = 0
    # Aggregate to get uptil that point
    for i in range(2,39):
        GoalsConceded[i] = GoalsConceded[i] + GoalsConceded[i-1]
    return GoalsConceded

def get_gss(playing_stat):
    GC = get_goals_conceded(playing_stat)
    GS = get_goals_scored(playing_stat)
   
    HTGS = []
    ATGS = []
    HTGC = []
    ATGC = []

    for i in range(len(playing_stat)):
        ht = playing_stat.iloc[i].HomeTeam
        at = playing_stat.iloc[i].AwayTeam
        j= playing_stat.iloc[i].MW
        HTGS.append(GS.loc[ht][j])
        ATGS.append(GS.loc[at][j])
        HTGC.append(GC.loc[ht][j])
        ATGC.append(GC.loc[at][j])
        
    playing_stat['HTGS'] = HTGS
    playing_stat['ATGS'] = ATGS
    playing_stat['HTGC'] = HTGC
    playing_stat['ATGC'] = ATGC
    
    return playing_stat

playing_statistics=get_gss(playing_statistics)

#calculating points on the basis of result
def get_points(result):
    if result == 'W':
        return 3
    elif result == 'D':
        return 1
    elif result =='X':                  #X is added as the result if the match has not been played yet
        return 0
    else:
        return 0
    

def get_cuml_points(matchres):  #cummulative points at the end of the weel
    matchres_points = matchres.applymap(get_points)
    for i in range(2,39):
        matchres_points[i] = matchres_points[i] + matchres_points[i-1]
        
    matchres_points.insert(column =0, loc = 0, value = [0*i for i in range(20)])
    return matchres_points


def get_matchres(playing_stat):     #Getting result of the match
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
      
    for i in teams.keys():
      teams[i]=teams[i] + ['X'] * (38 - len(teams[i]))

    return pd.DataFrame(data=teams, index = [i for i in range(1,39)]).T

def get_agg_points(playing_stat):           #Getting points on the basis of result
    matchres = get_matchres(playing_stat)
    cum_pts = get_cuml_points(matchres)
    HTP = []
    ATP = []

    for i in range(len(playing_stat)):
        ht = playing_stat.iloc[i].HomeTeam
        at = playing_stat.iloc[i].AwayTeam
        j= playing_stat.iloc[i].MW
        HTP.append(cum_pts.loc[ht][j])
        ATP.append(cum_pts.loc[at][j])
            
    playing_stat['HTP'] = HTP
    playing_stat['ATP'] = ATP
    return playing_stat

playing_statistics=get_agg_points(playing_statistics)

#playing_statistics #this would display the data, we have named our data- playing_statistics

#Functions for getting the form
def get_form(playing_stat,num):
    form = get_matchres(playing_stat)
    
    for i in form:
      for j in range(len(form[i])):
        if form[i][j]=='X':
          form[i][j]=form[i-1][j]

    form_final = form.copy()
    
    for i in range(num,39):
        form_final[i] = ''
        j = 0
        while j < num:
            form_final[i] += form[i-j]
            j += 1           
    return form_final

def add_form(playing_stat,num):
    form = get_form(playing_stat,num)
    h = ['M' for i in range(num * 10)]
    a = ['M' for i in range(num * 10)]
    
    j = num
    for i in range((num*10),len(playing_statistics)):
        ht = playing_stat.iloc[i].HomeTeam
        at = playing_stat.iloc[i].AwayTeam
        
        past = form.loc[ht][j]
        h.append(past[num-1])
        
        past = form.loc[at][j]
        a.append(past[num-1])
        
        if ((i + 1)% 10) == 0:
            j = j + 1

    playing_stat['HM' + str(num)] = h                 
    playing_stat['AM' + str(num)] = a

    
    return playing_stat

# We consider last 5 matches for form
def add_form_df(playing_statistics):
    playing_statistics = add_form(playing_statistics,1)
    playing_statistics = add_form(playing_statistics,2)
    playing_statistics = add_form(playing_statistics,3)
    playing_statistics = add_form(playing_statistics,4)
    playing_statistics = add_form(playing_statistics,5)
    return playing_statistics

playing_stat=add_form_df(playing_statistics)

def get_form_points(string):
    sum = 0
    for letter in string:
        sum += get_points(letter)
    return sum

playing_stat['HTFormPtsStr'] = playing_stat['HM1'] + playing_stat['HM2'] + playing_stat['HM3'] + playing_stat['HM4'] + playing_stat['HM5']
playing_stat['ATFormPtsStr'] = playing_stat['AM1'] + playing_stat['AM2'] + playing_stat['AM3'] + playing_stat['AM4'] + playing_stat['AM5']

#calculating form points on the basis of form
playing_stat['HTFormPts'] = playing_stat['HTFormPtsStr'].apply(get_form_points)
playing_stat['ATFormPts'] = playing_stat['ATFormPtsStr'].apply(get_form_points)

playing_stat=playing_stat.loc[:,['HomeTeam','AwayTeam','MW','HTGS','ATGS','HTGC','ATGC','HTP','ATP','HTFormPts','ATFormPts']]

##playing_stat #now our updated data is called playing_stat, these are just variable names to differentitate before and after a column is added

#scaling these features to maintain standard nature of data
cols = ['HTP','ATP']
playing_stat.MW = playing_stat.MW.astype(float)

for col in cols:
    playing_stat[col] = playing_stat[col] / playing_stat.MW

playing_stat=playing_stat.fillna(0)  #filling null values with 0

playing_stat['MW']=playing_stat['MW']+1  #Adding 1 to MW column so that the real MW value is displayed

home=playing_stat.loc[:,['MW','HomeTeam','HTGS','HTGC','HTP','HTFormPts']]  #selecting home and away columns separately as done for the training data
away=playing_stat.loc[:,['MW','AwayTeam','ATGS','ATGC','ATP','ATFormPts']]
home.columns=['MW','Team','GS','GC','Points','FormPts'] #renaming columns
away.columns=['MW','Team','GS','GC','Points','FormPts']
home=home[home['Team']!='Brentford'] #Dropping data related to Brentford as it is only playing this year
away=away[away['Team']!='Brentford']

home=home.groupby(['Team','MW']).sum().reset_index()   #Grouping data according to each Matchweek just like training data
away=away.groupby(['Team','MW']).sum().reset_index()

playing_stat=pd.concat([home,away]).reset_index(drop=True) #Combining data of home and away teams

playing_stat=pd.get_dummies(playing_stat,columns=['Team'])   #one-hot encoding the data

playing_stat.to_csv('/Users/KillSwitch/Desktop/footy 2/playing_stat.csv') #saving the data in the location you want


