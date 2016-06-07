c = {'a': 10, 'b': 1, 'c': 22}

# [ ] list comprehension creates a dynamic list

print sorted([(v, k) for (k, v) in c.items()])
