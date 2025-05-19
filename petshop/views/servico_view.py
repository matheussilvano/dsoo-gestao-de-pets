from controllers.servico_controller import ServicoController

class ServicoView:
    def __init__(self, servico_ctrl: ServicoController):
        self.servico_ctrl = servico_ctrl

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
        try:
            servico = self.servico_ctrl.criar_servico(nome, descricao, preco)
            print("Serviço cadastrado:", servico)
        except Exception as e:
            print("Erro:", e)

    def _listar_servicos(self):
        servicos = self.servico_ctrl.listar_servicos()
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
        if self.servico_ctrl.atualizar_servico(nome, **dados):
            print("Serviço atualizado.")
        else:
            print("Serviço não encontrado.")

    def _excluir_servico(self):
        nome = input("Nome do serviço a excluir: ").strip()
        if self.servico_ctrl.excluir_servico(nome):
            print("Serviço excluído.")
        else:
            print("Serviço não encontrado.")
