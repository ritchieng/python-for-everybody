# SCRIPT FOR EXTRACTING LOCATION INFORMATION FROM GOOGLE API
# 1. Import urllib and json
# 2. Prompt for location raw_input()
# 3. Contact Google's web service using urllib.urlencode
# 3b. Print URL
# 3c. URL handle, read data and print len(URL)
# 4. Parse JSON using json.loads(url_data)
# 4b. Try and except for error handling
# 5. Pretty print JSON using json.dumps(js, indent=4)
# 6. Access JSON to find 'place_id'

# 1. Import urllib and json
import urllib
import json

# 2. Prompt for location raw_input()
address = raw_input('Enter location: ')


# 3. Contact Google's web service using urllib.urlencode
service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'
url = service_url + urllib.urlencode({'sensor': 'false', 'address': address})

# 3b. Print URL
print 'Retrieving', url

# 3c. URL handle, read data and print len(URL)
url_handle = urllib.urlopen(url)
url_data = url_handle.read()
print 'Retrieved %d characters' % (len(url_data))

# 4. Parse JSON using json.loads(url_data)
# jsh = json.loads(url_data)
# print jsh

# 4b. Try and except for error handling
try:
    js_handle = json.loads(url_data)
except:
    js_handle = None

# 5. Pretty print JSON using json.dumps(js, indent=4)
print json.dumps(js_handle, indent=4)


# 6. Access JSON to find 'place_id'
place = js_handle["results"][0]["place_id"]
print 'Place id', place
