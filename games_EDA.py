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

games = pd.read_csv("nfl-big-data-bowl-2021/games.csv",dtype={'gameId': 'object'})

games.gameDate = pd.to_datetime(games.gameDate)
games.gameTimeEastern.value_counts()
gametime_map = {'20:20:00':'night', '13:00:00':'early', '16:25:00':'afternoon', '19:10:00':'night', '22:20:00':'night',
       '16:05:00':'afternoon', '20:15:00':'night', '09:30:00':'london', '12:30:00':'early', '16:30:00':'afternoon'}
games['timeslot'] = games['gameTimeEastern'].map(gametime_map)
games['timeslot'].value_counts()
games['day'] = games['gameDate'].dt.day_name()
games.day.value_counts()

games.homeTeamAbbr.nunique()
games.visitorTeamAbbr.nunique()
games.week.value_counts()