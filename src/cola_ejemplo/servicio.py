from modelos import Trabajo, Estado
from repo import RepoMemoria


def encolar(repo: RepoMemoria, id_trabajo: int, nombre: str):
    trabajo = Trabajo(id_trabajo, nombre, Estado.PENDIENTE)
    repo.guardar(trabajo)


def iniciar(repo: RepoMemoria, id_trabajo: int):
    trabajo = repo.obtener_por_id(id_trabajo)
    trabajo.estado = Estado.EN_CURSO


def terminar(repo: RepoMemoria, id_trabajo: int):
    trabajo = repo.obtener_por_id(id_trabajo)
    trabajo.estado = Estado.TERMINADO