class Dono:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.pets = []

    def adicionar_pet(self, pet):
        self.pets.append(pet)

    def remover_pet(self, pet):
        if pet in self.pets:
            self.pets.remove(pet)

    def calcular_valor_total(self):
        total = 0
        for pet in self.pets:
            for agendamento in pet.agendamentos:
                total += agendamento.servico.preco
        return total
