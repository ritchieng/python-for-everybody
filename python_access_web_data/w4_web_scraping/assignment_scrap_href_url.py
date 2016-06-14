# 1. Import urllib and Beautiful Soup
# 2. Request raw URL input, count and position
# 3. Read HTML with urllib's urlopen() method
# 4. Parse HTML with BeautifulSoup's BeautifulSoup() method
# 5. Retrieve list of anchor a tags
# 6. Loop through to get names
# 7. Get new url based on (position - 1) due to nature of counts request
# 8. Delete the whole list for a new iteration through (3) to (7)

# 1. Import urllib and Beautiful Soup
import urllib
from BeautifulSoup import *

# 2. Request raw URL input, count and position
url = raw_input('Enter URL to scrap: ')
count = raw_input('Enter count: ')
count = int(count)
position = raw_input('Enter position: ')
position = int(position)

tag_list = list()
# Repeats this count number of times
for i in range(count):
    print "Retrieving:", url
    # 3. Read HTML with urllib's urlopen() method
    html = urllib.urlopen(url).read()

    # 4. Parse HTML with BeautifulSoup's BeautifulSoup() method
    soup = BeautifulSoup(html)

    # 5. Retrieve list of anchor a tags
    tags = soup('a')

    # 6. Loop through to append tags to a list tag_list
    for tag in tags:
        tag_list.append(tag)

    # 7. Get new url based on (position - 1) due to nature of counts request
    url = tag_list[position - 1].get('href', None)
    print tag_list

    # 8. Delete the whole list for a new iteration through (3) to (7)
    del tag_list[:]

print "Retrieving", url