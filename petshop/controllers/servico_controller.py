from models.servico import Servico
from typing import List, Optional
class ServicoController:
    def __init__(self) -> None:
        self._servicos: List[Servico] = []
    def criar_servico(self, nome: str, descricao: str, preco: float) -> Servico:
        servico = Servico(nome, descricao, preco)
        self._servicos.append(servico)
        return servico
    def listar_servicos(self) -> List[Servico]:
        return self._servicos
    def buscar_servico_por_nome(self, nome: str) -> Optional[Servico]:
        for servico in self._servicos:
            if servico.nome == nome:
                return servico
        return None
    def atualizar_servico(self, nome: str, **kwargs) -> bool:
        servico = self.buscar_servico_por_nome(nome)
        if servico:
            servico.update(**kwargs)
            return True
        return False
    def excluir_servico(self, nome: str) -> bool:
        servico = self.buscar_servico_por_nome(nome)
        if servico:
            self._servicos.remove(servico)
            return True
        return False
