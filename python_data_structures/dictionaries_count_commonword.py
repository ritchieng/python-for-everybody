name = raw_input('Enter file: ')
handle = open(name, 'r')
text = handle.read()
words = text.split()

# Full dictionary with key-value pairs of words and counts of each words
counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1

# Find largest key-value pair

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword, bigcount