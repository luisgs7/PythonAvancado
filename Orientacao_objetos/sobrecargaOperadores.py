'''
No python, o comportamento dos operadores é definido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuário.
'''

class Retangulo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b
    
    def __repr__(self):
        return f"<class 'Retangulo({self.a}, {self.b})'>"

    def __add__(self, other):
        novo_a = self.a + other.a
        novo_b = self.b + other.b
        return Retangulo(novo_a, novo_b)

    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False
        
    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

    def __eq__(self,other):
        if self.a == other.a and self.b == other.b:
            return True
        else:
            return False

r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
r3 = r1 + r2

print(r1 == r2)
print(r1 == r3)
print(r3)
