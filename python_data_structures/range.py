# Range returns a list of numbers from 0 to n - 1, n is the parameter

print range(4)

friends = ['Ritchie', 'John', 'Sally']
length_friends = len(friends)

print range(length_friends)

# This is preferred
for friend in friends:
    print 'Happy New Year!', friend

# Equivalent Loop where you need value of i
for i in range(length_friends):
    friend = friends[i]
    print 'Happy New Year!', friend
