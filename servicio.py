class Servicio:
    def __init__(self, codigo, nombre, cupo_max, entrenador_cedula, horario):
        self.codigo = codigo
        self.nombre = nombre
        self.cupo_max = cupo_max
        self.entrenador_cedula = entrenador_cedula
        self.horario = horario

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Servicio(data["codigo"], data["nombre"], data["cupo_max"], data["entrenador_cedula"], data["horario"])