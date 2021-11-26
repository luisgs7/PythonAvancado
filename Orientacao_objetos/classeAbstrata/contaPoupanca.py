from conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()