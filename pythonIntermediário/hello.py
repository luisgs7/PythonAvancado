
def hello(nome, msg='Olá'):
    nome = nome.replace('u', '3')
    msg = msg.replace('e', '5')
    return f'{msg} {nome}'

saudacao = hello('Luís Pedro', msg='Hello');

print(saudacao)