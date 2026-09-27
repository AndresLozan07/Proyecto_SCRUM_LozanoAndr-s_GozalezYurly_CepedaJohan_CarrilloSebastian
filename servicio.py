class Servicio:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.inscritos = 0

    def __str__(self):
        return f"{self.nombre} - Cupo: {self.capacidad} - Inscritos: {self.inscritos}"

# Esto lo necesita matricula.py
servicios = {
    "yoga": {"capacidad": 10, "inscritos": 0},
    "pilates": {"capacidad": 15, "inscritos": 0},
    "personalizado": {"capacidad": 5, "inscritos": 0},
    "piscina": {"capacidad": 20, "inscritos": 0},
    "general": {"capacidad": 30, "inscritos": 0}
}

lista_servicios = [Servicio("yoga",10), Servicio("pilates",15), Servicio("personalizado",5), Servicio("piscina",20), Servicio("general",30)]

def mostrar_servicios():
    for s in lista_servicios:
        print(s)