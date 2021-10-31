try:
    a = []
    print(a[1])

except NameError as erro:
    print("Erro do desenvolvedor")

except (IndexError, KeyError) as erro:
    print("Erro de índice ou chave.")

except Exception as erro:
    print("Ocorreu um erro inesperado.")

else:
    pass

finally:
    print("Finally")
