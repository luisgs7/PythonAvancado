from itertools import count

cidades = ['São Paulo', 'Belo Horizonte', 'Colinas', 'Salvador']

estados = ['SP', 'MG', 'TO']

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Colinas', 'Palmas']
estados = ['SP', 'MG', 'TO']

cidades_estados = zip(
    indice,
    estados,
    cidades,
)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)
