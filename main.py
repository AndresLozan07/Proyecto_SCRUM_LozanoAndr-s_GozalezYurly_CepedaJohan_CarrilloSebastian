from Cliente import registrar_cliente, listar_clientes
from Entrenadores import registrar_entrenador, listar_entrenadores
from servicio import mostrar_servicios
from Matricula import matricular
from reportes import reporte_clientes_por_servicio, reporte_cupos_disponibles, reporte_matriculas_por_fecha
import os

NOMBRE_GYM = "GIMNASIO FORCETECH"

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("="*60)
    print(f" 🏋️ {NOMBRE_GYM} - SISTEMA DE GESTION 🏋️ ".center(60))
    print("="*60)
    print(" ¡BIENVENIDOS A FORCETECH! ".center(60))
    print(" Donde tu fuerza se convierte en tecnologia ".center(60))
    print()

def menu():
    banner()
    print("┌──────────────────────────────────────────┐")
    print("│ MENU PRINCIPAL FORCETECH │")
    print("├──────────────────────────────────────────┤")
    print("│ 1. 📝 Registrar Cliente [Sebastian] │")
    print("│ 2. 📋 Listar Clientes [Sebastian] │")
    print("│ 3. 🏋️ Ver Servicios ForceTech [Yurly] │")
    print("│ 4. 👨‍🏫 Registrar Entrenador [Johan] │")
    print("│ 5. 📅 Matricular Cliente [Johan] │")
    print("│ 6. 📊 Reportes ForceTech [Andres] │")
    print("│ 7. 🚪 Salir │")
    print("└──────────────────────────────────────────┘")

while True:
    limpiar()
    menu()
    op = input("\n👉 Selecciona una opcion (1-7): ")

    if op == "1":
        print(f"\n--- REGISTRO CLIENTE - {NOMBRE_GYM} ---")
        registrar_cliente()
    elif op == "2":
        print(f"\n--- CLIENTES {NOMBRE_GYM} ---")
        listar_clientes()
    elif op == "3":
        print(f"\n--- SERVICIOS {NOMBRE_GYM} ---")
        print(" Yoga | Pilates | Personalizado | Piscina | General ")
        mostrar_servicios()
    elif op == "4":
        print(f"\n--- INSTRUCTORES {NOMBRE_GYM} ---")
        registrar_entrenador()
    elif op == "5":
        print(f"\n--- MATRICULAS {NOMBRE_GYM} ---")
        matricular()
    elif op == "6":
        print(f"\n{'='*10} REPORTES {NOMBRE_GYM} {'='*10}")
        reporte_clientes_por_servicio()
        print("-"*60)
        reporte_cupos_disponibles()
        print("-"*60)
        reporte_matriculas_por_fecha()
    elif op == "7":
        limpiar()
        print(f"\n¡Gracias por usar {NOMBRE_GYM}!")
        print("¡Vuelve pronto, tu progreso nos importa! 💪🔥")
        break
    else:
        print("❌ Opcion no valida")

    input("\nPresiona ENTER para continuar...")