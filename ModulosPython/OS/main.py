import os
from utils import formata_tamanho

caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo: ')

conta = 0

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                
                print('\nEncontrei o arquivo: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensão: ', ext_arquivo)
                print('Tamanho: ', tamanho)
                print('Tamanho formatado: ', formata_tamanho(tamanho))

            except PermissionError as e:
                print('Semp permissões.')
            
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            
            except Exception as e:
                print('Erro desconhecido: ', e)


print(f'\n{conta} arquivo(s) encontrado(s).')