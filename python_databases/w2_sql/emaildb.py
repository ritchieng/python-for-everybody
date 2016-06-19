# Importing library to talk to SQL db
import sqlite3

# Use db, store db in file emaildb.sqlite
# SQLite Browser to view this
# Create connection object
conn = sqlite3.connect('emaildb.sqlite')
# .cursor() so you can communicate
cur = conn.cursor()

# Call execute() method
# The DROP TABLE statement is used to delete a table.
cur.execute('''
DROP TABLE IF EXISTS Counts''')


# Call execute() methods
# CREATE TABLE
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    # Looping through and retrieving email
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    print email


    # first param: ? is a placeholder to be filled in
    # second param: one tuple --> first thing in tuple to substitute question mark
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, ))

    # This method retrieves the next row of a query result set and
    # returns a single sequence, or None if no more rows are available.
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) 
                    VALUES (?, 1)''', (email, ))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?',
                    (email, ))

    # This statement commits outstanding changes to disk each
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
    conn.commit()

# https://www.sqlite.org/lang_select.html
# DESC so large number on the top
# LIMIT 10: only give 10 out of n records --> top 10 email senders
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

print "Counts:"
for row in cur.execute(sqlstr):
    print str(row[0]), row[1]

cur.close()

