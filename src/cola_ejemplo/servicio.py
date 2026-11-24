from cola_ejemplos.modelos import Trabajo, Estado
from cola_ejemplos.repo import RepoMemoria


class Servicio:
    def __init__(self):
        self.repo = RepoMemoria()
        self.proximo_id = 1


    def encolar(id_trabajo: int, nombre: str):
        trabajo = Trabajo(self.proximo_id, nombre, Estado.PENDIENTE)
        self.repo.guardar(trabajo)
        return trabajo
        

    def iniciar(id_trabajo: int):
        try:
            trabajo = self.repo.obtener_por_id(id_trabajo)
        except ValueError:
            print(f"No existe un trabajo con el id: {id_trabajo}")

        trabajo = Trabajo(id_trabajo, trabajo.nombre, Estado.EN_CURSO)
        self.repo.guardar(trabajo)


    def terminar(id_trabajo: int):
        try:
            trabajo = self.repo.obtener_por_id(id_trabajo)
        except ValueError:
            print(f"No existe un trabajo con el id: {id_trabajo}")

        trabajo = self.repo.obtener_por_id(id_trabajo)
        trabajo = Trabajo(id_trabajo, trabajo.nombre, Estado.TERMINADO)
        self.repo.guardar(trabajo)
