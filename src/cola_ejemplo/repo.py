class RepoMemoria:
    def __init__(self):
        self.cola = list()
    

    def guardar(self, trabajo):
        self.cola.append(trabajo)

    

    def listar(self):
        return [trabajo.uid for trabajo in trabajos]

    
    def obtener_por_uid(self, uid):
        for trabajo in self.cola:
            if trabajo.uid == uid:
                return trabajo

