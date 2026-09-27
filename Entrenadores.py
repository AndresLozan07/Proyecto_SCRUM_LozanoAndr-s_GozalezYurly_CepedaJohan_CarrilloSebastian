class Instructor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.estado = "activo"
        self.clientes_asignados = []

    def __str__(self):
        return f"Instructor: {self.nombre} - {self.especialidad} - {self.estado}"

instructores = []
instructores.append(Instructor("Carlos", "yoga"))
instructores.append(Instructor("Laura", "pilates"))
instructores.append(Instructor("Andres", "entrenamiento personalizado"))

def registrar_entrenador(nombre, especialidad):
    for i in instructores:
        if i.nombre.lower() == nombre.lower():
            return "ERROR: Ese instructor ya existe"
    nuevo = Instructor(nombre, especialidad)
    instructores.append(nuevo)
    return "Instructor registrado OK"