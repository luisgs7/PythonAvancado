from dados import pessoas

def filtra(pessoa):
    if pessoa['idade'] > 20:
        return True

p = filter(filtra, pessoas)

for pessoa in p:
    print(pessoa)