from registry.registry import relatorio_controller, venda_controller

class RelatorioView:
    def __init__(self):
        pass  # Não precisa mais receber controllers

    def exibir_relatorio_vendas(self):
        print("\n===== Relatório de Vendas =====")
        vendas = venda_controller.listar_vendas()
        relatorio = relatorio_controller.gerar_relatorio_vendas(vendas)
        for chave, valor in relatorio.items():
            print(f"{chave}: {valor}")
