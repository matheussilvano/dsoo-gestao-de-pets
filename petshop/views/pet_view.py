from controllers.pet_controller import PetController

def gerenciar_pet(pet_ctrl: PetController) -> None:
    while True:
        print("\n===== Gerenciar Pets =====")
        print("1 - Criar Pet")
        print("2 - Listar Pets")
        print("3 - Atualizar Pet")
        print("4 - Excluir Pet")
        print("5 - Voltar")
        opc = input("Escolha uma opção: ").strip()
        if opc == "1":
            dono_nome = input("Nome do dono: ").strip()
            nome = input("Nome do pet: ").strip()
            especie = input("Espécie do pet: ").strip()
            raca = input("Raça do pet: ").strip()
            try:
                idade = int(input("Idade do pet: ").strip())
            except ValueError:
                print("Idade inválida.")
                continue
            try:
                pet = pet_ctrl.criar_pet(dono_nome, nome, especie, raca, idade)
                print(f"Pet cadastrado: {pet}")
            except Exception as e:
                print("Erro ao cadastrar pet:", e)
        elif opc == "2":
            pets = pet_ctrl.listar_pets()
            if not pets:
                print("Nenhum pet cadastrado.")
            else:
                for p in pets:
                    print(p)
        elif opc == "3":
            nome = input("Nome do pet a atualizar: ").strip()
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
                    continue
            if "nome" in dados:
                del dados["nome"]
            if pet_ctrl.atualizar_pet(nome, **dados):
                print("Pet atualizado.")
            else:
                print("Pet não encontrado.")
        elif opc == "4":
            nome = input("Nome do pet a excluir: ").strip()
            if pet_ctrl.excluir_pet(nome):
                print("Pet excluído.")
            else:
                print("Pet não encontrado.")
        elif opc == "5":
            break
        else:
            print("Opção inválida.")
