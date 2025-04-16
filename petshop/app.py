from registry.registry import (
    dono_controller,
    pet_controller,
    produto_controller,
    servico_controller,
    agendamento_controller,
    despesa_controller,
    venda_controller,
    relatorio_controller,
)

from views.dono_view import gerenciar_dono
from views.pet_view import gerenciar_pet
from views.produto_view import gerenciar_produto
from views.servico_view import gerenciar_servico
from views.agendamento_view import agendar_servico
from views.venda_view import realizar_venda
from views.relatorio_view import exibir_relatorio_vendas

from utils.utils import cadastrar_despesas_iniciais


def menu() -> None:
    produto_controller.criar_produto("Xampu", 10, 2.0)
    produto_controller.criar_produto("Condicionador", 5, 3.0)

    print("========================================")
    print("          Bem‑vindo ao Petshop          ")
    print("========================================\n")
    print("Antes de iniciar, cadastre as despesas.")
    cadastrar_despesas_iniciais(despesa_controller)

    while True:
        print("\n----------------------------------------")
        print("Menu:")
        print("1 - Realizar Venda")
        print("2 - Agendar Serviço")
        print("3 - Exibir Relatório de Vendas")
        print("4 - Gerenciar Donos")
        print("5 - Gerenciar Pets")
        print("6 - Gerenciar Produtos")
        print("7 - Gerenciar Serviços")
        print("8 - Sair")
        print("----------------------------------------")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n========== REALIZAR VENDA ==========")
            realizar_venda(
                venda_controller,
                pet_controller,
                servico_controller,
                produto_controller,
                despesa_controller,
                agendamento_controller,
            )

        elif opcao == "2":
            print("\n========== AGENDAR SERVIÇO ==========")
            agendar_servico(
                agendamento_controller,
                pet_controller,
                servico_controller,
            )

        elif opcao == "3":
            print("\n========== RELATÓRIO DE VENDAS ==========")
            exibir_relatorio_vendas(
                relatorio_controller,
                venda_controller,
            )

        elif opcao == "4":
            print("\n========== GERENCIAR DONOS ==========")
            gerenciar_dono(dono_controller)

        elif opcao == "5":
            print("\n========== GERENCIAR PETS ==========")
            gerenciar_pet(pet_controller)

        elif opcao == "6":
            print("\n========== GERENCIAR PRODUTOS ==========")
            gerenciar_produto(produto_controller)

        elif opcao == "7":
            print("\n========== GERENCIAR SERVIÇOS ==========")
            gerenciar_servico(servico_controller)

        elif opcao == "8":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
