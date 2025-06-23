from registry.registry import servico_controller, produto_controller


class ServicoView:
    def __init__(self):
        pass

    def gerenciar_servicos(self) -> None:
        while True:
            print("\n===== Gerenciar Serviços =====")
            print("1 - Criar Serviço")
            print("2 - Listar Serviços")
            print("3 - Atualizar Serviço")
            print("4 - Excluir Serviço")
            print("5 - Voltar")
            opc = input("Escolha uma opção: ").strip()
            if opc == "1":
                self._criar_servico()
            elif opc == "2":
                self._listar_servicos()
            elif opc == "3":
                self._atualizar_servico()
            elif opc == "4":
                self._excluir_servico()
            elif opc == "5":
                break
            else:
                print("Opção inválida.")

    def _criar_servico(self):
        nome = input("Nome do serviço: ").strip()
        descricao = input("Descrição do serviço: ").strip()
        try:
            preco = float(input("Preço do serviço: ").strip())
        except ValueError:
            print("Preço inválido.")
            return

        produtos_disponiveis = produto_controller.listar_produtos()
        produtos_usados = []

        if not produtos_disponiveis:
            print("Nenhum produto cadastrado. O serviço será criado sem produtos.")
        else:
            print("Produtos disponíveis:")
            for i, p in enumerate(produtos_disponiveis, 1):
                print(f"{i} - {p.nome} (Estoque: {p.quantidade_estoque}, Custo: R${p.custo_unitario:.2f})")

            while True:
                escolha = input("Escolha o número do produto (ou vazio para encerrar): ").strip()
                if escolha == "":
                    break
                try:
                    idx = int(escolha) - 1
                    if idx < 0 or idx >= len(produtos_disponiveis):
                        print("Número inválido.")
                        continue
                    produto = produtos_disponiveis[idx]
                    qtd = int(input(f"Quantidade de '{produto.nome}' usada no serviço: ").strip())
                    if qtd <= 0:
                        print("Quantidade deve ser maior que zero.")
                        continue
                    produtos_usados.append((produto, qtd))
                except ValueError:
                    print("Entrada inválida.")

        try:
            servico = servico_controller.criar_servico(nome, descricao, preco, produtos_usados)
            print("Serviço cadastrado:", servico)
        except Exception as e:
            print("Erro:", e)

    def _listar_servicos(self):
        servicos = servico_controller.listar_servicos()
        if not servicos:
            print("Nenhum serviço cadastrado.")
        else:
            for s in servicos:
                print(s)

    def _atualizar_servico(self):
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
                return
        if servico_controller.atualizar_servico(nome, **dados):
            print("Serviço atualizado.")
        else:
            print("Serviço não encontrado.")

    def _excluir_servico(self):
        nome = input("Nome do serviço a excluir: ").strip()
        if servico_controller.excluir_servico(nome):
            print("Serviço excluído.")
        else:
            print("Serviço não encontrado.")
