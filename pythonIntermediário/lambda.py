
lista = [
    ['P1', 13],
    ['P2', 10],
    ['P3', 9],
    ['P4', 45]
]

print(sorted(lista, key=lambda i: i[1], reverse=True))
print(lista)
