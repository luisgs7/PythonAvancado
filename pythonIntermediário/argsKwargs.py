def func(*args):
    print(args)


lista = [1, 2, 3, 4, 5]


print(*lista, sep='-')

print(func(*lista))


def func2(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    print(kwargs)

    if idade is not None:
        print(idade)
    else:
        print('Idade não informada')


lista = [1, 2, 3, 4, 5]
lista1 = [10, 20, 30, 40, 50]

func2(*lista, *lista1, idade=30, nome='Pedro')
