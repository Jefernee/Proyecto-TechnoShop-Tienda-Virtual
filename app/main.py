from fastapi import FastAPI
import asyncio

from app.config import init_db  # Asegúrate de que la importación coincida con tu config.py
from app.models.clientes import Cliente, ClienteCreate

app = FastAPI(title="TechnoShop MX API")

# Inicializar la base de datos al iniciar la app
@app.on_event("startup")
async def startup_event():
    await init_db()

# Ruta de prueba
@app.get("/")
async def root():
    return {"message": "API de TechnoShop MX funcionando!"}

# Crear un cliente de prueba
@app.post("/clientes/")
async def crear_cliente(cliente: ClienteCreate):
    nuevo_cliente = Cliente(**cliente.dict())
    await nuevo_cliente.insert()
    return {"message": "Cliente creado", "cliente": cliente}
