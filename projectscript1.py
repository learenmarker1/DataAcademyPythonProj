import datetime
import json
import requests
from datetime import date, timedelta
wind_id = 75
consumption_id = 124
variable_id = {'wind_id':75, 'consumption_id':124}
personal_code = {'x-api-key': 'fXC7ucDVprBINXhgfBHh80Aq1SpIUPy9KahxZHfj'}
#time_param = {'start_time': '2021-09-07T00:00:00Z', 'end_time': '2021-09-07T23:59:59Z'}


#requests.get('https://api.fingrid.fi/v1/variable/{}/events/json'.format(variable_id), headers=header, params=time)

#print(r.json())

def get_time_param():
    yesterday = date.today() - datetime.timedelta(days=1)
    start = str(yesterday)+'T00:00:00Z'
    end = str(yesterday)+'T23:59:59Z'
    time_parameter = {'start_time': str(start),'end_time':str(end)}
    return time_parameter

def create_file():
    #parameters
    time_param = get_time_param()
    yesterday = date.today() - datetime.timedelta(days=1)

    #create wind file and request wind data
    wind_file = open(str(yesterday)+'_wind.txt', 'w')
    wind_request = requests.get('https://api.fingrid.fi/v1/variable/{}/events/json'.format(wind_id), headers=personal_code, params=time_param)
    wind_file.write(json.dumps(wind_request.json()))

    #create consumption file and request consumption data
    consumption_file = open(str(yesterday)+'_consumption.txt', 'w')
    consumption_request = requests.get('https://api.fingrid.fi/v1/variable/{}/events/json'.format(consumption_id), headers=personal_code, params=time_param)
    consumption_file.write(json.dumps(consumption_request.json()))

    wind_file.close()
    consumption_file.close()



