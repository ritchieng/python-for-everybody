import urllib
import twurl
import json

# Base URL: get from API Documentation
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print ''
    acct = raw_input('Enter Twitter Account:')
    if ( len(acct) < 1 ) : break
    # Count: # of friends
    url = twurl.augment(TWITTER_URL,
        {'screen_name': acct, 'count': '5'} )
    print 'Retrieving', url
    # Open URL
    connection = urllib.urlopen(url)
    # Open body, JSON
    data = connection.read()
    # Open headers, dictionary
    headers = connection.info().dict
    # Remaining limit for the day by accessing the dictionary
    print 'Remaining', headers['x-rate-limit-remaining']
    # Deserialize the json --> turn to list (native Python)
    js = json.loads(data)
    # json.dumps for pretty printing of 'js' using 'indent=4'
    # Easier readability of JSON data
    print json.dumps(js, indent=4)

    # Loop through list of users
    for u in js['users']:
        print u['screen_name']
        s = u['status']['text']
        print '  ',s[:50]
