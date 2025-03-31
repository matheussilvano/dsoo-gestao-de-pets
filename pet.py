from dono import Dono

class Pet:
    def __init__(self, nome: str, especie: str, raca: str, idade: int, dono: Dono):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.dono = dono

    def exibir_informacoes(pet):
        return [
            f'Nome do Pet: {pet.nome}',
            f'Especie do pet: {pet.especie}',
            f'Raca do Pet: {pet.raca}',
            f'Idade do pet: {pet.idade}',
            f'Dono do pet: {pet.dono.nome}']
    
    def atualizar_dados(self, nome = None, especie = None, raca = None, idade = None):
        if nome:
            self.nome = nome
        if especie:
            self.especie = especie
        if raca:
            self.raca = raca
        if idade:
            self.idade = idade


dono1 = Dono('Carlos', '99999-9999', 'Rua A, 123')
pet1 = Pet('Paçoca', 'Cachorro', 'Vira-lata', '3', dono1)

dono1.adicionar_pet(pet1)

pet1.atualizar_dados(idade = 4)
