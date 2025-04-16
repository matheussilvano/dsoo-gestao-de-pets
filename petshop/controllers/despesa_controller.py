from typing import List, Optional
from models.despesa import Despesa
from services.despesa_service import DespesaService

class DespesaController:
    def __init__(self, despesa_service: DespesaService) -> None:
        self._despesa_service = despesa_service

    def criar_despesa(self, descricao: str, valor: float) -> Despesa:
        return self._despesa_service.criar_despesa(descricao, valor)

    def listar_despesas(self) -> List[Despesa]:
        return self._despesa_service.listar_despesas()

    def buscar_despesa(self, descricao: str) -> Optional[Despesa]:
        return self._despesa_service.buscar_despesa(descricao)

    def atualizar_despesa(self, descricao: str, **kwargs) -> bool:
        return self._despesa_service.atualizar_despesa(descricao, **kwargs)

    def excluir_despesa(self, descricao: str) -> bool:
        return self._despesa_service.excluir_despesa(descricao)
