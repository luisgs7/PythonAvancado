from pythonIntermediário.pacotes.vendas.formata import preco as preco2
from vendas.calc_preco import aumento, desconto


preco: float = 49.90
preco_com_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)


preco_com_desconto = desconto(valor=preco, porcentagem=15, formata=True)
print(preco_com_desconto)

print(preco2.real(53.5892))
