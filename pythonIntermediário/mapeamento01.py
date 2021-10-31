from dados import produtos


def preco(p):
    return round(p['preco'] * 1.15, 2)

precos = map(preco, produtos)

for produto in precos:
    print(produto)
