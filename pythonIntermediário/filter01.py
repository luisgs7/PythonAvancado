from dados import produtos

nova_lista = list(filter(lambda p: p['preco'] > 10, produtos))

for produto in nova_lista:
    print(produto)
