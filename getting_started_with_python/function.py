# Function is some reusable code --> helps to reduce repeat codes
# Takes arguments as input
# Does computation then returns a result

# def to define a function
# function_name(argument) to invoke with argument

def hello():
    print('Hello!')
    name = input('Who are you? ')
    print('Welcome ' + name + ".")

hello()
# Invoking function

# Built-in function
big = max('1, 2, 3')
print(big)
# Input: string '1, 2, 3'
# Function: max() --> takes input to produce output
# Result: '3'
