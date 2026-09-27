class Cliente:
    def _init_(self, cedula, nombres, apellidos, direccion, celular, fijo, estado, riesgo):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.celular = celular
        self.fijo = fijo
        self.estado = estado  # En proceso de inscripcion, Inscrito, Activo, Inactivo
        self.riesgo = riesgo  # alto, medio, bajo

    def _str_(self):
        return f"{self.cedula} - {self.nombres} {self.apellidos} | {self.estado} | Riesgo: {self.riesgo}"

clientes = []

def registrar_cliente(cedula, nombres, apellidos, direccion, celular, fijo, estado, riesgo):
    for c in clientes:
        if c.cedula == cedula:
            return "ERROR: Esa cedula ya existe"
    nuevo = Cliente(cedula, nombres, apellidos, direccion, celular, fijo, estado, riesgo)
    clientes.append(nuevo)
    return "Cliente registrado OK"

def listar_clientes():
    if not clientes:
        print("No hay clientes")
    for c in clientes:
        print(c)