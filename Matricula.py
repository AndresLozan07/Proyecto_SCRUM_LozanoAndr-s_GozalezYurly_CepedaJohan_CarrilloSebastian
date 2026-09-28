class Matricula:
    def __init__(self, cedula_cliente, codigo_servicio):
        self.cedula_cliente = cedula_cliente
        self.codigo_servicio = codigo_servicio

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Matricula(data["cedula_cliente"], data["codigo_servicio"])