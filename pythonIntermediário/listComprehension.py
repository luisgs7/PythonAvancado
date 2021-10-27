lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a1 = [number for number in lista]
print(a1)

a2 = [v * 2 for v in lista]
print(a2)

a3 = [(a, b) for a in lista for b in range(3)]
print(a3)

lista2 = ['Luiz', 'Mauro', 'Pedro']
a4 = [a.replace('u','@').upper() for a in lista2]
print(a4)


tupla = (
    ('chave', 'valor'),
    ('chave1', 'valor1'),
)


a5 = [(b, a) for a, b in tupla]
a5 = dict(a5)
print(a5['valor1'])

lista3 = list(range(100))
a6 = [a for a in lista3 if a % 3 == 0 and a % 8 == 0]
print(a6)

a7 = [a if a % 3 == 0 else 0 for a in lista3]
print(a7)
