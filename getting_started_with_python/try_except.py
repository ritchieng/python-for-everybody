# Try Fails
first_string = input("What's your age? ")
try:
    first_integer_string = int(first_string)
    # If try fails, except runs.
    # Keep as little code as possible so you know what's failing.
except:
    first_integer_string = -1

print('Your Age', first_integer_string)

# Try Passes
second_string = input("What's your age? ")
try:
    second_integer_string = int(second_string)
    # If try fails, except runs.
except:
    second_integer_string = -1

print('Your Age, Second Try', second_integer_string)

# Proper Error Log
third_strong = input("What's your age? ")
try:
    third_integer_string = int(third_strong)
except:
    third_integer_string = -1

if third_integer_string > 0:
    print('Your age:', third_integer_string)
else:
    print('Error: not a number')
