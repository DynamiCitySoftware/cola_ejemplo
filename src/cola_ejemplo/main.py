from servicio import encolar, iniciar, terminar
from modelos import Trabajo, Estado
from repo import RepoMemoria

repo = RepoMemoria()

encolar(repo, 1, "limado")

listado_trabajos= repo.listar()

print(listado_trabajos)