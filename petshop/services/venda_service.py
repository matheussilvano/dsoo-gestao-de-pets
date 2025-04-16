from typing import List, Tuple
from models.venda import Venda
from models.agendamento import Agendamento
from models.despesa import Despesa
from models.produto import Produto

class VendaService:
    def __init__(self) -> None:
        self._vendas: List[Venda] = []

    def criar_venda(self, agendamento: Agendamento, produtos_usados: List[Tuple[Produto, int]], despesas: List[Despesa], margem_lucro: float) -> Venda:
        for produto, quantidade in produtos_usados:
            produto.baixar_estoque(quantidade)
        venda = Venda(agendamento, produtos_usados, despesas, margem_lucro)
        self._vendas.append(venda)
        agendamento.pet.dono.total_gasto += venda.valor_total
        return venda

    def listar_vendas(self) -> List[Venda]:
        return self._vendas
