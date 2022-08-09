import requests
import pandas as pd
import json


def pull_propublica_api():
    house_response = requests.get('https://api.propublica.org/congress/v1/117/house/members.json',
                                  headers={"X-API-Key": "9L6uV3lFjPXOfqlLMs7LSSmDfYamLpjtM1G92ujV"}).text
    senate_response = requests.get('https://api.propublica.org/congress/v1/117/senate/members.json',
                                   headers={"X-API-Key": "9L6uV3lFjPXOfqlLMs7LSSmDfYamLpjtM1G92ujV"}).text

    house_info = json.loads(house_response)['results'][0]['members']
    senate_info = json.loads(senate_response)['results'][0]['members']

    house_df = pd.DataFrame(house_info)
    senate_df = pd.DataFrame(senate_info)

    full_df = pd.concat([house_df, senate_df], ignore_index=True)

    return full_df


def pretty_print(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)


'''
Taken from:
https://gis.stackexchange.com/questions/16423/converting-state-name-abbreviations-to-full-names-using-arcgis-field-calculator
'''


def statenames(stateabbreviation):
    states = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
    }
    if stateabbreviation is not None:
        if stateabbreviation in states:
            return states[stateabbreviation]
        else:
            return None
    else:
        return None
