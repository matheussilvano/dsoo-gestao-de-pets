from __future__ import annotations
import datetime
from typing import Optional
from models.pet import Pet
from models.servico import Servico
class Agendamento:
    def __init__(self, pet: Pet, servico: Servico, data_horario: datetime.datetime) -> None:
        if data_horario <= datetime.datetime.now():
            raise ValueError("O agendamento deve ser para uma data futura.")
        self.pet: Pet = pet
        self.servico: Servico = servico
        self.data_horario: datetime.datetime = data_horario
        self.cancelado: bool = False
        self.data_cancelamento: Optional[datetime.datetime] = None
    def cancelar(self) -> None:
        self.cancelado = True
        self.data_cancelamento = datetime.datetime.now()
    def __repr__(self) -> str:
        return f"Agendamento(pet={self.pet.nome}, servico={self.servico.nome}, data_horario={self.data_horario})"
