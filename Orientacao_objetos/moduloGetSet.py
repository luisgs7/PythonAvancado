# SETTER = CONFIGURANDO UM VALOR (=)
# GETTER = OBTER UM VALOR (.)

class Pessoa:
    def __init__(self):
        self._nome = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def sobrenome(self):
        return 'Não tem!'
    
p1 = Pessoa()
print(p1.nome)

p1.nome = 'José'
print(p1.nome)
print(p1.sobrenome)