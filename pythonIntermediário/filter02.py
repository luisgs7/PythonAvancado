from dados import produtos

def filtra(produto):
    if produto['preco'] >= 15:
        return True


nova_lista = list(filter(filtra, produtos))

for produto in nova_lista:
    print(produto)
