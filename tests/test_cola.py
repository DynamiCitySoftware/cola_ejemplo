import pytest

from cola_ejemplo.modelos import Estado
from cola_ejemplo.repo import RepoMemoria
from cola_ejemplo.servicio import Servicio, TransicionInvalida, TrabajoNoExiste


def _servicio_nuevo():
    repo = RepoMemoria()
    return Servicio(repo)


def test_encolar_deja_en_pendiente():
    servicio = _servicio_nuevo()
    trabajo = servicio.encolar("limado")
    assert trabajo.estado is Estado.PENDIENTE


def test_iniciar_pasa_a_en_curso():
    servicio = _servicio_nuevo()
    trabajo = servicio.encolar("limado")
    iniciado = servicio.iniciar(trabajo.id)
    assert iniciado.estado is Estado.EN_CURSO


def test_terminar_pasa_a_terminado():
    servicio = _servicio_nuevo()
    trabajo = servicio.encolar("limado")
    servicio.iniciar(trabajo.id)
    terminado = servicio.terminar(trabajo.id)
    assert terminado.estado is Estado.TERMINADO


def test_iniciar_terminado_falla():
    servicio = _servicio_nuevo()
    trabajo = servicio.encolar("limado")
    servicio.iniciar(trabajo.id)
    servicio.terminar(trabajo.id)
    with pytest.raises(TransicionInvalida):
        servicio.iniciar(trabajo.id)


def test_terminar_pendiente_falla():
    servicio = _servicio_nuevo()
    trabajo = servicio.encolar("limado")
    with pytest.raises(TransicionInvalida):
        servicio.terminar(trabajo.id)


def test_iniciar_con_id_inexistente():
    servicio = _servicio_nuevo()
    with pytest.raises(TrabajoNoExiste):
        servicio.iniciar(8)