import sys
import time

def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.01)
    return r

g = gera()

for v in g:
    print(v)