from typing import List, Optional
from models.despesa import Despesa
from utils.utils import BaseService

class DespesaService(BaseService):
    def __init__(self) -> None:
        self._despesas: List[Despesa] = []

    def criar_despesa(self, descricao: str, valor: float) -> Despesa:
        if not descricao.strip():
            raise ValueError("Descrição vazia.")
        if valor < 0:
            raise ValueError("Valor negativo.")
        self.validacao_unique(self._despesas, "descricao", descricao, "Despesa já existe.")
        despesa = Despesa(descricao, valor)
        self._despesas.append(despesa)
        return despesa

    def listar_despesas(self) -> List[Despesa]:
        return self._despesas

    def buscar_despesa(self, descricao: str) -> Optional[Despesa]:
        return next((d for d in self._despesas if d.descricao == descricao), None)

    def atualizar_despesa(self, descricao: str, **kwargs) -> bool:
        despesa = self.buscar_despesa(descricao)
        if not despesa:
            return False
        if "descricao" in kwargs and kwargs["descricao"] != descricao:
            self.validacao_unique(self._despesas, "descricao", kwargs["descricao"], "Despesa já existe.")
        if "valor" in kwargs and kwargs["valor"] < 0:
            raise ValueError("Valor negativo.")
        despesa.update(**kwargs)
        return True

    def excluir_despesa(self, descricao: str) -> bool:
        despesa = self.buscar_despesa(descricao)
        if despesa:
            self._despesas.remove(despesa)
            return True
        return False
