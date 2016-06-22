# 1. Import ElementTree and SQLite libraries
import xml.etree.ElementTree as ET
import sqlite3

# 2. Call .connect() method to create connection object
connect_db = sqlite3.connect('exercise_db.sqlite')

# 3. Create cursor object
cursor_db = connect_db.cursor()

# 4. Create Tables
# User
# Course
# Member

# Delete table if it exists
cursor_db.execute('DROP TABLE IF EXISTS User')

# Create table
cursor_db.execute('''
    CREATE TABLE IF NOT EXISTS User (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      name TEXT,
      email TEXT
    )
''')

# Delete table if it exists
cursor_db.execute('DROP TABLE IF EXISTS Course')

# Create table
cursor_db.execute('''
    CREATE TABLE IF NOT EXISTS Course (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      title TEXT
    )
''')

# Delete table if it exists
cursor_db.execute('DROP TABLE IF EXISTS Member')

# Create CONNECTOR (Junction) table
cursor_db.execute('''
    CREATE TABLE IF NOT EXISTS Member (
      user_id INTEGER,
      course_id INTEGER,
      role INTEGER,
      PRIMARY KEY(user_id, course_id)
    )
''')

# Insert User and Course Data
# INSERT INTO User (name, email) VALUES ('Jane', 'jane@me.com');
# INSERT INTO User (name, email) VALUES ('Ed', 'ed@me.com');
# INSERT INTO User (name, email) VALUES ('Sue', 'sue@me.com');
# INSERT INTO Course (title) VALUES ('Python');
# INSERT INTO Course (title) VALUES ('SQL');
# INSERT INTO Course (title) VALUES ('PHP');

# Insert Member Data
# INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
# INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
# INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);
#
# INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
# INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);
#
# INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
# INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);


# Select, Join, On and Order By
# SELECT User.name, Member.role, Course.title
# FROM User
# JOIN Member JOIN Course
# ON Member.user_id = User.id AND Member.course_id = Course.id
# ORDER BY Course.title, Member.role DESC, User.name

# Course.title first --> Member.role first --> User.name last