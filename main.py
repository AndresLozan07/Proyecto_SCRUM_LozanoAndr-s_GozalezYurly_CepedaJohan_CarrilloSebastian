from funciones import *


while True:

    print("\n================================")
    print("       GIMNASIO FORCE TECH")
    print("================================")

    print("1. Iniciar sesión")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        cuenta = iniciar_sesion()

        if cuenta is not None:

            if cuenta["rol"] == "Cliente":

                menu_cliente(cuenta)

            elif cuenta["rol"] == "Entrenador":

                menu_entrenador(cuenta)

            elif cuenta["rol"] == "Administrador":

                menu_administrador(cuenta)

    elif opcion == "2":

        print("Gracias por utilizar ForceTech.")
        break

    else:

        print("Opción no válida.")