cidades = ['São Paulo', 'Belo Horizonte', 'Colinas', 'Salvador']

estados = ['SP', 'MG', 'TO']

uf = zip(cidades, estados)

print(dict(uf))

#print(next(uf))
print("For")
for cidade in uf:
    print(cidade)

from itertools import zip_longest

cidades_estados = zip_longest(estados, cidades, fillvalue='Estado')

print(list(cidades_estados))
