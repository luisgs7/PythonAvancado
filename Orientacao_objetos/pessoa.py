from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, estudando=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.estudando = estudando
        self.falando = falando

    def falar(self, assunto):
        if self.estudando:
            print(f'{self.nome} não pode falar estudando.') 
            return 

        if self.falando:
            print(f'{self.nome} está falando sobre {assunto}') 
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        
        print(f'{self.nome} parou de falar.')
        self.falando = False

    def estudar(self, conteudo):
        if self.estudando:
            print(f'{self.nome} já está comendo.')
            return 

        if self.falando:
            print(f'{self.nome} não pode estudar falando.')
            return

        print(f'{self.nome} está estudando {conteudo}.')
        self.estudando = True

    def parar_estudar(self):
        if not self.estudando:
            print(f'{self.nome} não está estudando.')
            return
        
        print(f'{self.nome} parou de estudar.')
        self.estudando = False

    
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
