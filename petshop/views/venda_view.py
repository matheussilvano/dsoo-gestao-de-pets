from registry.registry import venda_controller, pet_controller, servico_controller, produto_controller, despesa_controller, agendamento_controller
import datetime

class VendaView:
    def __init__(self):
        pass

    def realizar_venda(self):
        print("\n===== Realizar Venda =====")

        donos = sorted({pet.dono for pet in pet_controller.listar_pets()}, key=lambda d: d.nome)
        if not donos:
            print("Nenhum dono cadastrado. Cadastre antes.")
            return
        print("Donos:")
        for i, dono in enumerate(donos, 1):
            print(f"{i} - {dono.nome}")
        try:
            dono_idx = int(input("Escolha o número do dono: ").strip())
            dono = donos[dono_idx - 1]
        except (ValueError, IndexError):
            print("Opção inválida.")
            return

        pets_do_dono = [pet for pet in pet_controller.listar_pets() if pet.dono == dono]
        if not pets_do_dono:
            print(f"O dono {dono.nome} não tem pets cadastrados.")
            return
        print(f"Pets do dono {dono.nome}:")
        for i, pet in enumerate(pets_do_dono, 1):
            print(f"{i} - {pet.nome}")
        try:
            pet_idx = int(input("Escolha o número do pet: ").strip())
            pet = pets_do_dono[pet_idx - 1]
        except (ValueError, IndexError):
            print("Opção inválida.")
            return

        agora = datetime.datetime.now()
        agendamentos_pet = [
            ag for ag in agendamento_controller.listar_agendamentos() 
            if ag.pet == pet and ag.data_horario >= agora and not ag.cancelado
        ]
        if not agendamentos_pet:
            print(f"Não há agendamentos futuros para o pet {pet.nome}.")
            return
        print(f"Agendamentos futuros para {pet.nome}:")
        for i, ag in enumerate(agendamentos_pet, 1):
            print(f"{i} - {ag.data_horario.strftime('%Y-%m-%d %H:%M')} - Serviço: {ag.servico.nome}")
        try:
            agendamento_idx = int(input("Escolha o número do agendamento: ").strip())
            agendamento = agendamentos_pet[agendamento_idx - 1]
        except (ValueError, IndexError):
            print("Opção inválida.")
            return

        try:
            margem = float(input("Margem de lucro para a venda (%): ").strip())
            if margem < 0:
                raise ValueError()
        except ValueError:
            print("Margem inválida.")
            return

        produtos_usados = [(p, 1) for p in produto_controller.listar_produtos()]

        try:
            venda = venda_controller.criar_venda(
                agendamento,
                produtos_usados,
                despesa_controller.listar_despesas(),
                margem
            )
            print("Venda realizada:", venda)
        except Exception as e:
            print("Erro ao realizar venda:", e)
