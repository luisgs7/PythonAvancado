clientes = {
    'cliente1': {
        'nome': 'Luiz',
        'sobrenome': 'jose',
    },
    'cliente2': {
            'nome': 'João',
            'sobrenome': 'Pedro',
        },
}

for cliente_k, cliente_v in clientes.items():
    print(f'Exibindo {cliente_k}')
    for dados_k, dados_v in cliente_v.items():
        print(f'\t{dados_k} = {dados_v}')
