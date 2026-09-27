from servicio import servicios
from matricula import matriculas
def reporte_clientes_por_servicio():
    for s in servicios:
        count = sum(1 for m in matriculas if m["servicio"] == s)
        print(f"{s}: {count}")
def reporte_cupos_disponibles():
    for n, d in servicios.items():
        print(f"{n}: {d['capacidad'] - d['inscritos']} libres")
def reporte_matriculas_por_fecha():
    for m in matriculas: print(f"{m['fecha']} - {m['cedula']} - {m['servicio']}")