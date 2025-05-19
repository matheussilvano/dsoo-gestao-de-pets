from controllers.relatorio_controller import RelatorioController
from controllers.venda_controller import VendaController

class RelatorioView:
    def __init__(self, relatorio_ctrl: RelatorioController, venda_ctrl: VendaController):
        self.relatorio_ctrl = relatorio_ctrl
        self.venda_ctrl = venda_ctrl

    def exibir_relatorio_vendas(self):
        print("\n===== Relatório de Vendas =====")
        vendas = self.venda_ctrl.listar_vendas()
        relatorio = self.relatorio_ctrl.gerar_relatorio_vendas(vendas)
        for chave, valor in relatorio.items():
            print(f"{chave}: {valor}")
