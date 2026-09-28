def validar_nombre(nombre):
    if len(nombre.strip()) > 0:
        return True
    else:
        return False


def validar_estado(estado):
    estados = [
        "En proceso de inscripcion",
        "Inscrito",
        "Activo",
        "Inactivo"
    ]

    if estado in estados:
        return True
    else:
        return False


def validar_riesgo(riesgo):
    riesgos = ["alto", "medio", "bajo"]

    if riesgo.lower() in riesgos:
        return True
    else:
        return False


def validar_capacidad(capacidad):
    if capacidad > 0:
        return True
    else:
        return False