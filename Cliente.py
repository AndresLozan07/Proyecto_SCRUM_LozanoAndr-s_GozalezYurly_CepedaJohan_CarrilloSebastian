class Cliente:
    def __init__(self, cedula, nombres, apellidos, direccion, celular, fijo, estado, riesgo):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.celular = celular
        self.fijo = fijo
        self.estado = estado
        self.riesgo = riesgo

    def __str__(self):
        return f"{self.cedula} - {self.nombres} {self.apellidos} - {self.celular}"

clientes = []

def registrar_cliente():
    cedula = input("Cedula: ")
    for c in clientes:
        if c.cedula == cedula:
            print("Error: Cedula ya existe")
            return
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    direccion = input("Direccion: ")
    celular = input("Celular: ")
    fijo = input("Fijo: ")
    estado = input("Estado: ")
    riesgo = input("Riesgo: ")
    clientes.append(Cliente(cedula, nombres, apellidos, direccion, celular, fijo, estado, riesgo))
    print("Cliente OK")

def listar_clientes():
    for c in clientes:
        print(c)