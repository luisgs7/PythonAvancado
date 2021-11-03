from sys import platform as so
from random import randint as rd


print(so)


def randint():
    return 10


for i in range(10):
    print(rd(0, 10))
    print(randint())
