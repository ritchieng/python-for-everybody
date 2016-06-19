# 1. Import sqlite3
# 2. Call .connect() method to create connection object
# 3. Create cursor object
# 4. Delete table if it exists
# 5. Create table with domains and counts as attributes
# 6. Request file name
# 7. Create file handle
# 8. Loop through file to retrieve domain of emails
# 9a. Retrieve data
# 9b. Call fetchone() method to query db
# 10. if/else statement similar to get()
# 11. Commit changes with commit()
# 12. Print counts

# 1. Import sqlite3
import sqlite3

# 2. Call .connect() method to create connection object
connect_db = sqlite3.connect('domain_db.sqlite')

# 3. Create cursor object
cursor_db = connect_db.cursor()

# 4. Delete table if it exists
cursor_db.execute('''
DROP TABLE IF EXISTS Counts''')

# 5. Create table with emails and counts as attributes
cursor_db.execute('''
CREATE TABLE Counts(
  org TEXT,
  count INTEGER)''')

# 6. Request file name
fname = raw_input('File name: ')

# 7. Create file handle
fhandle = open(fname)

# 8. Loop through file to retrieve domain of emails
for line in fhandle:
    if not line.startswith('From: '):
        continue
    line = line.split()
    email = line[1]
    email = email.split('@')
    org = email[1]

    # Using cursor as iterator
    # 9a. Retrieve data
    cursor_db.execute('SELECT count FROM Counts WHERE org = ? ', (org,))

    # 9b. Call fetchone() method to query db
    row = cursor_db.fetchone()

    # 10. if/else statement similar to get()
    if row is None:
        cursor_db.execute('''INSERT INTO Counts (org, count)
                          VALUES (?, 1)''', (org, ))
    else:
        cursor_db.execute('''UPDATE Counts
                          SET count = count + 1
                          WHERE org = ?''', (org, ))

    # 11. Commit changes with commit()
    connect_db.commit()

# 12. Print counts
sqlstr = '''SELECT org, count FROM Counts ORDER BY count DESC'''

for row in cursor_db.execute(sqlstr):
    print row[0], row[1]

# 13. Close cursor (communication)
cursor_db.close()