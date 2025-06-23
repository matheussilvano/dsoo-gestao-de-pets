from registry.registry import pet_controller, dono_controller

class PetView:
    def __init__(self):
        pass

    def mostrar_menu(self) -> None:
        while True:
            print("\n===== Gerenciar Pets =====")
            print("1 - Criar Pet")
            print("2 - Listar Pets")
            print("3 - Atualizar Pet")
            print("4 - Excluir Pet")
            print("5 - Voltar")
            opc = input("Escolha uma opção: ").strip()

            if opc == "1":
                self.criar_pet()
            elif opc == "2":
                self.listar_pets()
            elif opc == "3":
                self.atualizar_pet()
            elif opc == "4":
                self.excluir_pet()
            elif opc == "5":
                break
            else:
                print("Opção inválida.")

    def escolher_dono(self):
        donos = dono_controller.listar_donos()
        if not donos:
            print("Nenhum dono cadastrado.")
            return None
        print("Donos cadastrados:")
        for idx, dono in enumerate(donos, 1):
            print(f"{idx} - {dono}")
        try:
            escolha = int(input("Escolha o número do dono: ").strip())
            if 1 <= escolha <= len(donos):
                return donos[escolha - 1].nome
            else:
                print("Número inválido.")
                return None
        except ValueError:
            print("Entrada inválida. Digite um número.")
            return None

    def escolher_pet(self):
        pets = pet_controller.listar_pets()
        if not pets:
            print("Nenhum pet cadastrado.")
            return None
        print("Pets cadastrados:")
        for idx, pet in enumerate(pets, 1):
            print(f"{idx} - {pet}")
        try:
            escolha = int(input("Escolha o número do pet: ").strip())
            if 1 <= escolha <= len(pets):
                return pets[escolha - 1].nome
            else:
                print("Número inválido.")
                return None
        except ValueError:
            print("Entrada inválida. Digite um número.")
            return None

    def criar_pet(self):
        dono_nome = self.escolher_dono()
        if not dono_nome:
            return
        nome = input("Nome do pet: ").strip()
        especie = input("Espécie do pet: ").strip()
        raca = input("Raça do pet: ").strip()
        try:
            idade = int(input("Idade do pet: ").strip())
        except ValueError:
            print("Idade inválida.")
            return

        try:
            pet = pet_controller.criar_pet(dono_nome, nome, especie, raca, idade)
            print(f"Pet cadastrado: {pet}")
        except Exception as e:
            print("Erro ao cadastrar pet:", e)

    def listar_pets(self):
        pets = pet_controller.listar_pets()
        if not pets:
            print("Nenhum pet cadastrado.")
        else:
            for p in pets:
                print(p)

    def atualizar_pet(self):
        nome = self.escolher_pet()
        if not nome:
            return
        novo_nome = input("Novo nome (ou vazio): ").strip()
        nova_especie = input("Nova espécie (ou vazio): ").strip()
        nova_raca = input("Nova raça (ou vazio): ").strip()
        nova_idade = input("Nova idade (ou vazio): ").strip()

        dados = {}
        if novo_nome: dados["nome"] = novo_nome
        if nova_especie: dados["especie"] = nova_especie
        if nova_raca: dados["raca"] = nova_raca
        if nova_idade:
            try:
                dados["idade"] = int(nova_idade)
            except ValueError:
                print("Idade inválida.")
                return

        if "nome" in dados:
            del dados["nome"]  # Evita mudar chave primária

        if pet_controller.atualizar_pet(nome, **dados):
            print("Pet atualizado.")
        else:
            print("Pet não encontrado.")

    def excluir_pet(self):
        nome = self.escolher_pet()
        if not nome:
            return
        if pet_controller.excluir_pet(nome):
            print("Pet excluído.")
        else:
            print("Pet não encontrado.")
