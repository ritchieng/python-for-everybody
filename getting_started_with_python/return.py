# Return Values
# Function can return a value
# If you want to do something in the function, use return.

def greet(lang):
    # lang is the parameter
    if lang == 'es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    else:
        return "Hello"

print(greet('fr'), "Monster")
# fr is the argument
print(greet('es'), "Monster")
# es is the argument
print(greet('en'), "Ritchie")
# en is the argument
