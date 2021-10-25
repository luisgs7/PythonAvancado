# 01
def ola(saudacao=" Bom dia", nome="Pedro"):
    print(saudacao, nome)


ola()


# 02
def soma(n1, n2, n3):
    return n1 + n2 + n3


print(soma(2, 3, 4))


# 03
def somarporcentagem(valor, porcentagem):
    return (valor * (porcentagem / 100)) + valor


print(somarporcentagem(50, 10))


# 04
def fizzbuzz(parametro):
    if parametro % 3 == 0 and parametro % 5 == 0:
        return 'FizzBuzz'
    elif parametro % 5 == 0:
        return 'Buzz'
    elif parametro % 3 == 0:
        return 'Fizz'
    else:
        return parametro


from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fizzbuzz(aleatorio))
