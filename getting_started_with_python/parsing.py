# Want to extract domain hotmail.com
data = 'From ritchie_ng@hotmail.com Tues May 31'
at_position = data.find('@')
print(at_position)

space_position = data.find(' ', at_position)
# Starting from at_position, where's the next space
print(space_position)

host = data[at_position + 1: space_position]
print(host)