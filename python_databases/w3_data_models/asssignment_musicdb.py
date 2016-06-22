# 1. Import ElementTree and SQLite libraries
import xml.etree.ElementTree as ET
import sqlite3

# 2. Call .connect() method to create connection object
connect_db = sqlite3.connect('trackdb_assign.sqlite')

# 3. Create cursor object
cursor_db = connect_db.cursor()

# 4. Create Tables
# Artist
# Genre
# Album
# Track

# Delete table if it exists
cursor_db.execute('''
DROP TABLE IF EXISTS Artist''')

# 4a. Create ARTIST TABLE
cursor_db.execute('''
    CREATE TABLE IF NOT EXISTS Artist (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      name TEXT UNIQUE
    )
''')

# Delete table if it exists
cursor_db.execute('''
DROP TABLE IF EXISTS Genre''')

# 4b. Create GENRE TABLE
cursor_db.execute('''
    CREATE TABLE IF NOT EXISTS Genre (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      name TEXT UNIQUE
    )
''')

# Delete table if it exists
cursor_db.execute('''
DROP TABLE IF EXISTS Album''')

# 4c. Create ALBUM TABLE
cursor_db.execute('''
    CREATE TABLE IF NOT EXISTS Album (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      artist_id INTEGER,
      title TEXT UNIQUE
    )
''')

# Delete table if it exists
cursor_db.execute('''
DROP TABLE IF EXISTS Track''')

# 4d. TRACK TABLE
cursor_db.execute('''
    CREATE TABLE IF NOT EXISTS Track (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      title TEXT UNIQUE,
      album_id INTEGER,
      genre_id INTEGER,
      len INTEGER,
      rating INTEGER,
      count INTEGER
    )
''')

# 5 Request file name
fname = raw_input('File name: ')
# 5a. Error handling
if len(fname) < 1:
    fname = 'Library.xml'

# 6. Parse XML using ElementTree
stuff = ET.parse(fname)

# 7. Find all keys and text
# Dictionary nested 3x
all = stuff.findall('dict/dict/dict')
# print 'Dictionary count:', len(all)

# 8. Define lookup method to seek stuff you want
def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

# 9. Loop through data to find necessary information
# Name
# Artist
# Album
# Play Count
# Rating
# Total Time
for entry in all:
    if lookup(entry, 'Track ID') is None:
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')

    if name is None or artist is None or album is None or genre is None:
        continue

    # print name, artist, album, genre, count, rating, length

    # 10. Idioms to place data into database

    # 10a. Artist Idiom
    # If artist don't exist, insert
    # If exist, ignore
    cursor_db.execute('''INSERT OR IGNORE INTO Artist (name)
         VALUES (?)''', (artist,))
    # Retrieve Data
    cursor_db.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    # Call fetchone() method to query db
    artist_id = cursor_db.fetchone()[0]

    # 10b. Genre Idiom
    # If genre don't exist, insert
    # If exist, ignore
    cursor_db.execute('''INSERT OR IGNORE INTO Genre (name)
             VALUES (?)''', (genre,))
    # Retrieve Data
    cursor_db.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    # Call fetchone() method to query db
    genre_id = cursor_db.fetchone()[0]

    # 10c. ALBUM IDIOM
    # Album has foreign key to artist
    cursor_db.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
          VALUES (?, ?)''', (album, artist_id))
    cursor_db.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cursor_db.fetchone()[0]

    # 10d. TRACK IDIOM
    cursor_db.execute('''INSERT OR REPLACE INTO Track
          (title, album_id, genre_id, len, rating, count)
          VALUES (?, ?, ?, ?, ?, ?)''',
                      (name, album_id, genre_id, length, rating, count))

    # Commit
    connect_db.commit()

cursor_db.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track
    JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID AND Track.album_id = Album.id
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3''')

