from Cliente import registrar_cliente, listar_clientes
from Entrenadores import registrar_entrenador
from servicio import mostrar_servicios
from Matricula import matricular
from reportes import *

while True:
    print("\n1.Registrar cliente (Sebastian)\n2.Listar (Sebastian)\n3.Ver servicios (Yurly)\n4.Reg Entrenador (Johan)\n5.Matricular (Johan)\n6.Reportes (Andres)\n7.Salir")
    op = input("Opcion: ")
    if op == "1": registrar_cliente()
    elif op == "2": listar_clientes()
    elif op == "3": mostrar_servicios()
    elif op == "4":
        nombre = input("Nombre del instructor: ")
        especialidad = input("Especialidad: ")
        print(registrar_entrenador(nombre, especialidad))
    elif op == "5":
        cedula = input("Cedula del cliente: ")
        nombre_servicio = input("Servicio: ")
        duracion = input("Duracion: ")
        nombre_instructor = input("Instructor: ")
        print(matricular(cedula, nombre_servicio, duracion, nombre_instructor))
    elif op == "6":
        reporte_clientes_por_servicio()
        reporte_cupos_disponibles()
        reporte_matriculas_por_fecha()
    elif op == "7": break