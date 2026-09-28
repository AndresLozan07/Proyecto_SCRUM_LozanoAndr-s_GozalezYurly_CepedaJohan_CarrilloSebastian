import json

def cargar_datos():

    try:
        with open("datos.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

    except (FileNotFoundError, json.JSONDecodeError):

        datos = {
            "usuarios": [],
            "clientes": [],
            "entrenadores": [],
            "servicios": [],
            "matriculas": [],
            "evaluaciones": [],
            "actividades": []
        }

    return datos

def guardar_datos(datos):

    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def iniciar_sesion():

    datos = cargar_datos()

    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    for cuenta in datos["usuarios"]:

        if cuenta["usuario"] == usuario and cuenta["contrasena"] == contrasena:

            print("\nInicio de sesión correcto.")
            print("Rol:", cuenta["rol"])

            return cuenta

    print("\nUsuario o contraseña incorrectos.")

    return None

def registrar_cliente():

    datos = cargar_datos()

    print("\n===== REGISTRAR CLIENTE =====")

    identificacion = input("Número de identificación: ")

    # Verificar si ya existe la identificación
    for cliente in datos["clientes"]:

        if cliente["identificacion"] == identificacion:
            print("Ya existe un cliente con esa identificación.")
            return

    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    direccion = input("Dirección: ")
    celular = input("Número de celular: ")
    telefono_fijo = input("Número fijo: ")

    print("\nEstados:")
    print("1. En proceso de inscripcion")
    print("2. Inscrito")
    print("3. Activo")
    print("4. Inactivo")

    opcion = input("Seleccione el estado: ")

    estados = {
        "1": "En proceso de inscripcion",
        "2": "Inscrito",
        "3": "Activo",
        "4": "Inactivo"
    }

    if opcion not in estados:
        print("Estado no válido.")
        return

    estado = estados[opcion]

    print("\nNivel de riesgo:")
    print("1. Alto")
    print("2. Medio")
    print("3. Bajo")

    opcion_riesgo = input("Seleccione el riesgo: ")

    riesgos = {
        "1": "alto",
        "2": "medio",
        "3": "bajo"
    }

    if opcion_riesgo not in riesgos:
        print("Riesgo no válido.")
        return

    riesgo = riesgos[opcion_riesgo]

    # Crear usuario y contraseña del cliente
    print("\n===== DATOS DE ACCESO DEL CLIENTE =====")

    usuario = input("Crear usuario para el cliente: ")
    contrasena = input("Crear contraseña para el cliente: ")

    # Verificar que el usuario no exista
    for cuenta in datos["usuarios"]:

        if cuenta["usuario"] == usuario:
            print("Ese usuario ya existe.")
            return

    # Crear cliente
    cliente = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "direccion": direccion,
        "celular": celular,
        "telefono_fijo": telefono_fijo,
        "estado": estado,
        "riesgo": riesgo
    }

    datos["clientes"].append(cliente)

    # Crear cuenta del cliente
    usuario_cliente = {
        "usuario": usuario,
        "contrasena": contrasena,
        "rol": "Cliente",
        "identificacion": identificacion
    }

    datos["usuarios"].append(usuario_cliente)

    guardar_datos(datos)

    print("\nCliente registrado correctamente.")
    print("Usuario creado:", usuario)

def registrar_entrenador():

    datos = cargar_datos()

    print("\n===== REGISTRAR ENTRENADOR =====")

    identificacion = input("Identificación: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")

    usuario = input("Crear usuario: ")
    contrasena = input("Crear contraseña: ")

    for cuenta in datos["usuarios"]:

        if cuenta["usuario"] == usuario:
            print("Ese usuario ya existe.")
            return

    entrenador = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "estado": "Activo",
        "usuario": usuario
    }

    datos["entrenadores"].append(entrenador)

    cuenta = {
        "usuario": usuario,
        "contrasena": contrasena,
        "rol": "Entrenador",
        "identificacion": identificacion
    }

    datos["usuarios"].append(cuenta)

    guardar_datos(datos)

    print("\nEntrenador registrado correctamente.")

