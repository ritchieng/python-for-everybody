# 1. Get file name
# 2. Open file
# 3. Look for 'From' each line
# 4. Get second word from each line
# 5. Create dictionary
# 6. Map address/count to dictionary
# 7. Count most common using maximum loop

# 1. Get file name
# fname = raw_input('Enter file: ')

# 2. Open file
fhandle = open('mbox-short.txt')

# 5. Create dictionary
counts = dict()

# 3. Look for 'From' each line
for line in fhandle:
    words = line.split()

    # Guardian pattern for blank lines
    if len(words) < 1:
        continue

    # To ignore all sentences starting from "From:"
    if words[0] == 'From:':
        continue

    # To ignore all sentences not starting from "From "
    if words[0] != 'From':
        continue

    word = words[1]
    # 6. Map address/count to dictionary
    counts[word] = counts.get(word, 0) + 1
    # print words

# 7. Count most common using maximum loop
bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword, bigcount
# print counts



