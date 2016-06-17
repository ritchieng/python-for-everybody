# 1. Import json and urllib libraries
# 2. Prompt for URL
# 3. Read the URL using urllib open and read()
# 4. Parse URL using json.loads
# 5. Extract comments from dictionary using loop
# 6. Store counts in list by creating list() and append()
# 7. Sum numbers in list using sum()


# 1. Import json and urllib libraries
import json
import urllib

# 2. Prompt for URL
url = raw_input('Enter location: ')
print 'Retrieving', url

# 3. Read the URL using urllib open and read()
url_handle = urllib.urlopen(url)
url_data = url_handle.read()
print 'Retrieved', len(url_data)

# 4. Parse URL using json.loads
jsp = json.loads(url_data)
# print jsp

# 5. Extract comments from dictionary using loop
l = list()
for u in jsp['comments']:
    num = int(u['count'])
    l.append(num)

print 'Count:', len(l)
print 'Sum:', sum(l)