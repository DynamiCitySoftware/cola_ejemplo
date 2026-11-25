from cola_ejemplo.modelos import Trabajo, Estado
from cola_ejemplo.repo import RepoMemoria

class TrabajoNoExiste(ValueError):
    '''Regla que impide trabajar sobre un trabajo que no pudo obtenerse'''


class Servicio:
    def __init__(self, repo: RepoMemoria):
        self.repo = repo
        self.proximo_id = 1


    def encolar(self, nombre: str):
        trabajo = Trabajo(self.proximo_id, nombre, Estado.PENDIENTE)
        self.repo.guardar(trabajo)
        self.proximo_id += 1
        return trabajo
        

    def iniciar(self, id_trabajo: int):
        trabajo = self._exigir(id_trabajo)
        trabajo = Trabajo(id_trabajo, trabajo.nombre, Estado.EN_CURSO)
        self.repo.guardar(trabajo)
        return trabajo


    def terminar(self, id_trabajo: int):
        trabajo = self._exigir(id_trabajo)
        trabajo = Trabajo(id_trabajo, trabajo.nombre, Estado.TERMINADO)
        self.repo.guardar(trabajo)
        return trabajo
    

    def _exigir(self, id_trabajo: int):
        trabajo = self.repo.obtener_por_id(id_trabajo)

        if not trabajo:
            raise ValueError

        return trabajo
