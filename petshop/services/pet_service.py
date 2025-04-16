from typing import List, Optional
from models.pet import Pet
from utils.utils import BaseService
from services.dono_service import DonoService

class PetService(BaseService):
    def __init__(self, dono_service: DonoService) -> None:
        self._pets: List[Pet] = []
        self._dono_service = dono_service

    def criar_pet(self, nome_dono: str, nome: str, especie: str, raca: str, idade: int) -> Pet:
        dono = self._dono_service.buscar_dono_por_nome(nome_dono)
        if not dono:
            raise ValueError("Dono não encontrado.")
        if idade < 0:
            raise ValueError("Idade negativa.")
        self.validacao_unique(self._pets, "nome", nome, "Pet já cadastrado.")
        pet = Pet(nome, especie, raca, idade, dono)
        self._pets.append(pet)
        return pet

    def listar_pets(self) -> List[Pet]:
        return self._pets

    def buscar_pet_por_nome(self, nome: str) -> Optional[Pet]:
        return next((p for p in self._pets if p.nome == nome), None)

    def atualizar_pet(self, nome_pet_atual: str, **kwargs) -> bool:
        pet = self.buscar_pet_por_nome(nome_pet_atual)
        if not pet:
            return False
        if "nome" in kwargs and kwargs["nome"] != nome_pet_atual:
            self.validacao_unique(self._pets, "nome", kwargs["nome"], "Pet já cadastrado.")
        if "idade" in kwargs and kwargs["idade"] < 0:
            raise ValueError("Idade negativa.")
        pet.update(**kwargs)
        return True

    def excluir_pet(self, nome: str) -> bool:
        pet = self.buscar_pet_por_nome(nome)
        if pet:
            if pet in pet.dono.pets:
                pet.dono.pets.remove(pet)
            self._pets.remove(pet)
            return True
        return False
