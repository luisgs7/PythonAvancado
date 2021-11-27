class Arquivo:
    def __init__(self, arquivo, modo):
        print('Init')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('retornando arquivo')
        return self.arquivo

    def __exit__(self, exec_type, exec_val, exec_tb):
        print('Exit')
        self.arquivo.close()


with Arquivo('app.txt', 'w') as arquivo:
    arquivo.write('Ola pessoal')