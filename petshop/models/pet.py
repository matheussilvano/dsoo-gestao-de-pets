from __future__ import annotations
from typing import List

class Pet:
    def __init__(self, nome: str, especie: str, raca: str, idade: int, dono: Dono) -> None:
        if idade <= 0:
            raise ValueError("A idade do pet deve ser um inteiro positivo.")
        self.nome: str = nome
        self.especie: str = especie
        self.raca: str = raca
        self.idade: int = idade
        self.dono: "Dono" = dono
        self.historico_servicos: List["Servico"] = []
        dono.adicionar_pet(self)
   
    def update(self, **kwargs) -> None:
        if "nome" in kwargs:
            self.nome = kwargs["nome"]
        if "especie" in kwargs:
            self.especie = kwargs["especie"]
        if "raca" in kwargs:
            self.raca = kwargs["raca"]
        if "idade" in kwargs:
            nova_idade: int = kwargs["idade"]
            if nova_idade <= 0:
                raise ValueError("A idade deve ser um inteiro positivo.")
            self.idade = nova_idade
    
    def registrar_servico(self, servico: "Servico") -> None:
        self.historico_servicos.append(servico)
    
    def __repr__(self) -> str:
        return f"Pet(nome={self.nome}, dono={self.dono.nome})"
