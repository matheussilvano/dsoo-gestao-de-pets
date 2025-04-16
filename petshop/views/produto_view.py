from controllers.produto_controller import ProdutoController

def gerenciar_produto(prod_ctrl: ProdutoController) -> None:
    while True:
        print("\n===== Gerenciar Produtos =====")
        print("1 - Criar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Excluir Produto")
        print("5 - Voltar")
        opc = input("Escolha uma opção: ").strip()
        if opc == "1":
            nome = input("Nome do produto: ").strip()
            try:
                quantidade = int(input("Quantidade em estoque: ").strip())
                custo = float(input("Custo unitário: ").strip())
            except ValueError:
                print("Valores inválidos.")
                continue
            try:
                prod = prod_ctrl.criar_produto(nome, quantidade, custo)
                print("Produto cadastrado:", prod)
            except Exception as e:
                print("Erro:", e)
        elif opc == "2":
            prods = prod_ctrl.listar_produtos()
            if not prods:
                print("Nenhum produto cadastrado.")
            else:
                for p in prods:
                    print(p)
        elif opc == "3":
            nome = input("Nome do produto a atualizar: ").strip()
            novo_nome = input("Novo nome (ou vazio): ").strip()
            nova_qtd = input("Nova quantidade (ou vazio): ").strip()
            novo_custo = input("Novo custo (ou vazio): ").strip()
            dados = {}
            if novo_nome: dados["nome"] = novo_nome
            if nova_qtd:
                try:
                    dados["quantidade_estoque"] = int(nova_qtd)
                except ValueError:
                    print("Quantidade inválida.")
                    continue
            if novo_custo:
                try:
                    dados["custo_unitario"] = float(novo_custo)
                except ValueError:
                    print("Custo inválido.")
                    continue
            if prod_ctrl.atualizar_produto(nome, **dados):
                print("Produto atualizado.")
            else:
                print("Produto não encontrado.")
        elif opc == "4":
            nome = input("Nome do produto a excluir: ").strip()
            if prod_ctrl.excluir_produto(nome):
                print("Produto excluído.")
            else:
                print("Produto não encontrado.")
        elif opc == "5":
            break
        else:
            print("Opção inválida.")
