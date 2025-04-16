from models.agendamento import Agendamento
from models.pet import Pet
from models.servico import Servico
from typing import List
import datetime
class AgendamentoController:
    def __init__(self) -> None:
        self._agendamentos: List[Agendamento] = []
    
    def criar_agendamento(self, pet: Pet, servico: Servico, data_horario: datetime.datetime) -> Agendamento:
        for ag in self._agendamentos:
            if ag.pet == pet and ag.data_horario == data_horario and not ag.cancelado:
                raise ValueError("Já existe agendamento para este pet neste horário.")
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
