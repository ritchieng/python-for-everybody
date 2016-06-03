# fhand is the handle
fhand = open('mbox.txt')
count = 0

# Python counts the number of lines using the loop
for line in fhand:
    count += 1

print('Line count: ', count)

# Read it all and return to string
inp = fhand.read()

print(inp)
print(len(inp))
print(inp[2: 4])
