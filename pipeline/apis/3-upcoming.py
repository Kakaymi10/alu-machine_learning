#!/usr/bin/env python3
'''Space X'''


import sys
import requests
from datetime import datetime, timezone


def get_upcoming_launch():
    '''space X'''
    try:
        response = requests.get('https://api.spacexdata.com/v4/launches/upcoming')
        if response.status_code == 200:
            launches = response.json()
            # Sort launches by date_unix to find the upcoming launch
            upcoming_launch = sorted(launches, key=lambda x: x['date_unix'])[0]
            
            launch_name = upcoming_launch['name']
            launch_date_utc = datetime.fromtimestamp(upcoming_launch['date_unix'], timezone.utc)
            launch_date_local = launch_date_utc.astimezone().strftime('%Y-%m-%d %H:%M:%S')
            rocket_id = upcoming_launch['rocket']
            
            # Fetch rocket details
            rocket_response = requests.get(f'https://api.spacexdata.com/v4/rockets/{rocket_id}')
            rocket_name = rocket_response.json().get('name', 'Unknown rocket')
            
            # Fetch launchpad details
            launchpad_id = upcoming_launch['launchpad']
            launchpad_response = requests.get(f'https://api.spacexdata.com/v4/launchpads/{launchpad_id}')
            launchpad_data = launchpad_response.json()
            launchpad_name = launchpad_data.get('name', 'Unknown launchpad')
            launchpad_locality = launchpad_data.get('locality', 'Unknown locality')
            
            print(f'{launch_name} ({launch_date_local}) {rocket_name} - {launchpad_name} ({launchpad_locality})')
        else:
            print(f'Error: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')

if __name__ == '__main__':
    get_upcoming_launch()
