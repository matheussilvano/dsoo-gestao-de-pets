from views.menu_view import MenuView
from views.pygame_view import PygameView
from registry.registry import dono_controller, pet_controller, produto_controller, servico_controller, despesa_controller

def popular_dados_exemplo():
    # Donos e Pets
    dono1 = dono_controller.criar_dono('Matheus Silvano Pereira', '11999999999', 'Rua das Flores, 123')
    dono2 = dono_controller.criar_dono('Ana Souza', '11888888888', 'Av. Central, 456')
    pet1 = pet_controller.criar_pet(dono1.nome, 'Fulaninho', 'Cachorro', 'SRD', 3)
    pet2 = pet_controller.criar_pet(dono2.nome, 'Bolota', 'Gato', 'Persa', 2)
    # Produtos
    prod1 = produto_controller.criar_produto('Shampoo', 10, 15.0)
    prod2 = produto_controller.criar_produto('Ração Premium', 20, 50.0)
    # Serviços
    servico_controller.criar_servico('Banho e tosa', 'Banho completo e tosa higiênica', 80.0, [(prod1, 1)])
    servico_controller.criar_servico('Consulta veterinária', 'Consulta clínica geral', 120.0, [(prod2, 1)])
    # Despesas
    despesa_controller.criar_despesa('Luz', 200.0)
    despesa_controller.criar_despesa('Água', 100.0)

def main() -> None:
    popular_dados_exemplo()
    print("Escolha a interface:")
    print("1 - Terminal (texto)")
    print("2 - Gráfica (pygame)")
    escolha = input("Opção: ").strip()
    if escolha == "2":
        PygameView().executar()
    else:
        menu_view = MenuView()
        menu_view.exibir_menu()

if __name__ == "__main__":
    main()
