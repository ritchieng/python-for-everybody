greet = ' Hello Bob '

zap = greet.lower()
print(zap)
# Converts to lowercase

large = greet.upper()
print(large)
# Converts to uppercase

what_type = type(greet)
print(what_type)

what_dir = greet.find('lo')
print(what_dir)
# Where is this in the string.

replace_name = greet.replace('Bob', 'Jane')
print(replace_name)
# It doesn't change the value of greet

replace_letter = greet.replace('o', 'X')
print(replace_letter)

strip_left = greet.lstrip()
strip_right = greet.rstrip()
strip_all = greet.strip()

print(strip_all)
print(strip_left)
print(strip_right)

start_with = greet.startswith('Hello')
print(start_with)
