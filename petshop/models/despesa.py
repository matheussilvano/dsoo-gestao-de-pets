from __future__ import annotations
class Despesa:
    def __init__(self, descricao: str, valor: float) -> None:
        self.descricao: str = descricao
        self.valor: float = valor
    
    def update(self, **kwargs) -> None:
        if "descricao" in kwargs:
            self.descricao = kwargs["descricao"]
        if "valor" in kwargs:
            self.valor = kwargs["valor"]
    
    def __repr__(self) -> str:
        return f"Despesa({self.descricao}, valor={self.valor})"
