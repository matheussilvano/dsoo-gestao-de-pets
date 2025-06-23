from controllers.dono_controller import DonoController
from controllers.pet_controller import PetController
from controllers.produto_controller import ProdutoController
from controllers.servico_controller import ServicoController
from controllers.agendamento_controller import AgendamentoController
from controllers.venda_controller import VendaController
from controllers.relatorio_controller import RelatorioController
from controllers.despesa_controller import DespesaController

from views.dono_view import DonoView
from views.pet_view import PetView
from views.produto_view import ProdutoView
from views.servico_view import ServicoView
from views.agendamento_view import AgendamentoView
from views.venda_view import VendaView
from views.relatorio_view import RelatorioView

from utils.utils import cadastrar_despesas_iniciais


class MenuView:
    def __init__(self):
        # Inicializa os controllers
        dono_ctrl = DonoController()
        pet_ctrl = PetController(dono_ctrl)
        produto_ctrl = ProdutoController()
        servico_ctrl = ServicoController()
        agendamento_ctrl = AgendamentoController(produto_ctrl)  # Aqui passa produto_ctrl
        venda_ctrl = VendaController()
        relatorio_ctrl = RelatorioController()
        despesa_ctrl = DespesaController()

        # Cadastra despesas iniciais
        cadastrar_despesas_iniciais(despesa_ctrl)

        # Inicializa as views com os controllers apropriados
        self.menu_opcoes = {
            "1": ("Realizar Venda", VendaView().realizar_venda),
            "2": ("Agendar Serviço", AgendamentoView().agendar_servico),
            "3": ("Exibir Relatório de Vendas", RelatorioView().exibir_relatorio_vendas),
            "4": ("Gerenciar Donos", DonoView().mostrar_menu),
            "5": ("Gerenciar Pets", PetView().mostrar_menu),
            "6": ("Gerenciar Produtos", ProdutoView().mostrar_menu),
            "7": ("Gerenciar Serviços", ServicoView().gerenciar_servicos),
            "8": ("Sair", None),
        }

    def exibir_menu(self):
        print("========================================")
        print("         Bem-vindo ao Petshop")
        print("========================================")

        while True:
            print("\n----------------------------------------")
            print("Menu Principal:")
            for opc, (titulo, _) in self.menu_opcoes.items():
                print(f"{opc} - {titulo}")
            opc = input("Escolha uma opção: ").strip()

            if opc == "8":
                print("Encerrando o sistema.")
                break

            acao = self.menu_opcoes.get(opc)
            if acao:
                print(f"\n========== {acao[0].upper()} ==========")
                acao[1]()  # chama a função associada
            else:
                print("Opção inválida.")
