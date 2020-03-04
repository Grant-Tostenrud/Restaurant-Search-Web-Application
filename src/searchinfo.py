# make imports
import requests


def searchinfo(location, termval: object, priceval: object, opennow: object) -> object:
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
        info = biz['location']
        street = info['address1']
        city = info['city']
        state = info['state']
        zip = info['zip_code']
        location = street + ', ' + city + ', ' + state + ', ' + zip

    return location