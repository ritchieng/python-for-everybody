# Tuples are immutable lists with key-value pair
# You can do what you do with lists
    # Loop through them
    # max(tuple)
    # min(tuple)
# CANNOT
    # sort()
    # append()


# Mutable List
x = [1, 2]
x[0] = 2
print x

print " "

# Immutable list or tuple, z
z = (5, 4, 3)
# z[0] = 1
# This does not work as a tuple is immutable
print z[0]

print " "

# Less in-built functions compared to lists
print dir(z)

print " "

# When to use tuples?
# 1. Temporary variables
# 2. Immutable variables
# 3. Saving processing time

# Tupple assignments
(a, b) = (99, 98)
print (a, b)

print " "

# Converting dictionaries to list of tuples to loop through list
d = dict()
d['BMW'] = 10
d['VW'] = 5
for (k, v) in d.items():
    print k, v

print " "

t = d.items()
print t

# Tuples are comparable

# (0, 1, 20) < (5, 1, 2)
# TRUE
# Compares the first only
# If equal, goes to the next value to compare

print " "

# Sorted: takes an unsorted list as input and returns a sorted list
f = sorted(d.items())

for k, v in f:
    print k, v

print " "
# Sort by values instead of key
c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()

for k, v in c.items():
    tmp.append((v, k))
print tmp

tmp = sorted(tmp, reverse=True)
print tmp

