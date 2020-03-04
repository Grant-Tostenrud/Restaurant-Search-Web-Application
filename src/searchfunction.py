# make imports
import requests
from src.mapfunction import mapfunction
from random import seed
from random import randint


def search(location, termval: object, priceval: object, opennow: object) -> object:
    # get API key
    API_KEY = 'DX12YoxM4wxoZcRXkxF4jiYscuhM5ibJuixL1zqDZ5sxORA3WnO2xf7-4fd6hwaAJHG3xsuFfnPlAp3Rssq6DLKc585' \
              '-OcyGasAjlhbXjnuhR-kV0RkY36_SmRlPXnYx '
    # define endpoint and header
    endpoint = 'https://api.yelp.com/v3/businesses/search'
    headers = {
        'Authorization': 'Bearer %s' % API_KEY
    }
    openval = True
    # transform opennow variable to a boolean true or false
    if opennow == 'yes':
        openVal = True
    else:
        openVal = False
    # define parameters
    parameters = {'term': termval,
                  'price': priceval,
                  'open_now': openval,
                  'hot_and_new': '',
                  'limit': 1,
                  'location': location}

    # make request
    response = requests.get(url=endpoint, params=parameters, headers=headers)
    # convert to a dictionary
    data: object = response.json()
    # print out names of businesses
    for biz in data['businesses']:
        name = biz['name']
    # get locations of each business
    lat = []
    long = []
    for item in data["businesses"]:
        lat.append(item['coordinates']['latitude'])
        long.append(item['coordinates']['longitude'])
    # merge latitude and longitude into an array
    lat_long = list((zip(lat, long)))
    print(lat_long)

    # call map function
    mapfunction(lat_long)

    return name