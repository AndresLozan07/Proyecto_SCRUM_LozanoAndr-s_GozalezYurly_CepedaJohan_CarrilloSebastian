from datetime import date
from servicio import servicios
from Cliente import clientes

class Matricula:
    def __init__(self, cedula, servicio, duracion, instructor):
        self.cedula = cedula
        self.servicio = servicio
        self.fecha = str(date.today())
        self.duracion = duracion
        self.instructor = instructor

    def __str__(self):
        return f"{self.fecha} - {self.cedula} - {self.servicio} - {self.instructor}"

matriculas = []

def matricular():
    cedula = input("Cedula cliente: ")
    if not any(c.cedula == cedula for c in clientes):
        print("Cliente no existe"); return
    serv = input("Servicio (yoga/pilates/personalizado/piscina/general): ").lower()
    if serv not in servicios:
        print("Servicio no existe"); return
    if servicios[serv]["inscritos"] >= servicios[serv]["capacidad"]:
        print(f"Cupo lleno {serv} max {servicios[serv]['capacidad']}")
        return
    duracion = input("Duracion: ")
    instructor = input("Instructor: ")
    matriculas.append(Matricula(cedula, serv, duracion, instructor))
    servicios[serv]["inscritos"] += 1
    print("Matricula OK")