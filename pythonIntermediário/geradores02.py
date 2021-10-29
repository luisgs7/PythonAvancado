import sys
import time

def gera():
    for n in range(100):
        yield n
        time.sleep(0.01)

g = gera()

#for v in g:
#    print(v)

print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
