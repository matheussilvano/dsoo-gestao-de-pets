from typing import List, Optional
from models.produto import Produto
from services.produto_service import ProdutoService

class ProdutoController:
    def __init__(self, produto_service: ProdutoService) -> None:
        self._produto_service = produto_service

    def criar_produto(self, nome: str, quantidade_estoque: int, custo_unitario: float) -> Produto:
        return self._produto_service.criar_produto(nome, quantidade_estoque, custo_unitario)

    def listar_produtos(self) -> List[Produto]:
        return self._produto_service.listar_produtos()

    def buscar_produto(self, nome: str) -> Optional[Produto]:
        return self._produto_service.buscar_produto(nome)

    def atualizar_produto(self, nome: str, **kwargs) -> bool:
        return self._produto_service.atualizar_produto(nome, **kwargs)

    def excluir_produto(self, nome: str) -> bool:
        return self._produto_service.excluir_produto(nome)

    def baixar_estoque(self, nome: str, quantidade: int) -> None:
        return self._produto_service.baixar_estoque(nome, quantidade)
