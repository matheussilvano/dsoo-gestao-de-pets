from __future__ import annotations
import re
from typing import List, Optional
from models.dono import Dono
from utils.utils import BaseService

class DonoService(BaseService):
    PHONE_RE = re.compile(r"^\d{8,15}$")

    def __init__(self) -> None:
        self._donos: List[Dono] = []


    def criar_dono(self, nome: str, telefone: str, endereco: str) -> Dono:
        self.validacao_unique(self._donos, "nome", nome, f"Dono '{nome}' já cadastrado.")
        dono = Dono(nome, telefone, endereco)
        self._donos.append(dono)
        return dono

    def listar_donos(self) -> List[Dono]:
        return self._donos

    def buscar_dono_por_nome(self, nome: str) -> Optional[Dono]:
        return next((d for d in self._donos if d.nome == nome), None)

    def atualizar_dono(self, nome_dono_atual: str, **kwargs) -> bool:
        d = self.buscar_dono_por_nome(nome_dono_atual)
        if not d:
            return False
        if "nome" in kwargs and kwargs["nome"] != nome_dono_atual:
            self.validacao_unique(self._donos, "nome", kwargs["nome"], f"Dono '{kwargs['nome']}' já cadastrado.")
        if "telefone" in kwargs and not self.PHONE_RE.fullmatch(kwargs["telefone"]):
            raise ValueError("Telefone inválido.")
        d.update(**kwargs)
        return True

    def excluir_dono(self, nome: str) -> bool:
        d = self.buscar_dono_por_nome(nome)
        if d:
            self._donos.remove(d)
            return True
        return False
