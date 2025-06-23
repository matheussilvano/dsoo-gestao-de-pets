from registry.registry import agendamento_controller, pet_controller, servico_controller, produto_controller
import datetime

class AgendamentoView:
    def __init__(self):
        pass

    def agendar_servico(self):
        pets = pet_controller.listar_pets()
        if not pets:
            print("Nenhum pet cadastrado.")
            return

        print("Pets disponíveis:")
        for i, pet in enumerate(pets, 1):
            print(f"{i} - {pet.nome}")

        escolha_pet = input("Escolha o pet pelo número: ").strip()
        try:
            pet_idx = int(escolha_pet) - 1
            pet = pets[pet_idx]
        except (ValueError, IndexError):
            print("Pet inválido.")
            return

        servicos = servico_controller.listar_servicos()
        if not servicos:
            print("Nenhum serviço cadastrado.")
            return

        print("Serviços disponíveis:")
        for i, servico in enumerate(servicos, 1):
            print(f"{i} - {servico.nome}")

        escolha_servico = input("Escolha o serviço pelo número: ").strip()
        try:
            servico_idx = int(escolha_servico) - 1
            servico = servicos[servico_idx]
        except (ValueError, IndexError):
            print("Serviço inválido.")
            return

        data_str = input("Data e hora (YYYY-MM-DD HH:MM): ").strip()
        try:
            data_horario = datetime.datetime.strptime(data_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Data/hora inválida.")
            return

        try:
            agendamento = agendamento_controller.criar_agendamento(pet, servico, data_horario)
            print(f"Agendamento criado: {agendamento}")
        except Exception as e:
            print(f"Erro ao agendar: {e}")

    def listar_agendamentos(self):
        agendamentos = agendamento_controller.listar_agendamentos()
        if not agendamentos:
            print("Nenhum agendamento.")
            return
        for ag in agendamentos:
            print(ag)
