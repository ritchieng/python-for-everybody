# File handle to open the file
fhand = open('romeo.txt')

# Create dictionary
counts = dict()

# Populate dictionary
for line in fhand:
    # Split the words for looping
    words = line.split()
    # Loop through words
    for word in words:
        # 1. If there is no count for the word, add 0
        # 2. If there is count for the word, add 1
        counts[word] = counts.get(word, 0) + 1

# Create list
lst = list()

# Convert to list
for key, val in counts.items():
    lst.append((val, key))
    # Create list for sorting based on value

# Sort based on highest value
lst.sort(reverse=True)

# Print 10 most common words based on key and value
for val, key in lst[:10]:
    print key, val