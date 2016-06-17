# Imports
import urllib
import json

# Access Service API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

# Loop
while True:
    # Prompt location
    address = raw_input('Enter location: ')
    # If input = 0, end loop
    if len(address) < 1 : break

    # Encodes using urlencode using a dictionary
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})

    # Print URL
    print 'Retrieving', url

    # Open and read URL
    uh = urllib.urlopen(url)
    data = uh.read()

    # Print URL characters
    print 'Retrieved',len(data),'characters'

    # Try and except for bad data handling
    # json.loads loads data
    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    # Using json library, dump string using .dumps
    # Parse dictionary js
    # indent = 4: print it out nicely with indent of 4
    print json.dumps(js, indent=4)

    # js is a dictionary
    # ["results"] is a list of dictionaries
    # ["results"][0] accesses first object
    # Access geometry dictionary
    # Access location dictionary
    # Pull out lat
    lat = js["results"][0]["place_id"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng

    # Access formatted_address
    # Tip, slowly do print [] until you reach where you want
    location = js['results'][0]['formatted_address']
    print location
