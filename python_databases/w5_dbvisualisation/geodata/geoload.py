# 1. Imports
import urllib
import sqlite3
import json
import time
import ssl

# 2. API's URL to connect
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

# Deal with SSL certificate anomalies Python > 2.7
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
scontext = None

# 2. Call .connect() method to create connection object
conn = sqlite3.connect('geodata.sqlite')

# 3. Create cursor object
cur = conn.cursor()

# 4. Create table
cur.execute('''
    CREATE TABLE IF NOT EXISTS Locations (
        address TEXT,
        geodata TEXT
    )
''')

# Open input data
fh = open("where.data")
count = 0

# Loop through data
for line in fh:
    if count > 200:
        break
    address = line.strip()
    print ''
    # Buffer to force it to what we want
    # Retrieve data
    cur.execute('''
      SELECT geodata
      FROM Locations
      WHERE address= ?''', (buffer(address), ))

    try:
        # Query data
        # fetchone() grabs a row
        # [0] grabs first column
        data = cur.fetchone()[0]
        print "Found in database ",address
        continue
    except:
        pass

    print 'Resolving', address
    # Create URL
    url = serviceurl + urllib.urlencode({"sensor":"false", "address": address})
    print 'Retrieving', url

    # Open URL
    uh = urllib.urlopen(url, context=scontext)

    # Read URL
    data = uh.read()
    print 'Retrieved',len(data),'characters',data[:20].replace('\n',' ')
    count = count + 1
    try: 
        js = json.loads(str(data))
        # print js  # We print in case unicode causes an error
    except:
        # If bad JSON
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print '==== Failure To Retrieve ===='
        print data
        break

    # SQL Command
    cur.execute('''INSERT INTO Locations (address, geodata) 
            VALUES ( ?, ? )''', (buffer(address), buffer(data)))

    # Write to disk to ensure we've data if it blows up halfway
    conn.commit() 
    time.sleep(1)

print "Run geodump.py to read the data from the database so you can visualize it on a map."
