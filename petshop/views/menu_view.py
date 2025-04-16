from services.dono_service import DonoService
from services.pet_service import PetService
from services.produto_service import ProdutoService
from services.servico_service import ServicoService
from services.agendamento_service import AgendamentoService
from services.venda_service import VendaService
from services.relatorio_service import RelatorioService
from services.despesa_service import DespesaService

from controllers.dono_controller import DonoController
from controllers.pet_controller import PetController
from controllers.produto_controller import ProdutoController
from controllers.servico_controller import ServicoController
from controllers.agendamento_controller import AgendamentoController
from controllers.venda_controller import VendaController
from controllers.relatorio_controller import RelatorioController
from controllers.despesa_controller import DespesaController

from views.dono_view import gerenciar_dono
from views.pet_view import gerenciar_pet
from views.produto_view import gerenciar_produto
from views.servico_view import gerenciar_servico
from views.agendamento_view import agendar_servico
from views.venda_view import realizar_venda
from views.relatorio_view import exibir_relatorio_vendas

from utils.utils import cadastrar_despesas_iniciais

def start_app():
    dono_service = DonoService()
    pet_service = PetService(dono_service)
    produto_service = ProdutoService()
    servico_service = ServicoService()
    agendamento_service = AgendamentoService()
    venda_service = VendaService()
    relatorio_service = RelatorioService()
    despesa_service = DespesaService()

    dono_ctrl = DonoController(dono_service)
    pet_ctrl = PetController(pet_service)
    produto_ctrl = ProdutoController(produto_service)
    servico_ctrl = ServicoController(servico_service)
    agendamento_ctrl = AgendamentoController(agendamento_service)
    despesa_ctrl = DespesaController(despesa_service)
    venda_ctrl = VendaController(venda_service)
    relatorio_ctrl = RelatorioController(relatorio_service)

    print("========================================")
    print("         Bem-vindo ao Petshop")
    print("========================================")

    cadastrar_despesas_iniciais(despesa_ctrl)

    while True:
        print("\n----------------------------------------")
        print("Menu Principal:")
        print("1 - Realizar Venda")
        print("2 - Agendar Serviço")
        print("3 - Exibir Relatório de Vendas")
        print("4 - Gerenciar Donos")
        print("5 - Gerenciar Pets")
        print("6 - Gerenciar Produtos")
        print("7 - Gerenciar Serviços")
        print("8 - Sair")
        opc = input("Escolha uma opção: ").strip()

        if opc == "1":
            realizar_venda(venda_ctrl, pet_ctrl, servico_ctrl, produto_ctrl, despesa_ctrl, agendamento_ctrl)
        elif opc == "2":
            agendar_servico(agendamento_ctrl, pet_ctrl, servico_ctrl)
        elif opc == "3":
            exibir_relatorio_vendas(relatorio_ctrl, venda_ctrl)
        elif opc == "4":
            gerenciar_dono(dono_ctrl)
        elif opc == "5":
            gerenciar_pet(pet_ctrl)
        elif opc == "6":
            gerenciar_produto(produto_ctrl)
        elif opc == "7":
            gerenciar_servico(servico_ctrl)
        elif opc == "8":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")
