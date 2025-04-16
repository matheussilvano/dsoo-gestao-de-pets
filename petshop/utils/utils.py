def cadastrar_despesas_iniciais(despesa_service):
    print("Cadastre as despesas iniciais (ex: 'água', 'luz', etc.). Para encerrar, digite 'salvar'.")
    while True:
        descricao = input("Digite o nome da despesa: ").strip()
        if descricao.lower() == 'salvar':
            break
        if descricao == "":
            print("O nome da despesa não pode ser vazio. Tente novamente.")
            continue
        try:
            valor_input = input(f"Digite o valor para '{descricao}': ").strip()
            valor = float(valor_input)
            despesa_service.criar_despesa(descricao, valor)
            print(f"Despesa '{descricao}' cadastrada com sucesso!")
        except ValueError:
            print("Valor inválido. Tente novamente.")
    if not despesa_service.listar_despesas():
        print("Você deve cadastrar pelo menos uma despesa!")
        cadastrar_despesas_iniciais(despesa_service)


class BaseService:
    @staticmethod
    def validacao_unique(collection, attr: str, value, message: str) -> None:
        if any(getattr(obj, attr) == value for obj in collection):
            raise ValueError(message)
