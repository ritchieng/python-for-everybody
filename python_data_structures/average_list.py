# New way to do it with list compared to using single variables
# Performance: this stores data then calculate and requires more memory

numlist = list()

while True:
    inp = raw_input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)

print 'Average:', average
