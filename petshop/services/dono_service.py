from models.dono import Dono
from typing import List, Optional

class DonoService:
    def __init__(self) -> None:
        self._donos: List[Dono] = []

    def criar_dono(self, nome: str, telefone: str, endereco: str) -> Dono:
        dono = Dono(nome, telefone, endereco)
        self._donos.append(dono)
        return dono

    def listar_donos(self) -> List[Dono]:
        return self._donos

    def buscar_dono_por_nome(self, nome: str) -> Optional[Dono]:
        for dono in self._donos:
            if dono.nome == nome:
                return dono
        return None

    def atualizar_dono(self, nome_dono_atual: str, **kwargs) -> bool:
        d = self.buscar_dono_por_nome(nome_dono_atual)
        if d:
            d.update(**kwargs)
            return True
        return False

    def excluir_dono(self, nome: str) -> bool:
        d = self.buscar_dono_por_nome(nome)
        if d:
            self._donos.remove(d)
            return True
        return False
