nome = 'José Pedro'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))

print('FOR - 01')

for letra in gerador:
    print(letra)

print('FOR - 02')

for letra in gerador:
    print(letra)
