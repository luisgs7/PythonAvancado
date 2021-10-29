import sys

l1 = [a for a in range(10000)]
print(type(l1))

l2 = (a for a in range(10000))
print(type(l2))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

print(next(l2))
print(next(l2))
print(next(l2))
