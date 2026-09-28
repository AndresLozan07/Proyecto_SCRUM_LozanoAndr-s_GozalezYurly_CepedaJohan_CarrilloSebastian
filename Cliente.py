class Cliente:
    def __init__(self, identificacion, nombres, apellidos, direccion, celular, fijo, estado, riesgo):
        self.identificacion = identificacion
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.celular = celular
        self.fijo = fijo
        self.estado = estado # En proceso de inscripción, Inscrito, Activo, Inactivo
        self.riesgo = riesgo # alto, medio, bajo
        self.progreso = {} # {codigo_servicio: "asistencia / rendimiento"}

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(d):
        c = Cliente(d["identificacion"], d["nombres"], d["apellidos"], d["direccion"], d["celular"], d["fijo"], d["estado"], d["riesgo"])
        c.progreso = d.get("progreso", {})
        return c