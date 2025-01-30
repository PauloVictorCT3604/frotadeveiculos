# src/models/servico_model.py

class Servico:
    def __init__(self, id: str, categoria: str, descricao: str, veiculo_id: str):
        self.id = id
        self.categoria = categoria
        self.descricao = descricao
        self.veiculo_id = veiculo_id