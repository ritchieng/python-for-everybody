import urllib
from BeautifulSoup import *

url =raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of anchor tags
# Each tag is like a dictionary of HTML attributes

# Just want <a .... ></a>
tags = soup('a')

# Look at all the 'a' anchor tags
# Give values of href
for tag in tags:
    print tag.get('href', None)
