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

def new_orientation(angle, play_direction):
    if play_direction == 0:
        new_angle = 360.0 - angle
        if new_angle == 360.0:
            new_angle = 0.0
        return new_angle
    else:
        return angle


Opositions = ['OL','QB', 'RB', 'TE', 'WR','FB','HB']
Dpositions = ['DL', 'LB', 'DB','SS','FS','MLB','CB','OLB', 'ILB','NT', 'S', 'DE','DT']
STpositions = ['K','P','LS']

tracking = pd.DataFrame()
for i in range(1,3):
    print(i)
    df = pd.read_csv("nfl-big-data-bowl-2021/week" + str(i) + ".csv",dtype={'playId': 'object','gameId': 'object'})
    tracking = tracking.append(df)


tracking.info()
tracking.isna().sum()
tracking.playId.nunique()


tracking['a'] = np.where(tracking['a'].isna(),0,tracking['a'])
tracking['nflId'] = np.where(tracking['nflId'].notnull(),tracking['nflId'],0)
tracking['nflId'] = tracking['nflId'].astype(int).astype(str)
tracking.dropna(subset=["playDirection"],inplace=True)



tracking['playDirection'] = tracking['playDirection'].apply(lambda x: x.strip() == 'right')
tracking['x'] = tracking.apply(lambda row: row['x'] if row['playDirection'] else 120-row['x'], axis=1)
tracking['y'] = tracking.apply(lambda row: row['y'] if row['playDirection'] else 160/3-row['y'], axis=1)
tracking['o'] = tracking.apply(lambda row: new_orientation(row['o'], row['playDirection']), axis=1)
tracking['dir'] = tracking.apply(lambda row: new_orientation(row['dir'], row['playDirection']), axis=1)
#tracking['nflId'] = tracking['nflId'].round(0).astype(str)








