from servicio import servicios
from Matricula import matriculas
from Cliente import clientes

class Reporte:
    def generar(self):
        pass

def reporte_clientes_por_servicio():
    for s in servicios:
        c = sum(1 for m in matriculas if m.servicio == s)
        print(f"{s}: {c}")

def reporte_cupos_disponibles():
    for n,d in servicios.items():
        print(f"{n}: {d['capacidad'] - d['inscritos']} libres")

def reporte_matriculas_por_fecha():
    for m in matriculas:
        print(m)