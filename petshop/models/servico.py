from __future__ import annotations
import datetime
from typing import List, Tuple, Optional
from models.produto import Produto

class Servico:
    def __init__(self, nome: str, descricao: str, preco: float,
                 produtos_usados: Optional[List[Tuple[Produto, int]]] = None) -> None:
        self.nome: str = nome
        self.descricao: str = descricao
        self.preco: float = preco
        self.data_criacao: datetime.datetime = datetime.datetime.now()
        self.data_conclusao: datetime.datetime | None = None
        self.produtos_usados: List[Tuple[Produto, int]] = produtos_usados or []

    def update(self, **kwargs) -> None:
        if "nome" in kwargs:
            self.nome = kwargs["nome"]
        if "descricao" in kwargs:
            self.descricao = kwargs["descricao"]
        if "preco" in kwargs:
            self.preco = kwargs["preco"]
        # Poderia permitir update em produtos_usados também, se quiser:
        if "produtos_usados" in kwargs:
            self.produtos_usados = kwargs["produtos_usados"]

    def concluir(self) -> None:
        self.data_conclusao = datetime.datetime.now()

    def __repr__(self) -> str:
        if self.produtos_usados:
            produtos_str = ', '.join(f"{p.nome} x{qtd}" for p, qtd in self.produtos_usados)
            return f"Servico(nome={self.nome}, preco={self.preco}, produtos=[{produtos_str}])"
        else:
            return f"Servico(nome={self.nome}, preco={self.preco})"