def registrar_servicio():

    datos = cargar_datos()

    print("\n===== REGISTRAR SERVICIO =====")

    print("1. Clases de yoga")
    print("2. Clases de pilates")
    print("3. Entrenamiento personalizado")
    print("4. Acceso a la piscina")
    print("5. Uso del gimnasio general")

    opcion = input("Seleccione el servicio: ")

    servicios = {
        "1": "Clases de yoga",
        "2": "Clases de pilates",
        "3": "Entrenamiento personalizado",
        "4": "Acceso a la piscina",
        "5": "Uso del gimnasio general"
    }

    if opcion not in servicios:
        print("Servicio no válido.")
        return

    nombre = servicios[opcion]

    capacidad = int(input("Capacidad máxima: "))

    if capacidad <= 0:
        print("La capacidad debe ser mayor que 0.")
        return

    servicio = {
        "nombre": nombre,
        "capacidad": capacidad,
        "clientes_actuales": 0
    }

    datos["servicios"].append(servicio)

    guardar_datos(datos)

    print("\nServicio registrado correctamente.") 

def matricular_cliente():

    datos = cargar_datos()

    if len(datos["clientes"]) == 0:
        print("No hay clientes registrados.")
        return

    if len(datos["servicios"]) == 0:
        print("No hay servicios registrados.")
        return

    print("\n===== CLIENTES =====")

    for i, cliente in enumerate(datos["clientes"], 1):

        print(
            i,
            "-",
            cliente["identificacion"],
            cliente["nombres"],
            cliente["apellidos"]
        )

    try:
        opcion_cliente = int(input("Seleccione el cliente: "))
    except ValueError:
        print("Debe ingresar un número.")
        return

    if opcion_cliente < 1 or opcion_cliente > len(datos["clientes"]):
        print("Cliente no válido.")
        return

    cliente = datos["clientes"][opcion_cliente - 1]

    print("\n===== SERVICIOS =====")

    for i, servicio in enumerate(datos["servicios"], 1):

        print(
            i,
            "-",
            servicio["nombre"],
            "| Capacidad:",
            servicio["capacidad"],
            "| Ocupados:",
            servicio["clientes_actuales"]
        )

    try:
        opcion_servicio = int(input("Seleccione el servicio: "))
    except ValueError:
        print("Debe ingresar un número.")
        return

    if opcion_servicio < 1 or opcion_servicio > len(datos["servicios"]):
        print("Servicio no válido.")
        return

    servicio = datos["servicios"][opcion_servicio - 1]

    if servicio["clientes_actuales"] >= servicio["capacidad"]:

        print("\nNo hay cupos disponibles.")
        return

    fecha_inicio = input("Fecha de inicio: ")
    duracion = input("Duración: ")

    print("\nEntrenadores disponibles:")

    for i, entrenador in enumerate(datos["entrenadores"], 1):

        print(
            i,
            "-",
            entrenador["nombres"],
            entrenador["apellidos"]
        )

    if len(datos["entrenadores"]) > 0:

        try:
            opcion_entrenador = int(input("Seleccione entrenador: "))
        except ValueError:
            print("Debe ingresar un número.")
            return

        if opcion_entrenador < 1 or opcion_entrenador > len(datos["entrenadores"]):
            print("Entrenador no válido.")
            return

        entrenador = datos["entrenadores"][opcion_entrenador - 1]

        nombre_entrenador = (
            entrenador["nombres"] + " " +
            entrenador["apellidos"]
        )

    else:

        nombre_entrenador = "Sin entrenador"

    matricula = {
        "cliente": cliente["identificacion"],
        "servicio": servicio["nombre"],
        "fecha_inicio": fecha_inicio,
        "duracion": duracion,
        "instructor": nombre_entrenador
    }

    datos["matriculas"].append(matricula)

    servicio["clientes_actuales"] += 1

    guardar_datos(datos)

    print("\nMatrícula realizada correctamente.")

def ver_perfil_cliente(cuenta):

    datos = cargar_datos()

    identificacion = cuenta["identificacion"]

    for cliente in datos["clientes"]:

        if cliente["identificacion"] == identificacion:

            print("\n===== MI PERFIL =====")

            print("Identificación:", cliente["identificacion"])
            print("Nombres:", cliente["nombres"])
            print("Apellidos:", cliente["apellidos"])
            print("Dirección:", cliente["direccion"])
            print("Celular:", cliente["celular"])
            print("Teléfono fijo:", cliente["telefono_fijo"])
            print("Estado:", cliente["estado"])
            print("Nivel de riesgo:", cliente["riesgo"])

            return

    print("No se encontró el perfil.")

