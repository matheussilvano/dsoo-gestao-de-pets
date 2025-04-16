from models.relatorio import RelatorioVendas
from models.venda import Venda
from typing import List, Dict
class RelatorioController:
    def gerar_relatorio_vendas(self, vendas: List[Venda]) -> Dict[str, float]:
        relatorio = RelatorioVendas(vendas)
        return relatorio.gerar_relatorio()
