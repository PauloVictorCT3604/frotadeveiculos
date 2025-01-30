# src/dao/veiculo_dao.py

import json
from typing import List, Optional
from src.models.veiculo_model import Veiculo

class VeiculoDAO:
    def __init__(self, db_path: str = "db.json"):
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

    def adicionar_veiculo(self, veiculo: Veiculo) -> Veiculo:
        self.db["veiculos"].append(veiculo.__dict__)
        self.salvar_dados()
        return veiculo

    def buscar_veiculo_por_id(self, veiculo_id: str) -> Optional[Veiculo]:
        for veiculo_data in self.db["veiculos"]:
            if veiculo_data["id"] == veiculo_id:
                return Veiculo(**veiculo_data)
        return None

    def atualizar_status_veiculo(self, veiculo_id: str, trabalhando: bool) -> Optional[Veiculo]:
        for veiculo_data in self.db["veiculos"]:
            if veiculo_data["id"] == veiculo_id:
                veiculo_data["trabalhando"] = trabalhando
                veiculo_data["status"] = "Em serviço" if trabalhando else "Disponivel"
                self.salvar_dados()
                return Veiculo(**veiculo_data)
        return None

    def listar_veiculos(self) -> List[Veiculo]:
        return [Veiculo(**veiculo_data) for veiculo_data in self.db["veiculos"]]