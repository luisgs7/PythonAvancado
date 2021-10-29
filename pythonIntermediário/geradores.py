lista = [0, 1, 2, 3, 4, 5]

#lista = 'String'

print(hasattr(lista, '__iter__'))

lista = iter(lista)

print(hasattr(lista, '__next__'))

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

import sys

lista = list(range(10))

print(sys.getsizeof(lista))
