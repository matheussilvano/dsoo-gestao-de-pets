from controllers.servico_controller import ServicoController

def gerenciar_servico(serv_ctrl: ServicoController) -> None:
    while True:
        print("\n===== Gerenciar Serviços =====")
        print("1 - Criar Serviço")
        print("2 - Listar Serviços")
        print("3 - Atualizar Serviço")
        print("4 - Excluir Serviço")
        print("5 - Voltar")
        opc = input("Escolha uma opção: ").strip()
        if opc == "1":
            nome = input("Nome do serviço: ").strip()
            descricao = input("Descrição do serviço: ").strip()
            try:
                preco = float(input("Preço do serviço: ").strip())
            except ValueError:
                print("Preço inválido.")
                continue
            try:
                s = serv_ctrl.criar_servico(nome, descricao, preco)
                print("Serviço cadastrado:", s)
            except Exception as e:
                print("Erro:", e)
        elif opc == "2":
            servicos = serv_ctrl.listar_servicos()
            if not servicos:
                print("Nenhum serviço cadastrado.")
            else:
                for s in servicos:
                    print(s)
        elif opc == "3":
            nome = input("Nome do serviço a atualizar: ").strip()
            novo_nome = input("Novo nome (ou vazio): ").strip()
            nova_desc = input("Nova descrição (ou vazio): ").strip()
            novo_preco = input("Novo preço (ou vazio): ").strip()
            dados = {}
            if novo_nome: dados["nome"] = novo_nome
            if nova_desc: dados["descricao"] = nova_desc
            if novo_preco:
                try:
                    dados["preco"] = float(novo_preco)
                except ValueError:
                    print("Preço inválido.")
                    continue
            if serv_ctrl.atualizar_servico(nome, **dados):
                print("Serviço atualizado.")
            else:
                print("Serviço não encontrado.")
        elif opc == "4":
            nome = input("Nome do serviço a excluir: ").strip()
            if serv_ctrl.excluir_servico(nome):
                print("Serviço excluído.")
            else:
                print("Serviço não encontrado.")
        elif opc == "5":
            break
        else:
            print("Opção inválida.")
