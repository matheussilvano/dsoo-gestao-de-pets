from typing import List, Optional
from models.pet import Pet
from models.dono import Dono
from utils.utils import BaseService
from controllers.dono_controller import DonoController

class PetController(BaseService):
    def __init__(self, dono_controller: DonoController) -> None:
        self._dono_ctrl = dono_controller

    def criar_pet(self, nome_dono: str, nome: str, especie: str, raca: str, idade: int) -> Pet:
        dono = self._dono_ctrl.buscar_dono_por_nome(nome_dono)
        if not dono:
            raise ValueError("Dono não encontrado.")
        # Verifica se pet já existe no dono
        if any(p.nome == nome for p in dono.pets):
            raise ValueError(f"Pet '{nome}' já cadastrado para este dono.")
        pet = Pet(nome, especie, raca, idade, dono)
        return pet

    def listar_pets(self) -> List[Pet]:
        pets: List[Pet] = []
        for dono in self._dono_ctrl.listar_donos():
            pets.extend(dono.pets)
        return pets

    def buscar_pet_por_nome(self, nome: str) -> Optional[Pet]:
        for dono in self._dono_ctrl.listar_donos():
            for pet in dono.pets:
                if pet.nome == nome:
                    return pet
        return None

    def atualizar_pet(self, nome_pet_atual: str, **kwargs) -> bool:
        pet = self.buscar_pet_por_nome(nome_pet_atual)
        if not pet:
            return False
        if "nome" in kwargs and kwargs["nome"] != nome_pet_atual:
            # verifica duplicidade
            for dono in self._dono_ctrl.listar_donos():
                if any(p.nome == kwargs["nome"] for p in dono.pets):
                    raise ValueError("Pet já cadastrado.")
        if "idade" in kwargs and kwargs["idade"] < 0:
            raise ValueError("Idade negativa.")
        pet.update(**kwargs)
        return True

    def excluir_pet(self, nome: str) -> bool:
        pet = self.buscar_pet_por_nome(nome)
        if pet:
            pet.dono.pets.remove(pet)
            return True
        return False
