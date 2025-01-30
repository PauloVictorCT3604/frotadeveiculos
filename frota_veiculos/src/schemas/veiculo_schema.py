# src/schemas/veiculo_schema.py

from pydantic import BaseModel

class VeiculoSchema(BaseModel):
    id: str
    modelo: str
    categoria: str
    placa: str

class VeiculoCreateSchema(BaseModel):
    modelo: str
    categoria: str
    placa: str

class VeiculoUpdateSchema(BaseModel):
    modelo: str
    categoria: str
    placa: str