'''
Em Python tudo é um objeto: incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasse
'''

class Pai:
    nome = 'Ola'


A = type(
    'A',
    (Pai,),
    {
        'attr': 'Olá Mundo'
    }
)


a = A()
print(a.nome)
print(a.attr)