import datetime
from typing import List
from models.agendamento import Agendamento
from models.pet import Pet
from models.servico import Servico
from controllers.produto_controller import ProdutoController

class AgendamentoController:
    def __init__(self, produto_ctrl: ProdutoController) -> None:
        self._agendamentos: List[Agendamento] = []
        self.produto_ctrl = produto_ctrl

    def criar_agendamento(self, pet: Pet, servico: Servico, data_horario: datetime.datetime) -> Agendamento:
        # Verifica conflito de agendamento
        for ag in self._agendamentos:
            if ag.pet == pet and ag.data_horario == data_horario and not ag.cancelado:
                raise ValueError("Já existe agendamento para este pet neste horário.")

        # Verifica estoque e baixa produtos usados no serviço
        for produto, qtd_necessaria in servico.produtos_usados:
            produto_estoque = self.produto_ctrl.buscar_produto(produto.nome)
            if not produto_estoque:
                raise ValueError(f"Produto {produto.nome} não encontrado no estoque.")
            if produto_estoque.quantidade_estoque < qtd_necessaria:
                raise ValueError(f"Estoque insuficiente para o produto {produto.nome}.")
        
        # Baixa o estoque após validação
        for produto, qtd_necessaria in servico.produtos_usados:
            self.produto_ctrl.baixar_estoque(produto.nome, qtd_necessaria)

        agendamento = Agendamento(pet, servico, data_horario)
        self._agendamentos.append(agendamento)
        return agendamento

    def listar_agendamentos(self) -> List[Agendamento]:
        return self._agendamentos

    def cancelar_agendamento(self, agendamento: Agendamento) -> None:
        agendamento.cancelar()

    def listar_agendamentos_por_pet(self, pet: Pet) -> List[Agendamento]:
        return [ag for ag in self._agendamentos if ag.pet == pet]

    def concluir_servico(self, agendamento: Agendamento) -> None:
        if not agendamento.cancelado:
            agendamento.servico.concluir()
            agendamento.pet.registrar_servico(agendamento.servico)
            agendamento.pet.dono.registrar_servico(agendamento.servico)
