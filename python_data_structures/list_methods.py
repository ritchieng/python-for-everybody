# Constructor, gives an empty list
# Or x = []
x = list()

print type(x)

# This gives you the methods available
print dir(x)

# Appending
x.append('book')
x.append(99)
print x


# Is something in List?
if 99 in x:
    print '99 in x'

if 88 not in x:
    print '88 not in x'

# Ordering List
a = [3, 1, 2, 5, 4]

print a.sort()

print len(a)

print max(a)

print min(a)

print sum(a)
