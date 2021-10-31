from functools import reduce

from dados import lista, produtos, pessoas

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos / len(produtos))

soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(round(soma_idades / len(pessoas)))
