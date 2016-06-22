# 1. Import JSON and SQLite libraries
import json
import sqlite3

# 2. Call .connect() method to create connection object
connect_db = sqlite3.connect('roster_role_db.sqlite')

# 3. Create cursor object to send commands
cursor_db = connect_db.cursor()

# 4. Create tables
# Using multiple SQL commands using .executescript()
# Connector table: Member
# Member: 2 foreign keys, 1 composite primary key (concatenated)

cursor_db.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
  id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name  TEXT UNIQUE
);

CREATE TABLE Course (
  id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  title  TEXT UNIQUE
);

CREATE TABLE Member (
  user_id   INTEGER,
  course_id INTEGER,
  role INTEGER,
  PRIMARY KEY (user_id, course_id)
)
''')

# 5 Request file name
fname = raw_input('File name: ')
# 5a. Error handling
if len(fname) < 1:
    fname = 'roster_data_assignment.json'

# JSON Data example
# [
#   [
#     "Charley",
#     "si110",
#     1
#   ],
#   [
#     "Mea",
#     "si110",
#     0
#   ],

# 6. Open and load json
str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    print name, title, role

    # User: Insert, Retrieve and Query
    # Insert Data
    cursor_db.execute('''
      INSERT OR IGNORE INTO User (name)
      VALUES (?)''', (name, ))

    # Retrieve Data
    cursor_db.execute('''
      SELECT id
      FROM User
      WHERE name = ?''', (name, ))

    # Call fetchone() method to query db
    user_id = cursor_db.fetchone()[0]

    # Course: Insert, Retrieve and Query
    # Insert Data
    cursor_db.execute('''
      INSERT OR IGNORE INTO Course (title)
      VALUES (?)''', (title,))

    # Retrieve Data
    cursor_db.execute('''
      SELECT id
      FROM Course
      WHERE title = ?''', (title,))

    # Call fetchone() method to query db
    course_id = cursor_db.fetchone()[0]

    # Member: Insert
    cursor_db.execute('''
      INSERT OR REPLACE INTO Member (user_id, course_id, role)
      VALUES (?, ?, ?)''', (user_id, course_id, role))

    # Commit changes
    connect_db.commit()
