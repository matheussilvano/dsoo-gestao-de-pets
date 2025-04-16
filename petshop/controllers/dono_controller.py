from typing import List, Optional
from models.dono import Dono
from services.dono_service import DonoService

class DonoController:
    def __init__(self, dono_service: DonoService) -> None:
        self._dono_service = dono_service

    def criar_dono(self, nome: str, telefone: str, endereco: str) -> Dono:
        return self._dono_service.criar_dono(nome, telefone, endereco)

    def listar_donos(self) -> List[Dono]:
        return self._dono_service.listar_donos()

    def buscar_dono_por_nome(self, nome: str) -> Optional[Dono]:
        return self._dono_service.buscar_dono_por_nome(nome)

    def atualizar_dono(self, nome_autal: str, **kwargs) -> bool:
        return self._dono_service.atualizar_dono(nome_autal, **kwargs)

    def excluir_dono(self, nome: str) -> bool:
        return self._dono_service.excluir_dono(nome)
