from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from .models.clientes import Cliente # Importa aquí tus modelos

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/technoshop")

async def init_db():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client.get_default_database()
    # Inicializa Beanie con los modelos
    await init_beanie(database=db, document_models=[Cliente])
    print("Conexión a MongoDB exitosa")
