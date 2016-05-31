x = input('What number do you like?')
x = int(x)
# Convert the input into an integer for use with comparison operators

if x < 2:
    print('Below 2')
elif x < 20:
    print('Below 20')
elif x < 10:
    print('Below 10')
    # This will never run.
else:
    print('Above 20')
