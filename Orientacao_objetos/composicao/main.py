from classe import Cliente


cliente1 = Cliente('Pedro', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_endereco()
del cliente1
print()


cliente2 = Cliente('José', 50)
cliente2.insere_endereco('Palmas', 'TO')
print(cliente2.nome)
cliente2.lista_endereco()
del cliente2
print()

print("### OK ###")
