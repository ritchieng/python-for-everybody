smallest = None
# Seen nothing so far, so will wait.

print('Before', smallest)

for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    # This will happen the first time where smallest = 9
    # After the first time, it'll be permanently false
    elif value < smallest:
        smallest = value
    # This runs until the loop iterates through the array
    print(smallest, value)

print('After', smallest)

# Only use is when checking for None or False or True
# Other times, use comparison operator ==
