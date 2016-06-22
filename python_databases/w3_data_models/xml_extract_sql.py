# Import ET for parsing XML
import xml.etree.ElementTree as ET
import sqlite3

# Call .connect() method to create connection object
connect_db = sqlite3.connect('trackdb.sqlite')

# Create cursor object
cursor_db = connect_db.cursor()

# Make tables if they do not exist

# Create ARTIST TABLE
cursor_db.execute('''
    CREATE TABLE IF NOT EXISTS Artist (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      name TEXT UNIQUE
    )
''')

# Create ALBUM TABLE
cursor_db.execute('''
    CREATE TABLE IF NOT EXISTS Album (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      artist_id INTEGER,
      title TEXT UNIQUE
    )
''')

# TRACK TABLE
cursor_db.execute('''
    CREATE TABLE IF NOT EXISTS Track (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      title TEXT UNIQUE,
      album_id INTEGER,
      len INTEGER,
      rating INTEGER,
      count INTEGER
    )
''')

# Request file name
fname = raw_input('Enter file name: ')
if len(fname) < 1:
    fname = 'Library.xml'


# Parse XML using ET
stuff = ET.parse(fname)
# findall() returns a list of matching Elements
# find() efficiently returns only the first match
# findtext() returns the .text content of the first match
all = stuff.findall('dict/dict/dict')
print 'Dict count:', len(all)

# Define lookup method
def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

for entry in all:
    if lookup(entry, 'Track ID') is None:
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None:
        continue

    print name, artist, album, count, rating, length

    # ARTIST IDIOM
    # If artist don't exist, insert
    # If exist, ignore
    cursor_db.execute('''INSERT OR IGNORE INTO Artist (name)
      VALUES (?)''', (artist, ))
    # Retrieve Data
    cursor_db.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
    # Call fetchone() method to query db
    artist_id = cursor_db.fetchone()[0]

    # ALBUM IDIOM
    # Album has foreign key to artist
    cursor_db.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
      VALUES (?, ?)''', (album, artist_id))
    cursor_db.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cursor_db.fetchone()[0]

    # TRACK IDIOM
    cursor_db.execute('''INSERT OR REPLACE INTO Track
      (title, album_id, len, rating, count)
      VALUES (?, ?, ?, ?, ?)''',
      (name, album_id, length, rating, count))

    # Commit
    connect_db.commit()