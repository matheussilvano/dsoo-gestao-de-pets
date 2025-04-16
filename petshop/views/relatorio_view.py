from controllers.relatorio_controller import RelatorioController
from controllers.venda_controller import VendaController

def exibir_relatorio_vendas(relatorio_ctrl: RelatorioController, venda_ctrl: VendaController):
    print("\n===== Relatório de Vendas =====")
    vendas = venda_ctrl.listar_vendas()
    relatorio = relatorio_ctrl.gerar_relatorio_vendas(vendas)
    for chave, valor in relatorio.items():
        print(f"{chave}: {valor}")
