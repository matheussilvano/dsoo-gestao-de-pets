import datetime
from typing import List
from models.agendamento import Agendamento
from models.pet import Pet
from models.servico import Servico
from services.agendamento_service import AgendamentoService

class AgendamentoController:
    def __init__(self, agendamento_service: AgendamentoService) -> None:
        self._agendamento_service = agendamento_service
    
    def criar_agendamento(self, pet: Pet, servico: Servico, data_horario: datetime.datetime) -> Agendamento:
        return self._agendamento_service.criar_agendamento(pet, servico, data_horario)

    def listar_agendamentos(self) -> List[Agendamento]:
        return self._agendamento_service.listar_agendamentos()

    def cancelar_agendamento(self, agendamento: Agendamento) -> None:
        self._agendamento_service.cancelar_agendamento(agendamento)

    def listar_agendamentos_por_pet(self, pet: Pet) -> List[Agendamento]:
        return self._agendamento_service.listar_agendamentos_por_pet(pet)

    def concluir_servico(self, agendamento: Agendamento) -> None:
        self._agendamento_service.concluir_servico(agendamento)
