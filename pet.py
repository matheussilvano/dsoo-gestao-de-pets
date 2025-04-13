from dono import Dono

class Pet:
    def __init__(self, nome, especie, raca, idade, dono):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.dono = dono
        self.agendamentos = []

    def atualizar_dados(self, nome=None, especie=None, raca=None, idade=None):
        if nome: self.nome = nome
        if especie: self.especie = especie
        if raca: self.raca = raca
        if idade is not None: self.idade = idade

    def listar_servicos(self):
        return [agendamento.servico for agendamento in self.agendamentos]
