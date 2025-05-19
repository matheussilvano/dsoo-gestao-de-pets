from typing import List, Optional
from models.servico import Servico
from utils.utils import BaseService

class ServicoController(BaseService):
    def __init__(self) -> None:
        self._servicos: List[Servico] = []

    def criar_servico(self, nome: str, descricao: str, preco: float) -> Servico:
        if not nome.strip():
            raise ValueError("Nome vazio.")
        if not descricao.strip():
            raise ValueError("Descrição vazia.")
        if preco < 0:
            raise ValueError("Preço negativo.")
        self.validacao_unique(self._servicos, "nome", nome, "Serviço já existe.")
        service = Servico(nome, descricao, preco)
        self._servicos.append(service)
        return service

    def listar_servicos(self) -> List[Servico]:
        return self._servicos

    def buscar_servico_por_nome(self, nome: str) -> Optional[Servico]:
        return next((s for s in self._servicos if s.nome == nome), None)

    def atualizar_servico(self, nome: str, **kwargs) -> bool:
        service = self.buscar_servico_por_nome(nome)
        if not service:
            return False
        if "nome" in kwargs and kwargs["nome"] != nome:
            self.validacao_unique(self._servicos, "nome", kwargs["nome"], "Serviço já existe.")
        if "preco" in kwargs and kwargs["preco"] < 0:
            raise ValueError("Preço negativo.")
        service.update(**kwargs)
        return True

    def excluir_servico(self, nome: str) -> bool:
        service = self.buscar_servico_por_nome(nome)
        if service:
            self._servicos.remove(service)
            return True
        return False
