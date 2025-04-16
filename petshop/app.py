#!/usr/bin/env python3
import datetime
from controllers.dono_controller import DonoController
from controllers.pet_controller import PetController
from controllers.servico_controller import ServicoController
from controllers.agendamento_controller import AgendamentoController
from controllers.despesa_controller import DespesaController
from controllers.produto_controller import ProdutoController
from controllers.venda_controller import VendaController
from controllers.relatorio_controller import RelatorioController
def cadastrar_despesas_iniciais(despesa_ctrl: DespesaController) -> None:
    print("Cadastre pelo menos uma despesa.")
    while True:
        descricao = input("Descrição da despesa (ou 'fim' para encerrar): ")
        if descricao.lower() == 'fim':
            break
        try:
            valor = float(input("Valor da despesa: "))
            despesa_ctrl.criar_despesa(descricao, valor)
            print("Despesa cadastrada.")
        except ValueError:
            print("Valor inválido. Tente novamente.")
    if not despesa_ctrl.listar_despesas():
        print("Você deve cadastrar pelo menos uma despesa!")
        cadastrar_despesas_iniciais(despesa_ctrl)
def menu() -> None:
    dono_ctrl = DonoController()
    pet_ctrl = PetController(dono_ctrl)
    servico_ctrl = ServicoController()
    agendamento_ctrl = AgendamentoController()
    despesa_ctrl = DespesaController()
    produto_ctrl = ProdutoController()
    venda_ctrl = VendaController()
    relatorio_ctrl = RelatorioController()
    produto_ctrl.criar_produto("Xampu", 10, 2.0)
    produto_ctrl.criar_produto("Condicionador", 5, 3.0)
    print("Bem-vindo ao Petshop!")
    print("Antes de iniciar, cadastre as despesas.")
    cadastrar_despesas_iniciais(despesa_ctrl)
    while True:
        print("\nMenu:")
        print("1 - Realizar Venda")
        print("2 - Agendar Serviço")
        print("3 - Exibir Relatório de Vendas")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            print("\nRealizar Venda")
            pet_nome = input("Nome do pet: ")
            servico_nome = input("Nome do serviço: ")
            data_str = input("Data/Hora do agendamento (YYYY-MM-DD HH:MM): ")
            pet = pet_ctrl.buscar_pet_por_nome(pet_nome)
            servico = servico_ctrl.buscar_servico_por_nome(servico_nome)
            if pet is None:
                print("Pet não encontrado. Cadastre-o antes.")
                continue
            if servico is None:
                print("Serviço não encontrado. Cadastre-o antes.")
                continue
            try:
                ag_data = datetime.datetime.strptime(data_str, "%Y-%m-%d %H:%M")
                agendamento = agendamento_ctrl.criar_agendamento(pet, servico, ag_data)
                agendamento_ctrl.concluir_servico(agendamento)
            except Exception as e:
                print("Erro ao criar agendamento:", e)
                continue
            produtos_usados = [(p, 1) for p in produto_ctrl.listar_produtos()]
            try:
                margem = float(input("Margem de lucro para a venda (%): "))
            except ValueError:
                print("Margem inválida.")
                continue
            venda = venda_ctrl.criar_venda(agendamento, produtos_usados, despesa_ctrl.listar_despesas(), margem)
            print("Venda realizada:", venda)
        elif opcao == "2":
            print("\nAgendar Serviço")
            pet_nome = input("Nome do pet: ")
            servico_nome = input("Nome do serviço: ")
            data_str = input("Data/Hora do agendamento (YYYY-MM-DD HH:MM): ")
            pet = pet_ctrl.buscar_pet_por_nome(pet_nome)
            servico = servico_ctrl.buscar_servico_por_nome(servico_nome)
            if pet is None:
                print("Pet não encontrado.")
                continue
            if servico is None:
                print("Serviço não encontrado.")
                continue
            try:
                ag_data = datetime.datetime.strptime(data_str, "%Y-%m-%d %H:%M")
                agendamento = agendamento_ctrl.criar_agendamento(pet, servico, ag_data)
                agendamento_ctrl.concluir_servico(agendamento)
                print("Agendamento realizado:", agendamento)
            except Exception as e:
                print("Erro:", e)
        elif opcao == "3":
            print("\nRelatório de Vendas")
            relatorio = relatorio_ctrl.gerar_relatorio_vendas(venda_ctrl.listar_vendas())
            for chave, valor in relatorio.items():
                print(f"{chave}: {valor}")
        elif opcao == "4":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    menu()
