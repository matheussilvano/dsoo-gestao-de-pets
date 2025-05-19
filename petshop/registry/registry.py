from controllers.dono_controller        import DonoController
from controllers.pet_controller         import PetController
from controllers.produto_controller     import ProdutoController
from controllers.servico_controller     import ServicoController
from controllers.agendamento_controller import AgendamentoController
from controllers.despesa_controller     import DespesaController
from controllers.venda_controller       import VendaController
from controllers.relatorio_controller   import RelatorioController

dono_controller        = DonoController()
pet_controller = PetController(dono_controller)
produto_controller     = ProdutoController()
servico_controller     = ServicoController()
agendamento_controller = AgendamentoController()
despesa_controller     = DespesaController()
venda_controller       = VendaController()
relatorio_controller   = RelatorioController()

__all__: list[str] = [
    "dono_controller",
    "pet_controller",
    "produto_controller",
    "servico_controller",
    "agendamento_controller",
    "despesa_controller",
    "venda_controller",
    "relatorio_controller",
]
