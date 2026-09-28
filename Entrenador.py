class Entrenador:
    def __init__(self, cedula, nombre, especialidad, email):
        self.cedula = cedula
        self.nombre = nombre
        self.especialidad = especialidad
        self.email = email

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Entrenador(data["cedula"], data["nombre"], data["especialidad"], data["email"])