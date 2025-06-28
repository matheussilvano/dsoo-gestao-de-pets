from typing import List, Dict, Tuple
from collections import Counter
from models.venda import Venda
from models.relatorio import RelatorioVendas
from models.pet import Pet
from models.dono import Dono
from models.produto import Produto
from models.servico import Servico

class RelatorioController:
    def gerar_relatorio_vendas(self, vendas: List[Venda]) -> Dict[str, float]:
        r = RelatorioVendas(vendas)
        return r.gerar_relatorio()

    def gerar_ranking_donos_por_gasto(self, vendas: List[Venda]) -> List[Tuple[Dono, float]]:
        gastos_por_dono = Counter()
        for venda in vendas:
            dono = venda.agendamento.pet.dono
            gastos_por_dono[dono] += venda.valor_total
        
        ranking_ordenado = sorted(gastos_por_dono.items(), key=lambda item: item[1], reverse=True)
        return ranking_ordenado

    def gerar_ranking_pets_por_vendas(self, vendas: List[Venda]) -> List[Tuple[Pet, int]]:
        vendas_por_pet = Counter()
        for venda in vendas:
            pet = venda.agendamento.pet
            vendas_por_pet[pet] += 1

        ranking_ordenado = sorted(vendas_por_pet.items(), key=lambda item: item[1], reverse=True)
        return ranking_ordenado

    def gerar_relatorio_produtos_mais_usados(self, vendas: List[Venda]) -> List[Tuple[Produto, int]]:
        uso_produtos = Counter()
        for venda in vendas:
            for produto, quantidade in venda.produtos_usados:
                uso_produtos[produto] += quantidade

        ranking_ordenado = sorted(uso_produtos.items(), key=lambda item: item[1], reverse=True)
        return ranking_ordenado

    def gerar_relatorio_servicos_mais_vendidos(self, vendas: List[Venda]) -> List[Tuple[Servico, int]]:
        vendas_por_servico = Counter()
        for venda in vendas:
            servico = venda.agendamento.servico
            vendas_por_servico[servico] += 1
        
        ranking_ordenado = sorted(vendas_por_servico.items(), key=lambda item: item[1], reverse=True)
        return ranking_ordenado