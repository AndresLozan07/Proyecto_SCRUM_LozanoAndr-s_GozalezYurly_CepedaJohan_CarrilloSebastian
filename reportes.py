from storage import servicios, matriculas, clientes

class Reporte:
    def generar(self):
        pass

def reporte_clientes_por_servicio():
    for s in servicios:
        c = sum(1 for m in matriculas if m.codigo_servicio == s.codigo)
        print(f"Servicio: {s.nombre} | Matriculados: {c}")

def reporte_cupos_disponibles():
    for s in servicios:
        inscritos = sum(1 for m in matriculas if m.codigo_servicio == s.codigo)
        libres = s.cupo_max - inscritos
        print(f"Servicio: {s.nombre} | Libres: {libres}")

def reporte_matriculas_por_fecha():
    for m in matriculas:
        print(f"Cliente Cédula: {m.cedula_cliente} | Código Servicio: {m.codigo_servicio}")