from dados import lista
'''
nova_lista = list(filter(lambda l: l > 5, lista))
'''
nova_lista = list([a for a in lista if a > 5])
print(nova_lista)
