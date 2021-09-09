import datetime
import json
import requests
from datetime import date, timedelta
import pandas as pd

yesterday = date.today() - datetime.timedelta(days=1)

wind_data = pd.read_json(str(yesterday)+'_wind.txt')
total_wind = wind_data['value'].sum()

consump_data = pd.read_json(str(yesterday)+'_consumption.txt')
total_consump = consump_data['value'].sum()
print(total_wind)
print(total_consump)

daily_percent = total_wind/total_consump
print(daily_percent)

daily_stats = open('daily_stats.txt','a')
daily_stats.write('date: '+str(yesterday)+ ' percentage: '+str(daily_percent)+'\n')