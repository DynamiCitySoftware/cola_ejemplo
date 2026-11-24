from __future__ import annotations
from enum import Enum
from dataclasses import dataclass

class Estado(Enum):
    EN_CURSO = "en_curso"
    TERMINADO = "terminado"
    PENDIENTE = "pendiente"


@dataclass(frozen=True)
class Trabajo:
    id: int
    nombre: str
    estado: Estado
        
