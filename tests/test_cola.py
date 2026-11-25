from cola_ejemplo.modelos import Trabajo, Estado
from cola_ejemplo.repo import RepoMemoria
from cola_ejemplo.servicio import Servicio, TrabajoNoExiste, TransicionInvalida

def test_ciclo():
    repo = RepoMemoria()
    servicio = Servicio(repo)
    
    trabajo_torneado = servicio.encolar("torneado")
    trabajo_torneado = servicio.iniciar(trabajo_torneado.id)
    trabajo_torneado = servicio.terminar(trabajo_torneado.id)

    print(repo.listar())