x = 'From marquard@uct.ac.za'
find_at = x.find('@')
print(find_at)
find_dot = x.find('.')
print(find_dot)

uct_cut = x[find_at + 1: find_dot]
print(uct_cut)

print(len('banana')*7)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])