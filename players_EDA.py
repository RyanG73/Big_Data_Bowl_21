import pandas as pd
import numpy as np
import datetime as dt
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import re
import seaborn as sns
import matplotlib.animation as animation
import plotly.express as px
import scipy
import math

players = pd.read_csv("nfl-big-data-bowl-2021/players.csv")

players.info()

players['nflId'] = players['nflId'].astype(str)

Opositions = ['OL','QB', 'RB', 'TE', 'WR','FB','HB']
Dpositions = ['DL', 'LB', 'DB','SS','FS','MLB','CB','OLB', 'ILB','NT', 'S', 'DE','DT']
STpositions = ['K','P','LS']


players['feet'] = pd.to_numeric(np.where(players['height'].str.contains('-'),players['height'].str.split('-').str[0],np.nan))
players['inches'] = pd.to_numeric(np.where(players['height'].str.contains('-'),players['height'].str.split('-').str[1],np.nan))
players['height'] = np.where(players['height'].str.contains('-'),players['feet']*12+players['inches'],players['height'])
players['height'] = players['height'].astype(int)
players = players.drop(['feet','inches'],axis='columns')
players['birthDate'] = pd.to_datetime(players['birthDate'])
players['side'] = np.where(players['position'].isin(Opositions),'Offense',np.nan)
players['side'] = np.where(players['position'].isin(Dpositions),'Defense',players['side'])
players['side'] = np.where(players['position'].isin(STpositions),'Special Teams',players['side'])


players[['displayName','collegeName']].value_counts()

colleges = players.collegeName.value_counts()

players['collegeName'] = np.where(players['collegeName'] == 'Miami (Fla.)','Miami',players['collegeName'])

m = players[players['collegeName'] == 'Miami (Fla.)']




