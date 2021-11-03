from math import pi
PI = pi


def dobra_lista(lista):
    return [a * 2 for a in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)
