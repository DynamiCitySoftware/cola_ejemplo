from cola_ejemplo.modelos import Trabajo, Estado
from cola_ejemplo.repo import RepoMemoria
from cola_ejemplo.servicio import Servicio

repo = RepoMemoria()

servicio = Servicio(repo)

servicio.encolar(1, "limado")

listado_trabajos= repo.listar()

print(listado_trabajos)
