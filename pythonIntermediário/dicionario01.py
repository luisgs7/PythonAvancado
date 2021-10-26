d1 = {
    1: 2,
    2: 3,
    3: 4,
}


d2 = {
    'a': 'b',
    'c': 'd',
}


d1.update(d2)
print(d1)


d1.popitem()
print(d1)

d1.pop(2)
print(d1)
