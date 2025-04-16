from __future__ import annotations
import datetime
class Servico:
    def __init__(self, nome: str, descricao: str, preco: float) -> None:
        self.nome: str = nome
        self.descricao: str = descricao
        self.preco: float = preco
        self.data_criacao: datetime.datetime = datetime.datetime.now()
        self.data_conclusao: datetime.datetime | None = None
    def update(self, **kwargs) -> None:
        if "nome" in kwargs:
            self.nome = kwargs["nome"]
        if "descricao" in kwargs:
            self.descricao = kwargs["descricao"]
        if "preco" in kwargs:
            self.preco = kwargs["preco"]
    def concluir(self) -> None:
        self.data_conclusao = datetime.datetime.now()
    def __repr__(self) -> str:
        return f"Servico(nome={self.nome}, preco={self.preco})"
