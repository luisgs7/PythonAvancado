import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Pedro', 'Jose']}


v = copy.deepcopy(d1)

v[1] = 'Lucas'
v['d'][0] = 'Lorenna'

print(d1)
print(v)
