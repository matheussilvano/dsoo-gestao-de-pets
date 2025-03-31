class Dono:
    def __init__(self, nome: str, telefone: str, endereco: str, lista_de_pets: list = None):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.lista_de_pets = lista_de_pets if lista_de_pets is not None else []

    def adicionar_pet(self, pet):
        self.lista_de_pets.append(pet)
