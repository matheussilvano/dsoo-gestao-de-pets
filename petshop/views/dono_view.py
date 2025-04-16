from controllers.dono_controller import DonoController

def gerenciar_dono(dono_ctrl: DonoController) -> None:
    while True:
        print("\n===== Gerenciar Donos =====")
        print("1 - Criar Dono")
        print("2 - Listar Donos")
        print("3 - Atualizar Dono")
        print("4 - Excluir Dono")
        print("5 - Voltar")
        opc = input("Escolha uma opção: ").strip()
        if opc == "1":
            nome = input("Nome do dono: ").strip()
            telefone = input("Telefone do dono: ").strip()
            endereco = input("Endereço do dono: ").strip()
            try:
                dono = dono_ctrl.criar_dono(nome, telefone, endereco)
                print(f"Dono cadastrado: {dono}")
            except Exception as e:
                print("Erro ao cadastrar dono:", e)
        elif opc == "2":
            donos = dono_ctrl.listar_donos()
            if not donos:
                print("Nenhum dono cadastrado.")
            else:
                for d in donos:
                    print(d)
        elif opc == "3":
            nome = input("Nome do dono a atualizar: ").strip()
            novo_nome = input("Novo nome (ou vazio): ").strip()
            novo_tel = input("Novo telefone (ou vazio): ").strip()
            novo_end = input("Novo endereço (ou vazio): ").strip()
            dados = {}
            if novo_nome: dados["nome"] = novo_nome
            if novo_tel: dados["telefone"] = novo_tel
            if novo_end: dados["endereco"] = novo_end
            if dono_ctrl.atualizar_dono(nome, **dados):
                print("Dono atualizado.")
            else:
                print("Dono não encontrado.")
        elif opc == "4":
            nome = input("Nome do dono a excluir: ").strip()
            if dono_ctrl.excluir_dono(nome):
                print("Dono excluído.")
            else:
                print("Dono não encontrado.")
        elif opc == "5":
            break
        else:
            print("Opção inválida.")
