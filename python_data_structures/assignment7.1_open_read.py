# Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.

# Use words.txt as the file name
fname = raw_input('Enter file name: ')

# Neat Trick to load file
if len(fname) == 0:
    fname = 'words.txt'

# File handler allows iteration
fhand = open(fname)

for line in fhand:
    line = line.rstrip().upper()
    # rstrip then upper
    print line

