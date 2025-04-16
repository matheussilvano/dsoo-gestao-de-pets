from typing import List, Optional
from models.servico import Servico
from services.servico_service import ServicoService

class ServicoController:
    def __init__(self, servico_service: ServicoService) -> None:
        self._servico_service = servico_service

    def criar_servico(self, nome: str, descricao: str, preco: float) -> Servico:
        return self._servico_service.criar_servico(nome, descricao, preco)

    def listar_servicos(self) -> List[Servico]:
        return self._servico_service.listar_servicos()

    def buscar_servico_por_nome(self, nome: str) -> Optional[Servico]:
        return self._servico_service.buscar_servico_por_nome(nome)

    def atualizar_servico(self, nome: str, **kwargs) -> bool:
        return self._servico_service.atualizar_servico(nome, **kwargs)

    def excluir_servico(self, nome: str) -> bool:
        return self._servico_service.excluir_servico(nome)
