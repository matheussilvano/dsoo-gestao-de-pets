from __future__ import annotations
from typing import List
class Dono:
    def __init__(self, nome: str, telefone: str, endereco: str) -> None:
        self.nome: str = nome
        self.telefone: str = telefone
        self.endereco: str = endereco
        self.pets: List[Pet] = []
        self.historico_servicos: List[Servico] = []
        self.total_gasto: float = 0.0
    
    def update(self, **kwargs) -> None:
        if "nome" in kwargs:
            self.nome = kwargs["nome"]
        if "telefone" in kwargs:
            self.telefone = kwargs["telefone"]
        if "endereco" in kwargs:
            self.endereco = kwargs["endereco"]
    
    def adicionar_pet(self, pet: Pet) -> None:
        self.pets.append(pet)
    
    def registrar_servico(self, servico: Servico) -> None:
        self.historico_servicos.append(servico)
        self.total_gasto += servico.preco
    
    def __repr__(self) -> str:
        return f"Dono(nome={self.nome}, telefone={self.telefone})"
