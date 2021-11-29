from dataclasses import astuple, dataclass, asdict


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Invalid type {type(self.nome).__name__} != str em {self}'
            )

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    
p1 = Pessoa('João', 'José')
p2 = Pessoa('João', 'José')

print(p1)
print(p1.nome_completo)
print(asdict(p1))
print(astuple(p1))
print(p1 == p2)
