from typing import List, Optional
from models.servico import Servico

class ServicoService:
    def __init__(self) -> None:
        self._servicos: List[Servico] = []

    def criar_servico(self, nome: str, descricao: str, preco: float) -> Servico:
        service = Servico(nome, descricao, preco)
        self._servicos.append(service)
        return service

    def listar_servicos(self) -> List[Servico]:
        return self._servicos

    def buscar_servico_por_nome(self, nome: str) -> Optional[Servico]:
        for servico in self._servicos:
            if servico.nome == nome:
                return servico
        return None

    def atualizar_servico(self, nome: str, **kwargs) -> bool:
        service = self.buscar_servico_por_nome(nome)
        if service:
            service.update(**kwargs)
            return True
        return False

    def excluir_servico(self, nome: str) -> bool:
        service = self.buscar_servico_por_nome(nome)
        if service:
            self._servicos.remove(service)
            return True
        return False
