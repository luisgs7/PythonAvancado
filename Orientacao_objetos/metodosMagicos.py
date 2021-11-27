class Principal:
    #def __new__(cls, *args, **kwargs):
    #    print('New')

    def __init__(self):
        print("Init")

    def __len__(self):
        return 55

    def __str__(self) -> str:
        return f"<class '{__class__.__name__}'>"
    
    def __call__(self, *args, **kwargs) -> int:
        resultado = 1

        for i in args:
            resultado *= i

        return resultado


a = Principal()
print(len(a))
print(a)

variavel = a(1, 2, 3, 4, 5)
print(variavel)


