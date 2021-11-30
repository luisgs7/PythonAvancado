from dados import *
import json


with open('clients.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)


with open('clients.json', 'r') as arquivo:
    dados = json.load(arquivo)


for chave, valor in dados.items():
    print(chave)
    print(valor)