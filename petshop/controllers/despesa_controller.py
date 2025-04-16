from models.despesa import Despesa
from typing import List, Optional
class DespesaController:
    def __init__(self) -> None:
        self._despesas: List[Despesa] = []
    def criar_despesa(self, descricao: str, valor: float) -> Despesa:
        despesa = Despesa(descricao, valor)
        self._despesas.append(despesa)
        return despesa
    def listar_despesas(self) -> List[Despesa]:
        return self._despesas
    def buscar_despesa(self, descricao: str) -> Optional[Despesa]:
        for despesa in self._despesas:
            if despesa.descricao == descricao:
                return despesa
        return None
    def atualizar_despesa(self, descricao: str, **kwargs) -> bool:
        despesa = self.buscar_despesa(descricao)
        if despesa:
            despesa.update(**kwargs)
            return True
        return False
    def excluir_despesa(self, descricao: str) -> bool:
        despesa = self.buscar_despesa(descricao)
        if despesa:
            self._despesas.remove(despesa)
            return True
        return False