def ver_servicios_cliente(cuenta):

    datos = cargar_datos()

    identificacion = cuenta["identificacion"]

    print("\n===== MIS SERVICIOS =====")

    encontrado = False

    for matricula in datos["matriculas"]:

        if matricula["cliente"] == identificacion:

            encontrado = True

            print("\nServicio:", matricula["servicio"])
            print("Fecha de inicio:", matricula["fecha_inicio"])
            print("Duración:", matricula["duracion"])
            print("Entrenador:", matricula["instructor"])

    if not encontrado:
        print("No tiene servicios matriculados.")

def registrar_actividad(cuenta):

    datos = cargar_datos()

    actividad = input("Describa la actividad realizada: ")
    fecha = input("Fecha: ")

    nueva_actividad = {
        "cliente": cuenta["identificacion"],
        "fecha": fecha,
        "actividad": actividad
    }

    datos["actividades"].append(nueva_actividad)

    guardar_datos(datos)

    print("\nActividad registrada correctamente.")

def ver_progreso_cliente(cuenta):

    datos = cargar_datos()

    identificacion = cuenta["identificacion"]

    print("\n===== MI PROGRESO =====")

    # Mostrar asistencias
    print("\n--- ASISTENCIAS ---")

    encontro_asistencia = False

    for asistencia in datos["asistencias"]:

        if asistencia.get("cliente") == identificacion:

            encontro_asistencia = True

            print("Fecha:", asistencia.get("fecha", "No registrada"))
            print("Asistencia:", asistencia.get("asistencia", "No registrada"))

    if not encontro_asistencia:
        print("No tiene registros de asistencia.")


    # Mostrar evaluaciones
    print("\n--- EVALUACIONES ---")

    encontro_evaluacion = False

    for evaluacion in datos["evaluaciones"]:

        if evaluacion.get("cliente") == identificacion:

            encontro_evaluacion = True

            print("\nFecha:", evaluacion.get("fecha", "No registrada"))
            print("Servicio:", evaluacion.get("servicio", "No registrado"))
            print("Rendimiento:", evaluacion.get("rendimiento", "No registrado"))
            print("Condición física:", evaluacion.get("condicion_fisica", "No registrada"))

    if not encontro_evaluacion:
        print("No tiene registros de evaluación.")

def ver_clientes_entrenador(cuenta):

    datos = cargar_datos()

    nombre_entrenador = ""

    for entrenador in datos["entrenadores"]:

        if entrenador["identificacion"] == cuenta["identificacion"]:

            nombre_entrenador = (
                entrenador["nombres"] + " " +
                entrenador["apellidos"]
            )

    print("\n===== CLIENTES ASIGNADOS =====")

    encontrado = False

    for matricula in datos["matriculas"]:

        if matricula["instructor"] == nombre_entrenador:

            encontrado = True

            print("Cliente:", matricula["cliente"])
            print("Servicio:", matricula["servicio"])

    if not encontrado:
        print("No tiene clientes asignados.")

def registrar_asistencia(cuenta):

    datos = cargar_datos()

    identificacion = input("Identificación del cliente: ")
    fecha = input("Fecha: ")

    asistencia = input("¿Asistió? (Si/No): ")

    registro = {
        "cliente": identificacion,
        "fecha": fecha,
        "asistencia": asistencia
    }

    datos["asistencias"].append(registro)

    guardar_datos(datos)

    print("\nAsistencia registrada correctamente.")

def registrar_evaluacion(cuenta):

    datos = cargar_datos()

    identificacion = input("Identificación del cliente: ")
    servicio = input("Servicio: ")

    rendimiento = input("Rendimiento (bajo, medio, alto): ")
    condicion = input("Condición física: ")
    fecha = input("Fecha de evaluación: ")

    evaluacion = {
        "cliente": identificacion,
        "servicio": servicio,
        "fecha": fecha,
        "rendimiento": rendimiento,
        "condicion_fisica": condicion
    }

    datos["evaluaciones"].append(evaluacion)

    guardar_datos(datos)

    print("\nEvaluación registrada correctamente.")

def listar_clientes():

    datos = cargar_datos()

    print("\n===== CLIENTES =====")

    if len(datos["clientes"]) == 0:
        print("No hay clientes registrados.")
        return

    for cliente in datos["clientes"]:

        print("\nIdentificación:", cliente["identificacion"])
        print("Nombre:", cliente["nombres"], cliente["apellidos"])
        print("Estado:", cliente["estado"])
        print("Riesgo:", cliente["riesgo"])

def listar_servicios():

    datos = cargar_datos()

    print("\n===== SERVICIOS =====")

    for servicio in datos["servicios"]:

        print(
            servicio["nombre"],
            "| Capacidad:",
            servicio["capacidad"],
            "| Ocupados:",
            servicio["clientes_actuales"]
        )

