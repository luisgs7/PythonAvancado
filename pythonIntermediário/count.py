from itertools import count

contator = count(start=1, step=2)

for valor in contator:
    print(round(valor, 2))

    if valor >= 10 or valor <= -10:
        break