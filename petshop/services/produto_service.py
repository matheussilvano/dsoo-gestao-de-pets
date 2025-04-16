from typing import List, Optional
from models.produto import Produto

class ProdutoService:
    def __init__(self) -> None:
        self._produtos: List[Produto] = []

    def criar_produto(self, nome: str, quantidade: int, custo: float) -> Produto:
        p = Produto(nome, quantidade, custo)
        self._produtos.append(p)
        return p

    def listar_produtos(self) -> List[Produto]:
        return self._produtos

    def buscar_produto(self, nome: str) -> Optional[Produto]:
        for produto in self._produtos:
            if produto.nome == nome:
                return produto
        return None

    def atualizar_produto(self, nome: str, **kwargs) -> bool:
        produto = self.buscar_produto(nome)
        if produto:
            produto.update(**kwargs)
            return True
        return False

    def excluir_produto(self, nome: str) -> bool:
        produto = self.buscar_produto(nome)
        if produto:
            self._produtos.remove(produto)
            return True
        return False

    def baixar_estoque(self, nome: str, quantidade: int) -> None:
        produto = self.buscar_produto(nome)
        if not produto:
            raise ValueError("Produto não encontrado.")
        produto.baixar_estoque(quantidade)
