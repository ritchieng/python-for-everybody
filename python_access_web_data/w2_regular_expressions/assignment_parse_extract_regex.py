# 1. Import regex
# 2. Read file
# 3. Create
# 4. Look for integers re.findall('[0-9]+', line)
# 5. Convert strings to integers
# 6. Sum integers

# 1. Import regex
import re

# 2. Read file
fhandle = open('regex_sum_279460.txt')

# 3. Create list
numlist = list()

# 4. Look for integers re.findall('[0-9]+', line)
for line in fhandle:
    line = line.rstrip()
    # Create lists of numbers
    num = re.findall('[0-9]+', line)

    # print num
    # confirm that numbers are collated

    # print num
    # shows max 3 in a list

    # Skip blank lists
    if len(num) < 1:
        continue

    elif len(num) == 1:
        # 5. Convert strings to integers
        num1 = int(num[0])
        numlist.append(num1)
    elif len(num) == 2:
        num1 = int(num[0])
        num2 = int(num[1])
        numlist.append(num1)
        numlist.append(num2)
    else:
        num1 = int(num[0])
        num2 = int(num[1])
        num3 = int(num[2])
        numlist.append(num1)
        numlist.append(num2)
        numlist.append(num3)

# 6. Sum integers in a list
sum_num_int = sum(numlist)
print len(numlist)
print sum_num_int