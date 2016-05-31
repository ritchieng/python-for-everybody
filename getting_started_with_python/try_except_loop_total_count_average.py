count = 0
total = 0

while True:
    inp = raw_input('Enter a number: ')
    # Don't count here. Because you will count the last entry which is NaN

    # Handle the edge cases
    if inp == 'done':
        break
        # Breaks out of loop to print "Done!"
    if len(inp) < 1:
        break
        # Allows user to enter an empty line to print "Done!"

    # Do the work.
    try:
        num = float(inp)
    except:
        print "Invalid input"
        print " "
        continue
            # continue jumps up to loop without running the code below
    count += 1
        # count = count + 1
    total += num
        # total = total + num
    print num, total, count
    print " "

print " "
print "Results:"
print "Count = ", count
print "Total = ", total
print "Average = ", total / count

