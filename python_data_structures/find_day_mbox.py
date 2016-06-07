fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    # Skipping lines without 'From '
    if not line.startswith('From '):
        continue
    words = line.split()

    # Double split pattern
    email = words[1]
    pieces_email = email.split('@')
    print pieces_email[1]

    print words[2]

# Format of line without split
# From cwen@iupui.edu Thu Jan  3 16:34:40 2008
# 1: email
# 2: day
# 3: month
# 4: day of month


