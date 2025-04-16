import datetime
from controllers.venda_controller import VendaController
from controllers.pet_controller import PetController
from controllers.servico_controller import ServicoController
from controllers.produto_controller import ProdutoController
from controllers.despesa_controller import DespesaController
from controllers.agendamento_controller import AgendamentoController

def realizar_venda(
    venda_ctrl: VendaController,
    pet_ctrl: PetController,
    servico_ctrl: ServicoController,
    produto_ctrl: ProdutoController,
    despesa_ctrl: DespesaController,
    agendamento_ctrl: AgendamentoController
):
    print("\n===== Realizar Venda =====")
    pet_nome = input("Nome do pet: ").strip()
    servico_nome = input("Nome do serviço: ").strip()
    data_str = input("Data/Hora do agendamento (YYYY-MM-DD HH:MM): ").strip()

    pet_encontrado = pet_ctrl.buscar_pet_por_nome(pet_nome)
    servico_encontrado = servico_ctrl.buscar_servico_por_nome(servico_nome)
    if pet_encontrado is None:
        print("Pet não encontrado. Cadastre-o antes.")
        return
    if servico_encontrado is None:
        print("Serviço não encontrado. Cadastre-o antes.")
        return

    try:
        ag_data = datetime.datetime.strptime(data_str, "%Y-%m-%d %H:%M")
        agendamento = agendamento_ctrl.criar_agendamento(pet_encontrado, servico_encontrado, ag_data)
        agendamento_ctrl.concluir_servico(agendamento)
    except Exception as e:
        print("Erro ao criar agendamento:", e)
        return

    produtos_usados = [(p, 1) for p in produto_ctrl.listar_produtos()]
    try:
        margem = float(input("Margem de lucro para a venda (%): ").strip())
    except ValueError:
        print("Margem inválida.")
        return
    venda = venda_ctrl.criar_venda(agendamento, produtos_usados, despesa_ctrl.listar_despesas(), margem)
    print("Venda realizada:", venda)
