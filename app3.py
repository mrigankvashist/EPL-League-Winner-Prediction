from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import missingno as msno
from collections import defaultdict
import re
import seaborn as sns
import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, ConnectionPatch, Arc
from matplotlib.font_manager import FontProperties
from functools import reduce
import plotly.express as px
import plotly.graph_objects as go
from mplsoccer.pitch import VerticalPitch
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import part3

df22=pd.read_csv('/Users/KillSwitch/Desktop/footy 2/df22.csv')

app3 = Flask(__name__)

@app3.route('/')
def home():
	return render_template('home.html')

@app3.route('/', methods=['POST'])
def predict():
     if request.method == 'POST':
        
        
        home_team=request.form['home_team']
        away_team=request.form['away_team']
        
        img=part3.draw_teams_matchup(df22, df22, 'Home Team in 2022', 'Away Team in 2022', home_team_name=home_team, away_team_name=away_team, drawn_pitch='mplsoccer')
        
        pngImage = io.BytesIO()
        FigureCanvas(img).print_png(pngImage)
            
        # Encode PNG image to base64 string
        pngImageB64String = "data:image/png;base64,"
        pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
        
        return render_template('res.html',figure=pngImageB64String)

if __name__ == '__main__':
    app3.run(debug=True)
