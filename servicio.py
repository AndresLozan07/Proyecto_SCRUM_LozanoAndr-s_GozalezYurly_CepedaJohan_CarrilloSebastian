class Servicio:
    def __init__(self, nombre, cupo_maximo):
        self.nombre = nombre
        self.cupo_maximo = cupo_maximo
        self.clientes_matriculados = []

    def cupo_disponible(self):
        return self.cupo_maximo - len(self.clientes_matriculados)

# 5 servicios del Gimnasio ForceTech
servicios = []
servicios.append(Servicio("yoga", 10))
servicios.append(Servicio("pilates", 15))
servicios.append(Servicio("entrenamiento personalizado", 5))
servicios.append(Servicio("acceso a la piscina", 20))
servicios.append(Servicio("uso del gimnasio general", 30))