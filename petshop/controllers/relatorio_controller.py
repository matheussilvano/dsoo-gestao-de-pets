from typing import List, Dict
from models.venda import Venda
from models.relatorio import RelatorioVendas

class RelatorioController:
    def gerar_relatorio_vendas(self, vendas: List[Venda]) -> Dict[str, float]:
        r = RelatorioVendas(vendas)
        return r.gerar_relatorio()
