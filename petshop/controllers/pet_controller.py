from models.pet import Pet
from typing import List, Optional
from controllers.dono_controller import DonoController
class PetController:
    def __init__(self, dono_controller: DonoController) -> None:
        self._pets: List[Pet] = []
        self._dono_controller = dono_controller
    def criar_pet(self, nome_dono: str, nome: str, especie: str, raca: str, idade: int) -> Pet:
        dono = self._dono_controller.buscar_dono_por_nome(nome_dono)
        if not dono:
            raise ValueError("Dono não encontrado.")
        pet = Pet(nome, especie, raca, idade, dono)
        self._pets.append(pet)
        return pet
    def listar_pets(self) -> List[Pet]:
        return self._pets
    def buscar_pet_por_nome(self, nome: str) -> Optional[Pet]:
        for pet in self._pets:
            if pet.nome == nome:
                return pet
        return None
    def atualizar_pet(self, nome: str, **kwargs) -> bool:
        pet = self.buscar_pet_por_nome(nome)
        if pet:
            pet.update(**kwargs)
            return True
        return False
    def excluir_pet(self, nome: str) -> bool:
        pet = self.buscar_pet_por_nome(nome)
        if pet:
            if pet in pet.dono.pets:
                pet.dono.pets.remove(pet)
            self._pets.remove(pet)
            return True
        return False
