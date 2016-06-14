import re

fhand = open('mbox-short.txt')

# 1. search()
for line in fhand:
    line = line.rstrip()
    # Find 'From:' at the beginning of line
    # ^: beginning of
    # True/false if you find or not
    if re.search('^From:', line):
        print line

# 1. search()
for line in fhand:
    line = line.rstrip()
    # * 0 or more digits, any number of times
    # . matches any character
    if re.search('^X.*:', line):
        print line

# 1. search()
for line in fhand:
    line = line.rstrip()
    # \S --> non-blank character
    # + --> one or more times
    # This basically searches for X- with non-blank characters up to :
    if re.search('^X-\S+:', line):
        print line


# 2. findall()
x = 'my 2 favourite numbers are 19 and 24'
# findall: pull out to fill in list
# [0-9] digits and 1 or more digit
# search condition in x
y = re.findall('[0-9]+', x)
print y

# Find all one or more vowels
y = re.findall('[AEIOU]+', x)
print y

# 3. Greedy matching expanding out to the max :
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print y

# 4. Non-greedy matching to the nearest :
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print y

# \S+ at least one non blank before and after @
# Greedy
# ( ) gives you what you're looking for
# \S --> non-blank character
line = 'From stephen@u.nus.edu do not'
a = re.findall('^From (\S+@\S+)', line)
print a

# Extracting only the domain
line = 'From stephen@u.nus.edu do not'
# find @ in line
# ( ) gives you what you're looking for
# [^ ] non blank
# * 0 or more
b = re.findall('@([^ ]*)', line)
print b

# ^From --> starts From
# .* --> any character before @
# ( ) --> what you will get
# [^ ]* --> non-blank characters as many as them
c = re.findall('^From .*@([^ ]*)', line)
print c

# SPAM CONFIDENCE Example
fhand = open('mbox-short.txt')
numlist = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    # skip those you don't find
    print stuff
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print 'Maximium:', max(numlist)