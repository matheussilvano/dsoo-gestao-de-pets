from __future__ import annotations
from typing import List, Optional
from models.venda import Venda
class RelatorioVendas:
    def __init__(self, vendas: List[Venda]) -> None:
        self.vendas: List[Venda] = vendas
    def total_vendas(self) -> float:
        return sum(venda.valor_total for venda in self.vendas)
    def quantidade_vendas(self) -> int:
        return len(self.vendas)
    def media_vendas(self) -> float:
        qtd: int = self.quantidade_vendas()
        return self.total_vendas() / qtd if qtd > 0 else 0.0
    def maior_venda(self) -> Optional[Venda]:
        return max(self.vendas, key=lambda v: v.valor_total) if self.vendas else None
    def menor_venda(self) -> Optional[Venda]:
        return min(self.vendas, key=lambda v: v.valor_total) if self.vendas else None
    def gerar_relatorio(self) -> dict:
        return {"total_vendas": self.total_vendas(),"quantidade_vendas": self.quantidade_vendas(),"media_vendas": self.media_vendas(),"maior_venda": self.maior_venda().valor_total if self.maior_venda() else 0,"menor_venda": self.menor_venda().valor_total if self.menor_venda() else 0}
