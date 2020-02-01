import requests
import json
import datetime

print('balls')

apiKey = 'sjClxN1dYb44Pe0MN5EOYDv9fGaRkWwu'
URL = 'https://app.ticketmaster.com/discovery/v2/events.json'
artists = ['marcus king', 'john mayer', 'foo fighters',
           'eric clapton', 'bb king', 'joe bonomassa', 'queens of the stone age']
notListed = []
for x in artists:

    PARAMS = {'apikey': apiKey, 'local': 'en',
              'keyword': x, 'countryCode': 'GB', 'size': 1}

    request = requests.get(url=URL, params=PARAMS)

    parsed = json.loads(request.text)

    if '_embedded' not in parsed:
        notListed.append(x)
    else:
        gigs = []
        print('Results for ' + x.title())
        for e in parsed['_embedded']['events']:
            venues = e['_embedded']['venues'][0]
            dates = e['dates']['start']
            gigs.append({
                'name': e['name'],
                'venue': venues['name'] + ', ' + venues['city']['name'],
                'date': dates['localDate'],
                'time': dates['localTime'],
                'ticket-url': e['url']
            })

        print(json.dumps(gigs, indent=4, sort_keys=True))
print('Artists not listed:')
for a in notListed:
    print(a.title())
