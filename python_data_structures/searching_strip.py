fhand = open('mbox.txt')

for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print line

# This strips the line of a new blank line by removing all characters after the end of the string
# This means any whitespace characters are removed like \n in each space