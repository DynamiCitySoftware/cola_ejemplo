from cola_ejemplo.modelos import Trabajo, Estado
from cola_ejemplo.repo import RepoMemoria


class Servicio:
    def __init__(self, repo: RepoMemoria):
        self.repo = RepoMemoria()
        self.proximo_id = 1


    def encolar(self, id_trabajo: int, nombre: str):
        trabajo = Trabajo(self.proximo_id, nombre, Estado.PENDIENTE)
        self.repo.guardar(trabajo)
        return trabajo
        

    def iniciar(self, id_trabajo: int):
        try:
            trabajo = self.repo.obtener_por_id(id_trabajo)
        except ValueError:
            print(f"No existe un trabajo con el id: {id_trabajo}")

        trabajo = Trabajo(id_trabajo, trabajo.nombre, Estado.EN_CURSO)
        self.repo.guardar(trabajo)


    def terminar(self, id_trabajo: int):
        try:
            trabajo = self.repo.obtener_por_id(id_trabajo)
        except ValueError:
            print(f"No existe un trabajo con el id: {id_trabajo}")

        trabajo = self.repo.obtener_por_id(id_trabajo)
        trabajo = Trabajo(id_trabajo, trabajo.nombre, Estado.TERMINADO)
        self.repo.guardar(trabajo)
