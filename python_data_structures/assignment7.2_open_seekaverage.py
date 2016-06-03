fname = raw_input('Enter file name: ')
fhandle = open(fname)

x = 'X-DSPAM-Confidence:'
y = len(x)
count = 0
total = 0

# print y
# This would show that the number of characters is 19

# print x[18:]
# This would show that character 19 is ':'

for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        line_number = line[19:]
        line_float = float(line_number)

        count += 1
        # Loop, iterates through all numbers to count number of numbers

        total += line_float
        # Loop, iterates through all numbers to count sum of numbers

        # print line_float
        # This shows that we have successfully extracted the floating numbers

print 'Number of numbers:', count
# This would show that the number of numbers is 27

print 'Sum of numbers:', total
# This would show that total is 20.2694

print 'Average of numbers:', total / count

