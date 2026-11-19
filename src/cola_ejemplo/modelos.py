from enum import Enum
from __future__ import annotations
from dataclasses import dataclass

class Estado(Enum):
    EN_CURSO = "en_curso"
    TERMINADO = "terminado"
    PENDIENTE = "pendiente"


@dataclass
class Trabajo:
    uid: int
    nombre: str
    estado: Estado

        
