from typing import Union


def funcao(a: int, b: int) -> Union[int, float]:
    return a / b


a: int = 10
y: float = 20


def soma(a1: int, a2: int) -> int:
    return a1 + a2


print(funcao(3,2))
print(soma(a, y))
