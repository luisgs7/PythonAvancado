from dados import pessoas

def idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p

nomes = map(idade, pessoas)

for pessoa in nomes:
    print(pessoa)
