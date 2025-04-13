from datetime import date, time
from pet import Pet
from servico import Servico

class Agendamento:
    def __init__(self, data: date, hora: time, pet: Pet, servico: Servico):
        self.data = data
        self.hora = hora
        self.pet = pet
        self.servico = servico
        self.status = "Agendado"
        pet.agendamentos.append(self)

    def agendar_servico(self):
        self.status = "Agendado"

    def cancelar_servico(self):
        self.status = "Cancelado"

    def verificar_conflito(self, agendamentos):
        for ag in agendamentos:
            if (
                ag.pet == self.pet and
                ag.data == self.data and
                ag.hora == self.hora and
                ag != self
            ):
                return True
        return False

