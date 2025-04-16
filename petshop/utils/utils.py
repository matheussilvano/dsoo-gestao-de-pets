def cadastrar_despesas_iniciais(despesa_service):
    print("Cadastre as despesas iniciais (ex: 'água', 'luz', etc.). Para encerrar, digite 'fim'.")
    while True:
        descricao = input("Digite o nome da despesa: ").strip()
        if descricao.lower() == 'fim':
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
