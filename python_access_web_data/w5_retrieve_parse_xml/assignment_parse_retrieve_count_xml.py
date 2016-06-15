# 1. Import urllib and xml.etree.ElementTree
# 2. Prompt for URL using raw_input()
# 2b. Print Retrieving, url
# 3a. Read url using urllib method urlopen(url).read()
# 3b. Count length of data
# 4. Parse url
# 4a. Producing structure of grabbing the tree of nodes: de-serialization
# 4b. Grab all the count nodes
# 5. Extract comment counts from XML using loop
# 6. Compute the sum of numbers

# 1. Import urllib and xml.etree.ElementTree
import urllib
import xml.etree.ElementTree as ET

# 2. Prompt for URL using raw_input()
url = raw_input('Enter location: ')

# 2b. Print Retrieving, url
print 'Retrieving', url

# 3a. Read url using urllib method urlopen(url).read()
data = urllib.urlopen(url).read()

# 3b. Count length of data
print 'Retrieving %d characters' % (len(data))

# 4a. Producing structure of grabbing the tree of nodes: deserialization
tree = ET.fromstring(data)

# 4b. Grab all the count nodes
comments = tree.findall('.//comment')

lst = list()
# 5. Extract comment counts from XML using loop
for item in comments:
    count = item.find('count').text
    count = int(count)
    lst.append(count)

print sum(lst)