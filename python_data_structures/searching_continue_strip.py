fhand = open('mbox.txt')

for line in fhand:
    line = line.rstrip()
    # Skip all other lines
    if not line.startswith('From:'):
        continue
    # Process the lines we want
    print line
