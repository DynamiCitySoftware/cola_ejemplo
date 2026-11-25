from cola_ejemplo.modelos import Trabajo, Estado
from cola_ejemplo.repo import RepoMemoria
from cola_ejemplo.servicio import Servicio

repo = RepoMemoria()

servicio = Servicio(repo)

servicio.encolar("torneado")

listado_trabajos= repo.listar()

print(listado_trabajos)
