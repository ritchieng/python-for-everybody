# Dictionaries store key-value pairs
# They are like list() except that they use keys instead of numbers to look up values
purse = dict()

# keys: money and candy
purse['money'] = 12
purse['candy'] = 3

print purse

# Dictionary is good for adding the number of counts of candy
purse['candy'] += 2

print purse
print purse['candy']

# Check if key in dictionary
print 'candy' in purse
    # Returns true

# You can create a dictionary using curly
bag = {'chuck:': 1, 'ritchie': 0}
print bag

# Common pattern of counting number of names
counts = dict()
names = ['csev', 'qudas', 'john', 'john']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print counts

# get built-in function - new idiom
# first parameter: key name
# second parameter: value to give back if key does not exist
## print counts.get(name, 0)

# Simplified counting with get()

for name in names:
    counts[name] = counts.get(name, 0) + 1
    # No entry: 0
    # Entry: +1
print counts

# This assigns key to the key
for key in counts:
    print key, counts[key]

# Convert dictionaries to list for keys
print counts.keys()

# Convert dictionaries to list for values
print counts.values()

# Convert dictionaries to list for tuples (key-value pairs)
print counts.items()

# Two iteration variables
for a, b in counts.items():
    print a, b
