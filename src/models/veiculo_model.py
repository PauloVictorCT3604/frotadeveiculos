# src/models/veiculo_model.py

class Veiculo:
    def __init__(self, id: str, modelo: str, categoria: str, placa: str, status: str = "Disponivel", trabalhando: bool = False):
        self.id = id
        self.modelo = modelo
        self.categoria = categoria
        self.placa = placa
        self.status = status
        self.trabalhando = trabalhando