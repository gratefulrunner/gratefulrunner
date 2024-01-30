#this is a fun script that I wrote that will plot out some interesting data about my recent running via connecting to the Strava API 

#importing libraries and putting tokens in variables
import requests
import urllib3
import pandas as pd
import json
import time
import datetime
import urllib3
import numpy as np
import matplotlib
from json import loads
from datetime import datetime


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

#Strava Keys from API page
client_secret = 'xyz'
access_token = 'xyz'
refresh_token = 'xyz'
client_id = 'xyz'
ahtlete_id = 'xyz'

#Oauth put request to strava API for access token
payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'refresh_token': refresh_token,
    'grant_type': "refresh_token",
    'f': 'json'
}
res = requests.post(auth_url, data=payload, verify=False)
print("On a run to get the token...\n")

auth_token_app = res.json()['access_token']
print('Token is:')
print(auth_token_app)


#Making a request for all Strava activities within a given timeframe
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
start_range = input('Choose start date (yyyy-mm-dd):' )
end_range = input('Choose end date (yyyy-mm-dd):' )
print('Fetching Runs from '+start_range+' through '+end_range)

#converting input to epoch format for get request
start_epoch = str(datetime.strptime(start_range, '%Y-%m-%d').timestamp())
end_epoch = str(datetime.strptime(end_range, '%Y-%m-%d').timestamp())

header = {'Authorization': 'Bearer ' + auth_token_app}
param = {'per_page':200, 'page':1, 'before':end_epoch, 'after':start_epoch}
url = "https://www.strava.com/api/v3/athlete/activities"
athlete_dataset = requests.get(url, headers=header,params=param).json()


#getting data from Strava API, converting JSON output to Pandas DataFrame
data =  requests.get(url, headers=header,params=param)
data_dict = loads(data.text)
df = pd.DataFrame.from_dict(data_dict)

#converting meters to miles and formatting date column, plotting some visualizations
df['distance_miles'] = df.apply(lambda row: row['distance'] * 0.000621371, axis=1)
df['start_date']= pd.to_datetime(df['start_date'])
df.plot(x = 'distance_miles', y = 'average_heartrate', kind='scatter')
df.plot(x = 'start_date', y = 'distance_miles')
