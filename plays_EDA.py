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

Opositions = ['OL','QB', 'RB', 'TE', 'WR','FB','HB']
Dpositions = ['DL', 'LB', 'DB','SS','FS','MLB','CB','OLB', 'ILB','NT', 'S', 'DE','DT']
STpositions = ['K','P','LS']

plays = pd.read_csv("nfl-big-data-bowl-2021/plays.csv")

plays.info()
plays.isna().sum()

plays['gameId'] = plays['gameId'].astype(str)
plays['playId'] = plays['playId'].astype(str)

plays.playDescription
plays.quarter.value_counts()
plays.down.value_counts()
plays.playType.value_counts()
plays['playType'] = plays['playType'].str.replace("play_type_","")

plays.yardlineSide.value_counts()
plays['yardlineSide'] = np.where(plays['yardlineSide'].isna(),'Fifty',plays['yardlineSide'])

plays.personnelO.value_counts()






#plays = plays[plays['penaltyCodes'].isna()]
for p in Opositions:
    pattern = '(..' + str(p) + ')'
    plays[p] = 0
    plays[p] = plays['personnelO'].str.extract(pat=pattern,expand=True)
    plays[p] = plays[p].str.replace(r'\D+', '').fillna(0).astype(int)

plays['OL'] = np.where(plays['OL'] == 0, 5, plays['OL'])
plays['QB'] = np.where(plays['QB'] == 0, 1, plays['QB'])
plays['Off'] = plays['QB']+ plays['RB'] + plays['HB'] + plays['WR'] + plays['TE'] + plays['OL']
#plays = plays[plays['Off'] == 11]

for p in Dpositions:
    pattern = '(..' + str(p) + ')'
    plays[p] = 0
    plays[p] = plays['personnelD'].str.extract(pat=pattern,expand=True)
    plays[p] = plays[p].str.replace(r'\D+', '').fillna(0).astype(int)

plays['Def'] = plays['DL'] + plays['LB'] + plays['DB']
#plays = plays[plays['Def'] == 11]
#plays = plays[plays['defendersInTheBox'].notna()]
#plays['defendersInTheBox'] = plays['defendersInTheBox'].astype(int)
#plays = plays[plays['numberOfPassRushers'].notna()]
#plays['numberOfPassRushers'] = plays['numberOfPassRushers'].astype(int)
#plays = plays[plays['preSnapVisitorScore'].notna()]
#plays['preSnapVisitorScore'] = plays['preSnapVisitorScore'].astype(int)
#plays['preSnapHomeScore'] = plays['preSnapHomeScore'].astype(int)
plays['personnel'] = plays['RB'].astype(str) + plays['TE'].astype(str)
plays = plays.drop(columns={'OL', 'QB', 'RB', 'TE', 'WR', 'FB', 'HB', 'DL', 'LB', 'DB', 'SS',
       'FS', 'MLB', 'CB', 'OLB', 'ILB', 'NT', 'S', 'DE', 'DT',})
