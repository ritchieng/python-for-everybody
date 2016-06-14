# Using urllib which is easier than socket
# socket is like a phonecall where you determine the connection

import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
print type(fhand)
# for line in fhand:
#     print line.strip()

# You can count the words!

counts = dict()
for line in fhand:
    print line.strip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print counts