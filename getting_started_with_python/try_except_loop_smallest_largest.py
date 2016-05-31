largest = None
smallest = None

while True:
    num = raw_input('Enter a number: ')

    # Handle edge cases
    if num == "done":
        break
    if len(num) < 1:
        break
        # Allows user to press enter to complete

    # Work is done
    try:
        num_int = float(num)
        # If try fails, except runs
    except:
        print "Invalid input"
        continue
            # Jumps to the start of the loop without running any code below this line

    if smallest is None:
        smallest = num
        # This will be permanently false after the first iteration.
    elif num < smallest:
        smallest = num
        # Replaces the iteration variable with smaller input num

    if largest is None:
        largest = num
        # This will be permanently false after the first iteration.
    elif num > largest:
        largest = num
        # Replaces the iteration variable with larger input num

print "Maximum is " + largest
print "Minimum is " + smallest
