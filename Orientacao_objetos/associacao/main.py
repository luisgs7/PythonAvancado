from classes import Escritor, Caneta, MaquinaDeEscrever


escritor = Escritor("Machado de Assis")
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()