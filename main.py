# main.py

from fastapi import FastAPI
from src.controllers.veiculo_controller import router as veiculo_router
from src.controllers.servico_controller import router as servico_router

app = FastAPI()

app.include_router(veiculo_router, prefix="/api")
app.include_router(servico_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "API de Gerenciamento de Frota de Veículos e Serviços"}