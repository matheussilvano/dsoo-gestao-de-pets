from registry.registry import produto_controller

class ProdutoView:
    def __init__(self):
        pass

    def mostrar_menu(self) -> None:
        while True:
            print("\n===== Gerenciar Produtos =====")
            print("1 - Criar Produto")
            print("2 - Listar Produtos")
            print("3 - Atualizar Produto")
            print("4 - Excluir Produto")
            print("5 - Voltar")
            opc = input("Escolha uma opção: ").strip()

            if opc == "1":
                self.criar_produto()
            elif opc == "2":
                self.listar_produtos()
            elif opc == "3":
                self.atualizar_produto()
            elif opc == "4":
                self.excluir_produto()
            elif opc == "5":
                break
            else:
                print("Opção inválida.")

    def criar_produto(self):
        nome = input("Nome do produto: ").strip()
        try:
            quantidade = int(input("Quantidade em estoque: ").strip())
            custo = float(input("Custo unitário: ").strip())
        except ValueError:
            print("Valores inválidos.")
            return

        try:
            prod = produto_controller.criar_produto(nome, quantidade, custo)
            print("Produto cadastrado:", prod)
        except Exception as e:
            print("Erro:", e)

    def listar_produtos(self):
        prods = produto_controller.listar_produtos()
        if not prods:
            print("Nenhum produto cadastrado.")
        else:
            for p in prods:
                print(p)

    def atualizar_produto(self):
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
                return
        if novo_custo:
            try:
                dados["custo_unitario"] = float(novo_custo)
            except ValueError:
                print("Custo inválido.")
                return

        if produto_controller.atualizar_produto(nome, **dados):
            print("Produto atualizado.")
        else:
            print("Produto não encontrado.")

    def excluir_produto(self):
        nome = input("Nome do produto a excluir: ").strip()
        if produto_controller.excluir_produto(nome):
            print("Produto excluído.")
        else:
            print("Produto não encontrado.")
