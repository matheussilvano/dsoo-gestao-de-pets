from typing import List, Optional
from models.produto import Produto
from utils.utils import BaseService

class ProdutoController(BaseService):
    def __init__(self) -> None:
        self._produtos: List[Produto] = []

    def criar_produto(self, nome: str, quantidade: int, custo: float) -> Produto:
        if not nome.strip():
            raise ValueError("Nome vazio.")
        if quantidade < 0:
            raise ValueError("Quantidade negativa.")
        if custo < 0:
            raise ValueError("Custo negativo.")
        self.validacao_unique(self._produtos, "nome", nome, "Produto já existe.")
        p = Produto(nome, quantidade, custo)
        self._produtos.append(p)
        return p

    def listar_produtos(self) -> List[Produto]:
        return self._produtos

    def buscar_produto(self, nome: str) -> Optional[Produto]:
        return next((p for p in self._produtos if p.nome == nome), None)

    def atualizar_produto(self, nome: str, **kwargs) -> bool:
        produto = self.buscar_produto(nome)
        if not produto:
            return False
        if "nome" in kwargs and kwargs["nome"] != nome:
            self.validacao_unique(self._produtos, "nome", kwargs["nome"], "Produto já existe.")
        
        if "quantidade_estoque" in kwargs and kwargs["quantidade_estoque"] < 0:
            raise ValueError("Quantidade negativa.")
        if "custo_unitario" in kwargs and kwargs["custo_unitario"] < 0:
            raise ValueError("Custo negativo.")
            
        produto.update(**kwargs)
        return True

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
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva.")
        produto.baixar_estoque(quantidade)
