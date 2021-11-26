from contaPoupanca import ContaPoupanca
from contaCorrente import ContaCorrente


cp = ContaPoupanca(111, 222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(1)
cp.sacar(5)

print("##########################")
cc = ContaCorrente(agencia=4444, conta=555, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)