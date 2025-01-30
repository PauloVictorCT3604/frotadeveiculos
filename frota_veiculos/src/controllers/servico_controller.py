# src/controllers/servico_controller.py

from fastapi import APIRouter, HTTPException
from src.services.servico_service import ServicoService
from src.schemas.servico_schema import ServicoSchema, ServicoCreateSchema

router = APIRouter()
service = ServicoService()

@router.post("/servicos", response_model=ServicoSchema)
def adicionar_servico(servico: ServicoCreateSchema):
    try:
        return service.adicionar_servico(servico.categoria, servico.descricao, servico.veiculo_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/servicos/{servico_id}/finalizar", response_model=ServicoSchema)
def finalizar_servico(servico_id: str):
    try:
        return service.finalizar_servico(servico_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/servicos", response_model=list[ServicoSchema])
def listar_servicos():
    return service.listar_servicos()