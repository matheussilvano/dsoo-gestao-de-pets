from typing import List, Dict
from models.venda import Venda
from services.relatorio_service import RelatorioService

class RelatorioController:
    def __init__(self, relatorio_service: RelatorioService) -> None:
        self._relatorio_service = relatorio_service
    
    def gerar_relatorio_vendas(self, vendas: List[Venda]) -> Dict[str, float]:
        return self._relatorio_service.gerar_relatorio_vendas(vendas)
