from beanie import Document
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Modelo para crear un cliente
class ClienteCreate(BaseModel):
    nombre: str
    correo: str
    telefono: str
    direccion: str
    puntos_fidelidad: int = 0
    participa_rifa: bool = False

# Modelo principal de la colección Clientes
class Cliente(Document):
    nombre: str
    correo: str
    telefono: str
    direccion: str
    puntos_fidelidad: int = 0
    participa_rifa: bool = False
    fecha_creacion: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "clientes"  # nombre de la colección en MongoDB
