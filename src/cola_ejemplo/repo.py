from modelos import Trabajo

class RepoMemoria:
    """Su función es guardar Trabajos en memoria, sin saber de reglas."""

    def __init__(self) -> None:
        self._por_id: dict[int, Trabajo] = {}

    def guardar(self, trabajo: Trabajo) -> None:
        self._por_id[trabajo.id] = trabajo

    def obtener_por_id(self, id: int) -> Trabajo | None:
        return self._por_id.get(id)

    def listar(self) -> list[Trabajo]:
        return list(self._por_id.values())

