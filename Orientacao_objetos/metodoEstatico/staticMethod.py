from random import randint


class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def ano_nascimento(cls, nome, ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


print(Pessoa.gera_id())

p1 = Pessoa.ano_nascimento('Pedro', 1950)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

print(p1.gera_id())

p2 = Pessoa('José', 39)
print(p2)
p2.get_ano_nascimento()


