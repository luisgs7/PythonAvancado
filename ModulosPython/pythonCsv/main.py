import csv

with open('clientes.csv', 'r') as arquivo:
    dados = [a for a in csv.DictReader(arquivo)]
    
print('Leitura do arquivo realizada com sucesso.')


with open('clientes2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3],
        ]
    ) 

    for dado in dados:
        escreve.writerow(
            [
                dado['nome'],
                dado['sobrenome'],
                dado['e-mail'],
                dado['telefone'],
            ]
        )

print('Escrita do arquivo realizada com sucesso.')