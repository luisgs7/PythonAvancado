from contextlib import contextmanager


@contextmanager
def funcao(arquivo, modo):
    try:
        print('Open file')
        arquivo = open(arquivo, modo)
        yield arquivo
    
    finally:
        print('Close file')
        arquivo.close()

with funcao('app.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')