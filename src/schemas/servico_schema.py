# src/schemas/servico_schema.py

from pydantic import BaseModel

class ServicoSchema(BaseModel):
    id: str
    categoria: str
    descricao: str
    veiculo_id: str

class ServicoCreateSchema(BaseModel):
    categoria: str
    descricao: str
    veiculo_id: str