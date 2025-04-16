from typing import List, Optional
from models.pet import Pet
from services.pet_service import PetService

class PetController:
    def __init__(self, pet_service: PetService) -> None:
        self._pet_service = pet_service

    def criar_pet(self, nome_dono: str, nome: str, especie: str, raca: str, idade: int) -> Pet:
        return self._pet_service.criar_pet(nome_dono, nome, especie, raca, idade)

    def listar_pets(self) -> List[Pet]:
        return self._pet_service.listar_pets()

    def buscar_pet_por_nome(self, nome: str) -> Optional[Pet]:
        return self._pet_service.buscar_pet_por_nome(nome)

    def atualizar_pet(self, nome: str, **kwargs) -> bool:
        return self._pet_service.atualizar_pet(nome, **kwargs)

    def excluir_pet(self, nome: str) -> bool:
        return self._pet_service.excluir_pet(nome)
