import datetime
from controllers.venda_controller import VendaController
from controllers.pet_controller import PetController
from controllers.servico_controller import ServicoController
from controllers.produto_controller import ProdutoController
from controllers.despesa_controller import DespesaController
from controllers.agendamento_controller import AgendamentoController

class VendaView:
    def __init__(
        self,
        venda_ctrl: VendaController,
        pet_ctrl: PetController,
        servico_ctrl: ServicoController,
        produto_ctrl: ProdutoController,
        despesa_ctrl: DespesaController,
        agendamento_ctrl: AgendamentoController
    ):
        self.venda_ctrl = venda_ctrl
        self.pet_ctrl = pet_ctrl
        self.servico_ctrl = servico_ctrl
        self.produto_ctrl = produto_ctrl
        self.despesa_ctrl = despesa_ctrl
        self.agendamento_ctrl = agendamento_ctrl

    def realizar_venda(self):
        print("\n===== Realizar Venda =====")

        # Lista donos únicos a partir dos pets cadastrados
        donos = sorted({pet.dono for pet in self.pet_ctrl.listar_pets()}, key=lambda d: d.nome)
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

        # Lista pets do dono selecionado
        pets_do_dono = [pet for pet in self.pet_ctrl.listar_pets() if pet.dono == dono]
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

        # Lista agendamentos futuros disponíveis para o pet
        agora = datetime.datetime.now()
        agendamentos_pet = [
            ag for ag in self.agendamento_ctrl.listar_agendamentos() 
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

        # Pergunta a margem de lucro
        try:
            margem = float(input("Margem de lucro para a venda (%): ").strip())
            if margem < 0:
                raise ValueError()
        except ValueError:
            print("Margem inválida.")
            return

        # Usar todos os produtos cadastrados como usados na venda (pode adaptar se quiser)
        produtos_usados = [(p, 1) for p in self.produto_ctrl.listar_produtos()]

        try:
            venda = self.venda_ctrl.criar_venda(
                agendamento,
                produtos_usados,
                self.despesa_ctrl.listar_despesas(),
                margem
            )
            print("Venda realizada:", venda)
        except Exception as e:
            print("Erro ao realizar venda:", e)