def listar_entrenadores():

    datos = cargar_datos()

    print("\n===== ENTRENADORES ACTIVOS =====")

    for entrenador in datos["entrenadores"]:

        if entrenador["estado"] == "Activo":

            print(
                entrenador["identificacion"],
                "-",
                entrenador["nombres"],
                entrenador["apellidos"]
            )

def listar_clientes_riesgo():

    datos = cargar_datos()

    print("\n===== CLIENTES CON RIESGO ALTO =====")

    encontrado = False

    for cliente in datos["clientes"]:

        if cliente["riesgo"] == "alto":

            encontrado = True

            print(
                cliente["identificacion"],
                "-",
                cliente["nombres"],
                cliente["apellidos"]
            )

    if not encontrado:
        print("No hay clientes con riesgo alto.")

def listar_bajo_rendimiento():

    datos = cargar_datos()

    print("\n===== BAJO RENDIMIENTO =====")

    encontrado = False

    for evaluacion in datos["evaluaciones"]:

        if evaluacion.get("rendimiento", "").lower() == "bajo":

            encontrado = True

            print(
                "Cliente:",
                evaluacion["cliente"],
                "| Servicio:",
                evaluacion.get("servicio", "No especificado")
            )

    if not encontrado:
        print("No hay clientes con bajo rendimiento.")

def mostrar_progreso():

    datos = cargar_datos()

    print("\n===== PROGRESO DE CLIENTES =====")

    for evaluacion in datos["evaluaciones"]:

        print("\nCliente:", evaluacion["cliente"])

        if "servicio" in evaluacion:
            print("Servicio:", evaluacion["servicio"])

        if "asistencia" in evaluacion:
            print("Asistencia:", evaluacion["asistencia"])

        if "rendimiento" in evaluacion:
            print("Rendimiento:", evaluacion["rendimiento"])

        if "condicion_fisica" in evaluacion:
            print("Condición física:", evaluacion["condicion_fisica"])

def menu_cliente(cuenta):

    while True:

        print("\n==============================")
        print("        MENÚ CLIENTE")
        print("==============================")

        print("1. Ver mi perfil")
        print("2. Ver mis servicios")
        print("3. Registrar actividad")
        print("4. Ver mi progreso")
        print("5. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_perfil_cliente(cuenta)

        elif opcion == "2":
            ver_servicios_cliente(cuenta)

        elif opcion == "3":
            registrar_actividad(cuenta)

        elif opcion == "4":
            ver_progreso_cliente(cuenta)

        elif opcion == "5":
            print("Sesión cerrada.")
            break

        else:
            print("Opción no válida.")

def menu_entrenador(cuenta):

    while True:

        print("\n==============================")
        print("       MENÚ ENTRENADOR")
        print("==============================")

        print("1. Ver clientes asignados")
        print("2. Registrar asistencia")
        print("3. Registrar evaluación")
        print("4. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_clientes_entrenador(cuenta)

        elif opcion == "2":
            registrar_asistencia(cuenta)

        elif opcion == "3":
            registrar_evaluacion(cuenta)

        elif opcion == "4":
            print("Sesión cerrada.")
            break

        else:
            print("Opción no válida.")

def menu_administrador(cuenta):

    while True:

        print("\n==============================")
        print("     MENÚ ADMINISTRADOR")
        print("==============================")

        print("1. Registrar cliente")
        print("2. Registrar entrenador")
        print("3. Registrar servicio")
        print("4. Matricular cliente")
        print("5. Listar clientes")
        print("6. Listar servicios")
        print("7. Listar entrenadores")
        print("8. Clientes con riesgo alto")
        print("9. Clientes con bajo rendimiento")
        print("10. Mostrar progreso")
        print("11. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cliente()

        elif opcion == "2":
            registrar_entrenador()

        elif opcion == "3":
            registrar_servicio()

        elif opcion == "4":
            matricular_cliente()

        elif opcion == "5":
            listar_clientes()

        elif opcion == "6":
            listar_servicios()

        elif opcion == "7":
            listar_entrenadores()

        elif opcion == "8":
            listar_clientes_riesgo()

        elif opcion == "9":
            listar_bajo_rendimiento()

        elif opcion == "10":
            mostrar_progreso()

        elif opcion == "11":
            print("Sesión cerrada.")
            break

        else:
            print("Opción no válida.")



