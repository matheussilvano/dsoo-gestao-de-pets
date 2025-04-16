import datetime
from controllers.agendamento_controller import AgendamentoController
from controllers.pet_controller import PetController
from controllers.servico_controller import ServicoController

def agendar_servico(agendamento_ctrl: AgendamentoController, pet_ctrl: PetController, servico_ctrl: ServicoController):
    print("\n===== Agendar Serviço =====")
    pet_nome = input("Nome do pet: ").strip()
    servico_nome = input("Nome do serviço: ").strip()
    data_str = input("Data/Hora do agendamento (YYYY-MM-DD HH:MM): ").strip()

    pet_encontrado = pet_ctrl.buscar_pet_por_nome(pet_nome)
    servico_encontrado = servico_ctrl.buscar_servico_por_nome(servico_nome)
    if pet_encontrado is None:
        print("Pet não encontrado.")
        return
    if servico_encontrado is None:
        print("Serviço não encontrado.")
        return
    try:
        ag_data = datetime.datetime.strptime(data_str, "%Y-%m-%d %H:%M")
        agendamento = agendamento_ctrl.criar_agendamento(pet_encontrado, servico_encontrado, ag_data)
        agendamento_ctrl.concluir_servico(agendamento)
        print("Agendamento realizado:", agendamento)
    except Exception as e:
        print("Erro ao criar agendamento:", e)
