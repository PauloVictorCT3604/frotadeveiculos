# src/services/veiculo_service.py

from typing import List
from src.dao.veiculo_dao import VeiculoDAO
from src.models.veiculo_model import Veiculo

class VeiculoService:
    def __init__(self):
        self.dao = VeiculoDAO()

    def gerar_id(self):
        veiculos = self.dao.listar_veiculos()
        if not veiculos:
            return "V1"
        ultimo_id = veiculos[-1].id
        numero = int(ultimo_id[1:]) + 1
        return f"V{numero}"

    def adicionar_veiculo(self, modelo: str, categoria: str, placa: str) -> Veiculo:
        # Verifica se a placa já existe
        if self.dao.buscar_veiculo_por_placa(placa):
            raise ValueError("Placa já existe")
        novo_veiculo = Veiculo(
            id=self.gerar_id(),
            modelo=modelo,
            categoria=categoria,
            placa=placa
        )
        return self.dao.adicionar_veiculo(novo_veiculo)
    
    def atualizar_status_veiculo(self, veiculo_id: str, trabalhando: bool) -> Veiculo:
        veiculo = self.dao.buscar_veiculo_por_id(veiculo_id)
        if not veiculo:
            raise ValueError("Veículo não encontrado")
        return self.dao.atualizar_status_veiculo(veiculo_id, trabalhando)


    def buscar_veiculo_por_id(self, veiculo_id: str) -> Veiculo:
        veiculo = self.dao.buscar_veiculo_por_id(veiculo_id)
        if not veiculo:
            raise ValueError("Veículo não encontrado")
        return veiculo

    def buscar_veiculos_por_modelo(self, modelo: str) -> List[Veiculo]:
        veiculos = self.dao.buscar_veiculos_por_modelo(modelo)
        if not veiculos:
            raise ValueError("Nenhum veículo encontrado com este modelo")
        return veiculos

    def buscar_veiculo_por_placa(self, placa: str) -> Veiculo:
        veiculo = self.dao.buscar_veiculo_por_placa(placa)
        if not veiculo:
            raise ValueError("Veículo não encontrado")
        return veiculo

    def atualizar_veiculo(self, veiculo_id: str, modelo: str, categoria: str, placa: str) -> Veiculo:
        veiculo = self.dao.buscar_veiculo_por_id(veiculo_id)
        if not veiculo:
            raise ValueError("Veículo não encontrado")
        # Verifica se a nova placa já existe em outro veículo
        if placa != veiculo.placa and self.dao.buscar_veiculo_por_placa(placa):
            raise ValueError("Placa já existe")
        veiculo_atualizado = Veiculo(veiculo_id, modelo, categoria, placa)
        return self.dao.atualizar_veiculo(veiculo_id, veiculo_atualizado)

    def deletar_veiculo(self, veiculo_id: str) -> Veiculo:
        veiculo = self.dao.deletar_veiculo(veiculo_id)
        if not veiculo:
            raise ValueError("Veículo não encontrado")
        return veiculo

    def listar_veiculos(self) -> List[Veiculo]:
        return self.dao.listar_veiculos()