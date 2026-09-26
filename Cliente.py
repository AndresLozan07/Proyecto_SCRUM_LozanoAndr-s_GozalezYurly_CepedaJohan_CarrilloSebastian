# Lista donde se guardan todos los clientes
clientes_guardados = []


class Cliente:
    def __init__(self, cedula, nombre, apellido, direccion, celular):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.celular = celular
        self.estado = "Inscrito"  # Puede ser: En proceso, Inscrito, Activo, Inactivo


# Función para agregar un cliente
def agregar_cliente(cedula, nombre, apellido, direccion, celular):
    # Revisa si ya existe
    for c in clientes_guardados:
        if c.cedula == cedula:
            print("Esa cédula ya existe")
            return

    nuevo = Cliente(cedula, nombre, apellido, direccion, celular)
    clientes_guardados.append(nuevo)

    print(f"Cliente {nombre} agregado bien")
