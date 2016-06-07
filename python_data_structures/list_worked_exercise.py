fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    word = line.split()
    # Use a debug line to see what's happening before the line that has issue
        # print '++', line
        # print word
        # You will see that there's an issue with a blank line

    # Fix to the code below using a guardian pattern
    if word == []:
        continue

    # This code dies whenever there's a blank line
    if word[0] != 'From':
        continue

    print word[2]
