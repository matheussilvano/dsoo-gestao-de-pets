import datetime
from controllers.agendamento_controller import AgendamentoController
from controllers.pet_controller import PetController
from controllers.servico_controller import ServicoController

class AgendamentoView:
    def __init__(self, agendamento_ctrl: AgendamentoController, pet_ctrl: PetController, servico_ctrl: ServicoController):
        self.agendamento_ctrl = agendamento_ctrl
        self.pet_ctrl = pet_ctrl
        self.servico_ctrl = servico_ctrl

    def agendar_servico(self):
        print("\n===== Agendar Serviço =====")

        # Lista pets numerada e escolhe
        pets = self.pet_ctrl.listar_pets()
        if not pets:
            print("Nenhum pet cadastrado.")
            return

        print("Selecione o pet:")
        for i, pet in enumerate(pets, start=1):
            dono = pet.dono.nome if hasattr(pet, 'dono') else "Sem dono"
            print(f"{i} - {pet.nome} (Dono: {dono})")

        try:
            pet_idx = int(input("Número do pet: ").strip())
            pet_encontrado = pets[pet_idx - 1]
        except (ValueError, IndexError):
            print("Seleção inválida de pet.")
            return

        # Lista serviços numerada e escolhe
        servicos = self.servico_ctrl.listar_servicos()
        if not servicos:
            print("Nenhum serviço cadastrado.")
            return

        print("Selecione o serviço:")
        for i, servico in enumerate(servicos, start=1):
            print(f"{i} - {servico.nome}")

        try:
            servico_idx = int(input("Número do serviço: ").strip())
            servico_encontrado = servicos[servico_idx - 1]
        except (ValueError, IndexError):
            print("Seleção inválida de serviço.")
            return

        data_str = input("Data/Hora do agendamento (YYYY-MM-DD HH:MM): ").strip()

        try:
            ag_data = datetime.datetime.strptime(data_str, "%Y-%m-%d %H:%M")
            agendamento = self.agendamento_ctrl.criar_agendamento(pet_encontrado, servico_encontrado, ag_data)
            self.agendamento_ctrl.concluir_servico(agendamento)
            print("Agendamento realizado:", agendamento)
        except Exception as e:
            print("Erro ao criar agendamento:", e)
