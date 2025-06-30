from views.menu_view import MenuView
from views.pygame_view import PygameView
from utils.persistence import save_data, load_data  # Importando as funções de persistência
import datetime
import random

def popular_dados_exemplo():
    from registry.registry import (
        dono_controller, pet_controller, produto_controller,
        servico_controller, despesa_controller, agendamento_controller,
        venda_controller
    )
    
    print("Populando o sistema com dados de exemplo...")

    # --- Produtos ---
    produtos = [
        produto_controller.criar_produto('Shampoo Antipulgas', 50, 22.50),
        produto_controller.criar_produto('Ração Premium Cães Adultos', 100, 89.90),
        produto_controller.criar_produto('Ração Premium Gatos Castrados', 80, 95.50),
        produto_controller.criar_produto('Biscoito Canino', 200, 12.00),
        produto_controller.criar_produto('Arranhador para Gatos', 30, 45.00),
        produto_controller.criar_produto('Vacina V10', 100, 60.00),
        produto_controller.criar_produto('Vermífugo', 150, 18.00),
        produto_controller.criar_produto('Perfume para Cães', 60, 25.00),
        produto_controller.criar_produto('Areia Higiênica', 120, 30.00),
        produto_controller.criar_produto('Brinquedo Bola de Borracha', 75, 8.50)
    ]
    
    # --- Serviços ---
    servicos = [
        servico_controller.criar_servico('Banho e Tosa Higiênica', 'Banho completo e tosa das partes íntimas', 80.0, [(produtos[0], 1), (produtos[7], 1)]),
        servico_controller.criar_servico('Consulta Veterinária', 'Consulta clínica geral com veterinário', 150.0, [(produtos[6], 1)]),
        servico_controller.criar_servico('Vacinação V10', 'Aplicação da vacina polivalente V10', 90.0, [(produtos[5], 1)]),
        servico_controller.criar_servico('Tosa Completa', 'Tosa de toda a pelagem do animal', 100.0, [(produtos[0], 1), (produtos[7], 1)]),
        servico_controller.criar_servico('Adestramento Básico (Aula)', 'Aula de adestramento básico em grupo', 120.0, [(produtos[3], 5)])
    ]

    # --- Donos e Pets ---
    donos_info = [
        ('Matheus Silvano', '48999887766', 'Rua das Flores, 123, Florianópolis'),
        ('Ana Julia', '11988776655', 'Avenida Central, 456, São Paulo'),
        ('Carlos Eduardo', '21977665544', 'Travessa dos Ventos, 789, Rio de Janeiro'),
        ('Beatriz Costa', '85966554433', 'Rua das Dunas, 101, Fortaleza'),
        ('Lucas Andrade', '51955443322', 'Avenida Ipiranga, 212, Porto Alegre')
    ]
    pets_info = [
        ('Fulaninho', 'Cachorro', 'Golden Retriever', 3), ('Belinha', 'Cachorro', 'Poodle', 5),
        ('Thor', 'Cachorro', 'Bulldog Francês', 2), ('Mia', 'Gato', 'Siamês', 4),
        ('Simba', 'Gato', 'Persa', 6), ('Luna', 'Cachorro', 'Labrador', 1),
        ('Loki', 'Gato', 'SRD', 2), ('Amora', 'Cachorro', 'Spitz Alemão', 4),
        ('Nino', 'Gato', 'Maine Coon', 3), ('Fred', 'Cachorro', 'Beagle', 7)
    ]
    
    pets_criados = []
    for i, (nome_dono, tel, end) in enumerate(donos_info):
        dono = dono_controller.criar_dono(nome_dono, tel, end)
        pet_info1 = pets_info[i*2]
        pet_info2 = pets_info[i*2 + 1]
        pets_criados.append(pet_controller.criar_pet(dono.nome, pet_info1[0], pet_info1[1], pet_info1[2], pet_info1[3]))
        pets_criados.append(pet_controller.criar_pet(dono.nome, pet_info2[0], pet_info2[1], pet_info2[2], pet_info2[3]))

    # --- Despesas ---
    despesa_controller.criar_despesa('Aluguel', 2500.0)
    despesa_controller.criar_despesa('Salários', 8000.0)
    despesa_controller.criar_despesa('Luz', 450.0)
    despesa_controller.criar_despesa('Água', 250.0)
    despesa_controller.criar_despesa('Marketing', 500.0)

    # --- Agendamentos e Vendas ---
    agendamentos_para_venda = []
    for _ in range(25):
        pet_aleatorio = random.choice(pets_criados)
        servico_aleatorio = random.choice(servicos)
        data_agendamento = datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 30), hours=random.randint(1, 23))
        
        try:
            ag = agendamento_controller.criar_agendamento(pet_aleatorio, servico_aleatorio, data_agendamento)
            agendamentos_para_venda.append(ag)
        except (ValueError, RuntimeError):
            pass
    
    for i in range(len(agendamentos_para_venda) // 2):
        agendamento_venda = agendamentos_para_venda[i]
        agendamento_venda.data_horario = datetime.datetime.now() - datetime.timedelta(days=random.randint(1,10))
        
        try:
            margem = random.uniform(15.0, 40.0)
            produtos_da_venda = agendamento_venda.servico.produtos_usados
            venda_controller.criar_venda(
                agendamento_venda,
                produtos_da_venda,
                [],
                margem
            )
        except (ValueError, RuntimeError):
            pass

    print("População de dados concluída!")


def main() -> None:
    dados_carregados = load_data()
    if not dados_carregados:
        popular_dados_exemplo()

    print("\nEscolha a interface:")
    print("1 - Terminal (texto)")
    print("2 - Gráfica (pygame)")
    escolha = input("Opção: ").strip()

    try:
        if escolha == "2":
            view = PygameView()
            view.executar()
        else:
            menu_view = MenuView()
            menu_view.exibir_menu()
    finally:
        save_data()

if __name__ == "__main__":
    main()