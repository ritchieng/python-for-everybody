fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('From:'):
        print line

# print adds a newline \n to each line therefore explaining the blank lines