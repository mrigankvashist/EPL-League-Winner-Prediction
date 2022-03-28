from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
import warnings
warnings.filterwarnings("ignore")
import json
import plotly
import plotly.express as px
import epl_week_test_prep

playing_stat=pd.read_csv('/Users/KillSwitch/Desktop/footy 2/playing_stat.csv') #testing data
df=pd.read_csv('/Users/KillSwitch/Desktop/footy 2/epl_week.csv') #training data
y=df['Win']
df=df[playing_stat.columns]
clf = AdaBoostClassifier()  # ada boost obj
clf.fit(df,y) # object const and variable
        
results=clf.predict_proba(playing_stat)
results=pd.DataFrame(results,columns=['Lose','Win'])
final=pd.concat([playing_stat,results],axis=1)
final=final.drop(columns=['GS','GC','Points','FormPts'])
final['Team']=0
        
for i in range(len(final)):
    for j in range(2,len(final.columns)-3):
        if final.iloc[i,j]==1:
            final["Team"][i]=final.columns[j].split('_')[1]
        
final=final.loc[:,['MW','Team','Win']]
final['Win']=round(final["Win"]*100,2)   

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    if request.method == 'POST':
        
        
        team=request.form['team']
        
        team_wise=final[final['Team']==team].sort_values('MW').drop(columns=['Team']) # sorting graph by MW ascend
        
        fig = px.line(team_wise, x='MW', y='Win')
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder) # graph plot
        head1="Winning probability of {} across Matchweeks".format(team) #header and footer of graph
        foot1="The current chance of {} winning the EPL is: {}%".format(team,team_wise.iloc[-1,1])
       

        return render_template('result.html', graphJSON=graphJSON,header=head1,footer=foot1)

@app.route('/predict2', methods=['POST'])
def predict2():
    if request.method == 'POST':
        week=int(request.form['mw'])
        
        week_wise=final[final['MW']==week].sort_values('Team').drop(columns='MW') # sorting tem name lexograph
        max=week_wise.sort_values(by=['Win']).reset_index(drop=True)
        fig = px.line(week_wise,x='Team',y='Win') 
        
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        head2="Winning probability of teams in Matchweek {}".format(week)
        foot2="{} had the highest chance of winning the EPL in week {}.".format(max.iloc[-1,0],week)
    
    return render_template('result.html',header=head2,graphJSON=graphJSON,footer=foot2)


if __name__ == '__main__':
	app.run(debug=True)

