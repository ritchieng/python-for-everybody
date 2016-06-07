counts = dict()

fname = raw_input('Key in your file name: ')
fhandle = open('mbox-short.txt')

for line in fhandle:
    line = line.split()
    for word in line:
        counts[word] = counts.get(word, 0) + 1

print 'Counts', counts