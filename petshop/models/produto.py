from __future__ import annotations
class Produto:
    def __init__(self, nome: str, quantidade_estoque: int, custo_unitario: float) -> None:
        self.nome: str = nome
        self.quantidade_estoque: int = quantidade_estoque
        self.custo_unitario: float = custo_unitario
    def update(self, **kwargs) -> None:
        if "nome" in kwargs:
            self.nome = kwargs["nome"]
        if "quantidade_estoque" in kwargs:
            self.quantidade_estoque = kwargs["quantidade_estoque"]
        if "custo_unitario" in kwargs:
            self.custo_unitario = kwargs["custo_unitario"]
    def baixar_estoque(self, quantidade: int) -> None:
        if quantidade > self.quantidade_estoque:
            raise ValueError(f"Estoque insuficiente para {self.nome}.")
        self.quantidade_estoque -= quantidade
    def __repr__(self) -> str:
        return f"Produto(nome={self.nome}, estoque={self.quantidade_estoque})"
