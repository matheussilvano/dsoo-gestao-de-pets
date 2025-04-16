from __future__ import annotations
from typing import List, Tuple
from models.agendamento import Agendamento
from models.despesa import Despesa
from models.produto import Produto
class Venda:
    def __init__(self, agendamento: Agendamento, produtos_usados: List[Tuple[Produto, int]], despesas: List[Despesa], margem_lucro: float) -> None:
        self.agendamento: Agendamento = agendamento
        self.produtos_usados: List[Tuple[Produto, int]] = produtos_usados
        self.despesas: List[Despesa] = despesas
        self.margem_lucro: float = margem_lucro
        self.valor_total: float = 0.0
        self.calcular_valor_total()
    
    def calcular_valor_total(self) -> None:
        preco_servico: float = self.agendamento.servico.preco
        custo_produtos: float = sum(produto.custo_unitario * quantidade for produto, quantidade in self.produtos_usadas)
        custo_despesas: float = sum(despesa.valor for despesa in self.despesas)
        custo_total: float = preco_servico + custo_produtos + custo_despesas
        self.valor_total = custo_total * (1 + self.margem_lucro / 100.0)
    
    def __repr__(self) -> str:
        return f"Venda(servico={self.agendamento.servico.nome}, valor_total={self.valor_total:.2f})"
