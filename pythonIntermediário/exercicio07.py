lista_a = [1, 2, 3, 10, 11, 12]
lista_b = [1, 2, 5, 4]

lista_c = zip(
    lista_a,
    lista_b
)

soma = list([sum((a, b)) for a, b in lista_c])
print(soma)
