class Servico:
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def atualizar_servico(self, nome=None, descricao=None, preco=None):
        if nome: self.nome = nome
        if descricao: self.descricao = descricao
        if preco is not None: self.preco = preco
