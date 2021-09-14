import datetime
import json
import requests
from datetime import date, timedelta
wind_id = 75
consumption_id = 124
variable_id = {'wind_id':75, 'consumption_id':124}
personal_code = {'x-api-key': 'fXC7ucDVprBINXhgfBHh80Aq1SpIUPy9KahxZHfj'}

def get_yesterday_date():
    yesterday = date.today() - datetime.timedelta(days=1)
    return yesterday

def create_time_param():
    yesterday = get_yesterday_date()
    start = str(yesterday)+'T00:00:00Z'
    end = str(yesterday)+'T23:59:59Z'
    time_parameter = {'start_time': str(start),'end_time':str(end)}
    return time_parameter


    #parameters
    '''time_param = create_time_param()
    yesterday = get_yesterday_date()


    #create wind file and request wind data
    wind_file = open(str(yesterday)+'_wind.txt', 'w')
    wind_request = requests.get('https://api.fingrid.fi/v1/variable/{}/events/json'.format(wind_id), headers=personal_code, params=time_param)
    wind_file.write(json.dumps(wind_request.json()))

    #create consumption file and request consumption data
    consumption_file = open(str(yesterday)+'_consumption.txt', 'w')
    consumption_request = requests.get('https://api.fingrid.fi/v1/variable/{}/events/json'.format(consumption_id), headers=personal_code, params=time_param)
    consumption_file.write(json.dumps(consumption_request.json()))

    wind_file.close()
    consumption_file.close()'''

def create_wind_file():
    wind_file = open(str(get_yesterday_date())+'_wind.txt', 'w')
    wind_request = requests.get('https://api.fingrid.fi/v1/variable/{}/events/json'.format(wind_id), headers=personal_code, params=create_time_param())
    wind_file.write(json.dumps(wind_request.json()))
    wind_file.close()

def create_consumption_file():
    consumption_file = open(str(get_yesterday_date())+'_consumption.txt', 'w')
    consumption_request = requests.get('https://api.fingrid.fi/v1/variable/{}/events/json'.format(consumption_id), headers=personal_code, params=create_time_param())
    consumption_file.write(json.dumps(consumption_request.json()))
    consumption_file.close()

def create_files():
    create_wind_file()
    create_consumption_file()

create_files()

