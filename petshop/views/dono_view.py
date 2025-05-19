from controllers.dono_controller import DonoController

class DonoView:
    def __init__(self, dono_ctrl):
        self.dono_ctrl = dono_ctrl

    def mostrar_menu(self):
        while True:
            print("\n===== Gerenciar Donos =====")
            print("1 - Criar Dono")
            print("2 - Listar Donos")
            print("3 - Atualizar Dono")
            print("4 - Excluir Dono")
            print("5 - Voltar")
            opc = input("Escolha uma opção: ").strip()
            if opc == "1":
                self.criar_dono()
            elif opc == "2":
                self.listar_donos()
            elif opc == "3":
                self.atualizar_dono()
            elif opc == "4":
                self.excluir_dono()
            elif opc == "5":
                break
            else:
                print("Opção inválida.")

    def criar_dono(self):
        nome = input("Nome do dono: ").strip()
        telefone = input("Telefone do dono: ").strip()
        endereco = input("Endereço do dono: ").strip()
        try:
            dono = self.dono_ctrl.criar_dono(nome, telefone, endereco)
            print(f"Dono cadastrado: {dono}")
        except Exception as e:
            print("Erro ao cadastrar dono:", e)

    def listar_donos(self):
        donos = self.dono_ctrl.listar_donos()
        if not donos:
            print("Nenhum dono cadastrado.")
        else:
            for idx, d in enumerate(donos, 1):
                print(f"{idx}. {d}")

    def escolher_dono(self):
        donos = self.dono_ctrl.listar_donos()
        if not donos:
            print("Nenhum dono cadastrado.")
            return None
        print("Donos cadastrados:")
        for idx, dono in enumerate(donos, 1):
            print(f"{idx} - {dono}")
        try:
            escolha = int(input("Escolha o número do dono: ").strip())
            if 1 <= escolha <= len(donos):
                return donos[escolha - 1]
            else:
                print("Número inválido.")
                return None
        except ValueError:
            print("Entrada inválida. Digite um número.")
            return None

    def atualizar_dono(self):
        dono = self.escolher_dono()
        if not dono:
            return
        novo_nome = input("Novo nome (ou vazio): ").strip()
        novo_tel = input("Novo telefone (ou vazio): ").strip()
        novo_end = input("Novo endereço (ou vazio): ").strip()
        dados = {}
        if novo_nome: dados["nome"] = novo_nome
        if novo_tel: dados["telefone"] = novo_tel
        if novo_end: dados["endereco"] = novo_end
        if self.dono_ctrl.atualizar_dono(dono.nome, **dados):
            print("Dono atualizado.")
        else:
            print("Erro ao atualizar dono.")

    def excluir_dono(self):
        dono = self.escolher_dono()
        if not dono:
            return
        confirm = input(f"Confirma exclusão do dono '{dono.nome}'? (s/n): ").strip().lower()
        if confirm == "s":
            if self.dono_ctrl.excluir_dono(dono.nome):
                print("Dono excluído.")
            else:
                print("Erro ao excluir dono.")
        else:
            print("Exclusão cancelada.")
