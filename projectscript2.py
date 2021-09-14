import datetime
import json
import requests
from datetime import date, timedelta
import pandas as pd

def get_yesterday_date():
    yesterday = date.today() - datetime.timedelta(days=1)
    return yesterday

def read_wind_data():
    wind_data = pd.read_json(str(get_yesterday_date()) + '_wind.txt')
    total_wind = wind_data['value'].sum()
    return total_wind

def read_consump_data():
    consump_data = pd.read_json(str(get_yesterday_date()) + '_consumption.txt')
    total_consump = consump_data['value'].sum()
    return total_consump

def store_coverage_data():
    daily_percent = read_wind_data() / read_consump_data()
    daily_stats = open('daily_stats.txt', 'a')
    daily_stats.write('date: ' + str(get_yesterday_date()) + ' percentage: ' + str(daily_percent) + '\n')

store_coverage_data()