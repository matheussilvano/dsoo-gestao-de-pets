from typing import List, Tuple
from models.venda import Venda
from models.agendamento import Agendamento
from models.despesa import Despesa
from models.produto import Produto
from services.venda_service import VendaService

class VendaController:
    def __init__(self, venda_service: VendaService) -> None:
        self._venda_service = venda_service

    def criar_venda(self, 
                    agendamento: Agendamento, 
                    produtos_usados: List[Tuple[Produto, int]], 
                    despesas: List[Despesa], 
                    margem_lucro: float) -> Venda:
        return self._venda_service.criar_venda(agendamento, produtos_usados, despesas, margem_lucro)

    def listar_vendas(self) -> List[Venda]:
        return self._venda_service.listar_vendas()
