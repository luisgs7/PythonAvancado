'''
Polimorfismo é o principio que permite que classes derivadas de uma 
superclasse tenham métodos iguais (de mesma assinatura) mas comportamentos
diferentes.
Mesma assinatura = Mesma nome, quantidade e tipo de parâmetros
'''

from abc import ABC, abstractmethod


class Principal(ABC):
    @abstractmethod
    def fala(self, msg): pass


class Filho(Principal):
    def fala(self, msg):
        print(f'{__class__.__name__} está falando {msg}')

class Sobrinho(Principal):
    def fala(self, msg):
        print(f'{__class__.__name__} está falando {msg}')


filho = Filho()
filho.fala('sobre Python')

sobrinho = Sobrinho()
sobrinho.fala('sobre Kotlin')
        