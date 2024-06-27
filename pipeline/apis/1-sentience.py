#!/usr/bin/env python3
'''
triblizer in web scrapping
'''


import requests


def sentientPlanets():
    '''
    through links
    '''
    url = 'https://swapi-api.alx-tools.com/api/species/?page=1'
    planets = []

    while url:
        response = requests.get(url).json()

        for specy in response['results']:
            if specy['designation'] == 'sentient' or specy['classification'] == 'sentient':
                if specy['homeworld']:
                    get_planet = requests.get(specy['homeworld']).json()
                    planets.append(get_planet['name'])
        
        url = response['next']
    
    return planets
