fname = raw_input('Enter file name: ')
fhandle = open(fname)
count = 0

for line in fhandle:
    line = line.rstrip()
    word = line.split()

    # Guardian pattern
    if len(word) < 1:
        continue

    # Requires a guardian pattern due to empty line
    if word[0] != 'From':
        continue
    else:
        # Counting number
        count += 1

    # Shows you have retrieved the emails
    print word[1]

print "There were", count, "lines in the file with From as the first word"