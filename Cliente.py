class Cliente:
    def __init__(self, cedula, nombre, email, edad, telefono):
        self.cedula = cedula
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.telefono = telefono

    def to_dict(self):
        return {
            "cedula": self.cedula,
            "nombre": self.nombre,
            "email": self.email,
            "edad": self.edad,
            "telefono": self.telefono
        }

    @staticmethod
    def from_dict(data):
        return Cliente(data["cedula"], data["nombre"], data["email"], data["edad"], data["telefono"])