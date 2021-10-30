from itertools import groupby, tee

alunos = [
    {'nome1': 'nome', 'nota': 'A'},
    {'nome2': 'nome', 'nota': 'B'},
    {'nome3': 'nome', 'nota': 'C'},
    {'nome4': 'nome', 'nota': 'C'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos, nota: {agrupamento}')
    print()
