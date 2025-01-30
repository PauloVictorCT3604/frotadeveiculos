# src/dao/servico_dao.py

import json
from typing import List, Optional
from src.models.servico_model import Servico

class ServicoDAO:
    def __init__(self, db_path: str = "data/db.json"):
        self.db_path = db_path
        self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(self.db_path, "r") as file:
                self.db = json.load(file)
        except FileNotFoundError:
            self.db = {"veiculos": [], "servicos": []}

    def salvar_dados(self):
        with open(self.db_path, "w") as file:
            json.dump(self.db, file, indent=4)

    def adicionar_servico(self, servico: Servico) -> Servico:
        self.db["servicos"].append(servico.__dict__)
        self.salvar_dados()
        return servico

    def buscar_servico_por_id(self, servico_id: str) -> Optional[Servico]:
        for servico_data in self.db["servicos"]:
            if servico_data["id"] == servico_id:
                return Servico(**servico_data)
        return None

    def listar_servicos(self) -> List[Servico]:
        return [Servico(**servico_data) for servico_data in self.db["servicos"]]