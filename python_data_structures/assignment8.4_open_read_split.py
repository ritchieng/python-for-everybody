# fname = raw_input('Enter file name: ')
fhandle = open('romeo.txt')
words = []

for line in fhandle:
    line = line.rstrip().split()
    for word in line:
        if word not in words:
            words.append(word)

# Use sorted when the sort() returns None
print sorted(words)

