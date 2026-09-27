from servicio import servicios
from Matricula import matriculas

def reporte_clientes_por_servicio():
    for s in servicios:
        count = sum(1 for m in matriculas if m["servicio"] == s)
        print(f"{s.nombre}: {count}")

def reporte_cupos_disponibles():
    for s in servicios:
        print(f"{s.nombre}: {s.cupo_disponible()} libres")

def reporte_matriculas_por_fecha():
    for m in matriculas:
        print(f"{m['fecha_inicio']} - {m['cliente'].cedula} - {m['servicio'].nombre}")