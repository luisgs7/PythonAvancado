import sys
import time


def gera():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel

a = gera()
'''
print(next(a))
print(next(a))
print(next(a))
'''
for v in a:
    print(v)
