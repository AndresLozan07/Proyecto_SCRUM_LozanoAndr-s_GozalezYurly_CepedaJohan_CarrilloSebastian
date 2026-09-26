from datetime import date


class Matricula:
    def __init__(self, cliente, servicio, instructor, duracion_dias):
        self.cliente = cliente
        self.servicio = servicio
        self.instructor = instructor
        self.fecha_inicio = date.today()
        self.duracion = duracion_dias
