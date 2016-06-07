# 1. Use file handle to open mbox-short.txt
# 2. Loop through lines to read 'From '
# 3. Split the line to form list of words
# 4. Seek the time
# 5. Split line using ':'
# 6a. Create counts dictionary
# 6b. Map key-value pairs to dictionary
# 7. Convert counts dictionary to list of tuples
# 8. Sort list of tuples based on ascending order
# 9. Print sorted list with a loop

# 1. Use file handle to open mbox-short.txt
fhandle = open('mbox-short.txt')

# 6a. Create counts dictionary
counts = dict()

# 2. Loop through lines to read 'From '
for line in fhandle:
    # 3. Split the line to form list of words
    words = line.split()

    # Guardian pattern for blank lines
    # Error code: list index out of range
    if len(words) < 1:
        continue

    # Exclude 'From:'
    if words[0] == 'From:':
        continue

    # Exclude everything but 'From'
    if words[0] != 'From':
        continue

    # 4. Seek the time
    word = words[5]

    # 5. Split line using ':'
    word = word.split(':')
    num = word[0]

    # 6b. Map key-value pairs to dictionary
    # i. If there is no count for the word, add 0
    # ii. If there is count for the word, add 1
    counts[num] = counts.get(num, 0) + 1

# 7. Convert counts dictionary to list of tuples
counts = counts.items()

# 8. Sort list of tuples based on ascending order
counts_sorted = sorted(counts)

# 9. Print sorted list with a loop
for k, v in counts_sorted:
    print k, v
