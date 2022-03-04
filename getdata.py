import requests
import json
from getdata import upload_file, create_bucket

url = "https://api.covid19api.com/live/country/barbados/status/confirmed"

response = requests.get(url)
json_data = response.json()
latest_entry = json_data[-1]
seventh_latest_entry = json_data[-8]
fourteenth_latest_entry = json_data[-15]

last_week = latest_entry['Active'] - seventh_latest_entry['Active']
week_before = seventh_latest_entry['Active'] - fourteenth_latest_entry['Active']

if last_week < week_before:
    trend = "DOWN"
elif last_week == week_before:
    trend = "SAME SAME"
else:
    trend = "UP"

if last_week > 1000:
    lockdown = "true"
else:
    lockdown = "false"

dictionary = {
    'cases': latest_entry['Confirmed'] - seventh_latest_entry['Confirmed'],
    'active': latest_entry['Active'] - seventh_latest_entry['Active'],
    'trend': trend,
    'lockdown': lockdown
}

with open('barbados.json', 'w') as json_file:
    json.dump(dictionary, json_file)


bucket_name = 'supersparkyawesomebouquet202203042'

create_bucket(bucket_name, 'eu-central-1')
upload_file('barbados.json', bucket_name)