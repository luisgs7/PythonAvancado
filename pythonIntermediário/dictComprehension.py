
d1 = {f'chave_{a}': a**2 for a in range(5)}


print(d1, type(d1))

lista = [
    ('chave', 'valor'),
    ('chave1', 'valor1'),
]

d1 = {a: b for a, b in lista}
print(d1)

d1 = {a.upper(): b.upper() for a, b in lista}
print(d1)
