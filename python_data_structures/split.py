abc = 'With three words'

# Finds the spaces and split them into a list of strings
stuff = abc.split()
print stuff
print len(stuff)
print stuff[0]

# Can access through a loop
for w in stuff:
    print w

# Many spaces = 1 space
line = 'A lot        of spaces'
line_split = line.split()
print line_split

# Split based on other characters; not spaces
line_semicolon = 'first; second; third'
line_semicolon_split = line_semicolon.split('; ')
print line_semicolon_split


