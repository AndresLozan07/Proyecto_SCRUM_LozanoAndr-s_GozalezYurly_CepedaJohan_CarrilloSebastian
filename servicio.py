class Servicio:
    def __init__(self, codigo, nombre, capacidad_max):
        self.codigo = codigo
        self.nombre = nombre # yoga, pilates, entrenamiento personalizado, piscina, general
        self.capacidad_max = int(capacidad_max)

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(d):
        return Servicio(d["codigo"], d["nombre"], d["capacidad_max"])