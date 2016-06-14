# 1. Import urllib and Beautiful Soup
# 2. Request raw URL input
# 3. Read HTML with urllib's urlopen() method
# 4. Parse HTML with BeautifulSoup's BeautifulSoup() method
# 5. Retrieve list of span tags
# 6. Loop through to get numbers

# 1. Import urllib and Beautiful Soup
import urllib
from BeautifulSoup import *

# 2. Request raw URL input
url = raw_input('URL to scrap: ')

# 3. Read HTML with urllib's urlopen() method
html = urllib.urlopen(url).read()

# 4. Parse HTML with BeautifulSoup's BeautifulSoup() method
soup = BeautifulSoup(html)

# 5. Retrieve list of span tags
tags = soup('span')

total = 0
# 6. Loop through to get numbers
for tag in tags:
    # print 'TAG:', tag
    # print 'URL:', tag.get('href', None)
    # print 'Contents:', tag.contents[0]
    # print 'Attrs:', tag.attrs
    num = tag.contents[0]
    # Retrieve number with positions 0 onwards
    num_int = int(num[0:])
    total += num_int

print total




