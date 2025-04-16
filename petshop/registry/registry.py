from services.dono_service        import DonoService
from services.pet_service         import PetService
from services.produto_service     import ProdutoService
from services.servico_service     import ServicoService
from services.agendamento_service import AgendamentoService
from services.despesa_service     import DespesaService
from services.venda_service       import VendaService
from services.relatorio_service   import RelatorioService

from controllers.dono_controller        import DonoController
from controllers.pet_controller         import PetController
from controllers.produto_controller     import ProdutoController
from controllers.servico_controller     import ServicoController
from controllers.agendamento_controller import AgendamentoController
from controllers.despesa_controller     import DespesaController
from controllers.venda_controller       import VendaController
from controllers.relatorio_controller   import RelatorioController

dono_service        = DonoService()
pet_service         = PetService(dono_service)    
produto_service     = ProdutoService()
servico_service     = ServicoService()
agendamento_service = AgendamentoService()
despesa_service     = DespesaService()
venda_service       = VendaService()
relatorio_service   = RelatorioService()

dono_controller        = DonoController(dono_service)
pet_controller         = PetController(pet_service)
produto_controller     = ProdutoController(produto_service)
servico_controller     = ServicoController(servico_service)
agendamento_controller = AgendamentoController(agendamento_service)
despesa_controller     = DespesaController(despesa_service)
venda_controller       = VendaController(venda_service)
relatorio_controller   = RelatorioController(relatorio_service)

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
