from urllib.request import urlopen
from dotenv import load_dotenv
import json
import os

def oscEventNotif():
    load_dotenv()
    url = os.getenv('API')
    response = urlopen(url)

    event_data = json.loads(response.read())

    with open ('data.json', 'r') as f:
        local_data = json.load(f)
    if(local_data['eventID'] == event_data[-1]['_id']):
        print("No new events")
    else:
        local_data['eventID'] = event_data[-1]['_id']
        with open('data.json', 'w') as f:
            json.dump(local_data, f, indent=4, separators=(',', ': '))
        print("New event added")