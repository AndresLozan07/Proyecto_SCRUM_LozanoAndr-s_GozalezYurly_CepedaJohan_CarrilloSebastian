from Cliente import clientes
from servicio import servicios
from Entrenadores import instructores
from datetime import date

matriculas = []


def matricular(cedula, nombre_servicio, duracion, nombre_instructor):
    cliente = next((c for c in clientes if c.cedula == cedula), None)
    if not cliente:
        return "ERROR: Cliente no existe"

    servicio = next((s for s in servicios if s.nombre == nombre_servicio), None)
    if not servicio:
        return "ERROR: Servicio no existe"

    instructor = next(
        (i for i in instructores if i.nombre.lower() == nombre_instructor.lower()),
        None
    )
    if not instructor:
        return "ERROR: Instructor no existe"

    # Validacion capacidad
    if len(servicio.clientes_matriculados) >= servicio.cupo_maximo:
        return "ERROR: El servicio ya esta lleno - capacidad maxima alcanzada"

    servicio.clientes_matriculados.append(cliente)
    instructor.clientes_asignados.append(cliente)

    matricula = {
        "cliente": cliente,
        "servicio": servicio,
        "instructor": instructor,
        "fecha_inicio": str(date.today()),
        "duracion": duracion
    }

    matriculas.append(matricula)

    return (
        f"Matriculado OK en {nombre_servicio} con "
        f"{instructor.nombre} desde {matricula['fecha_inicio']}"
    )