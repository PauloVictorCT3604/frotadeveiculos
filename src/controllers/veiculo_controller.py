# src/controllers/veiculo_controller.py

from fastapi import APIRouter, HTTPException
from src.services.veiculo_service import VeiculoService
from src.schemas.veiculo_schema import VeiculoSchema, VeiculoCreateSchema, VeiculoUpdateSchema

router = APIRouter()
service = VeiculoService()

@router.get("/veiculos", response_model=list[VeiculoSchema])
def listar_veiculos():
    return service.listar_veiculos()

@router.get("/veiculos/{veiculo_id}", response_model=VeiculoSchema)
def buscar_veiculo_por_id(veiculo_id: str):
    try:
        return service.buscar_veiculo_por_id(veiculo_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/veiculos/modelo/{modelo}", response_model=list[VeiculoSchema])
def buscar_veiculos_por_modelo(modelo: str):
    try:
        return service.buscar_veiculos_por_modelo(modelo)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/veiculos/placa/{placa}", response_model=VeiculoSchema)
def buscar_veiculo_por_placa(placa: str):
    try:
        return service.buscar_veiculo_por_placa(placa)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/veiculos", response_model=VeiculoSchema)
def adicionar_veiculo(veiculo: VeiculoCreateSchema):
    try:
        return service.adicionar_veiculo(veiculo.modelo, veiculo.categoria, veiculo.placa)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/veiculos/{veiculo_id}", response_model=VeiculoSchema)
def atualizar_veiculo(veiculo_id: str, veiculo: VeiculoUpdateSchema):
    try:
        return service.atualizar_veiculo(veiculo_id, veiculo.modelo, veiculo.categoria, veiculo.placa)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/veiculos/{veiculo_id}", response_model=VeiculoSchema)
def deletar_veiculo(veiculo_id: str):
    try:
        return service.deletar_veiculo(veiculo_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))