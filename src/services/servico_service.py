# src/services/servico_service.py

from typing import List
from src.dao.servico_dao import ServicoDAO
from src.dao.veiculo_dao import VeiculoDAO
from src.models.servico_model import Servico
from src.models.veiculo_model import Veiculo

class ServicoService:
    def __init__(self):
        self.servico_dao = ServicoDAO()
        self.veiculo_dao = VeiculoDAO()

    def gerar_id(self):
        servicos = self.servico_dao.listar_servicos()
        if not servicos:
            return "S1"
        ultimo_id = servicos[-1].id
        numero = int(ultimo_id[1:]) + 1
        return f"S{numero}"

    def adicionar_servico(self, categoria: str, descricao: str, veiculo_id: str) -> Servico:
        # Verifica se o veículo existe e se a categoria é compatível
        veiculo = self.veiculo_dao.buscar_veiculo_por_id(veiculo_id)
        if not veiculo:
            raise ValueError("Veículo não encontrado")
        if veiculo.categoria != categoria:
            raise ValueError("Categoria do veículo não compatível com o serviço")

        # Atualiza o status do veículo para "Em serviço"
        self.veiculo_dao.atualizar_status_veiculo(veiculo_id, True)

        # Cria o serviço
        novo_servico = Servico(
            id=self.gerar_id(),
            categoria=categoria,
            descricao=descricao,
            veiculo_id=veiculo_id
        )
        return self.servico_dao.adicionar_servico(novo_servico)

    def finalizar_servico(self, servico_id: str) -> Servico:
        servico = self.servico_dao.buscar_servico_por_id(servico_id)
        if not servico:
            raise ValueError("Serviço não encontrado")

        # Atualiza o status do veículo para "Disponivel"
        self.veiculo_dao.atualizar_status_veiculo(servico.veiculo_id, False)

        return servico

    def listar_servicos(self) -> List[Servico]:
        return self.servico_dao.listar_servicos()