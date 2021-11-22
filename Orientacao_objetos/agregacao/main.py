from classes import CarrinhoDeCompras, Produto


carrinho = CarrinhoDeCompras()

p1 = Produto('Geladeira', 5000)
p2 = Produto('Fogão', 1000)
p3 = Produto('Iphone', 15000)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)

carrinho.lista_produto()

print(carrinho.soma_total())