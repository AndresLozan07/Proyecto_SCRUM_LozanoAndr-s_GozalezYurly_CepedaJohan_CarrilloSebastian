from storage import clientes, entrenadores, servicios, matriculas, guardar, cargar
from Cliente import Cliente
from Entrenador import Entrenador
from servicio import Servicio
from Matricula import Matricula
from usuarios import login, permiso, Rol, Usuario, usuario_actual, usuarios_sistema as users

def registrar_cliente():
    if not permiso(Rol.ADMINISTRADOR, Rol.ENTRENADOR): 
        print("❌ Solo ADMIN y ENTRENADOR pueden registrar clientes")
        return
    cedula = input("Cédula: ").strip()
    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip()
    edad = input("Edad: ").strip()
    tel = input("Teléfono (10 dígitos): ").strip()
    
    if not cedula or not nombre or not email or not edad or not tel:
        print("❌ Todos los campos son obligatorios")
        return
    if not cedula.isdigit() or any(c.cedula == cedula for c in clientes):
        print("❌ Cédula inválida o repetida")
        return
    if len(nombre) < 3 or "@" not in email:
        print("❌ Nombre o Email inválido")
        return
    if not edad.isdigit() or int(edad) < 14:
        print("❌ Edad mínima 14 años")
        return
        
    clientes.append(Cliente(cedula, nombre, email, int(edad), tel))
    users.append(Usuario(cedula, cedula, Rol.CLIENTE))
    guardar()
    print(f"✅ Cliente creado. Usuario: {cedula} | Pass: {cedula}")

def registrar_entrenador():
    if not permiso(Rol.ADMINISTRADOR): 
        print("❌ Solo ADMIN")
        return
    ced = input("Cédula: ").strip()
    nom = input("Nombre: ").strip()
    esp = input("Especialidad (Yoga/Pilates/Crossfit): ").strip()
    email = input("Email: ").strip()
    
    if not ced or not nom or not esp:
        print("❌ Campos obligatorios")
        return
    if any(e.cedula == ced for e in entrenadores):
        print("❌ Cédula repetida")
        return
        
    entrenadores.append(Entrenador(ced, nom, esp, email))
    users.append(Usuario(nom.lower(), "123", Rol.ENTRENADOR))
    guardar()
    print(f"✅ Entrenador creado. Usuario: {nom.lower()} | Pass: 123")

def crear_servicio():
    if not permiso(Rol.ADMINISTRADOR): 
        print("❌ Solo ADMIN")
        return
    cod = input("Código: ").strip()
    nom = input("Nombre: ").strip()
    cupo = input("Cupo (1-50): ").strip()
    ced_ent = input("Cédula entrenador: ").strip()
    hor = input("Horario: ").strip()
    
    if not cod or not nom or not cupo:
        print("❌ Campos obligatorios")
        return
    if any(s.codigo == cod for s in servicios):
        print("❌ El código ya existe")
        return
    if not cupo.isdigit() or not (1 <= int(cupo) <= 50):
        print("❌ Cupo debe ser de 1 a 50")
        return
        
    servicios.append(Servicio(cod, nom, int(cupo), ced_ent, hor))
    guardar()
    print("✅ Servicio creado exitosamente")

def matricular():
    if permiso(Rol.CLIENTE) and usuario_actual.username.isdigit():
        ced = usuario_actual.username
    else:
        ced = input("Cédula cliente: ").strip()
        
    cod = input("Código servicio: ").strip()
    
    if not any(c.cedula == ced for c in clientes):
        print("❌ El cliente no existe")
        return
    serv = next((s for s in servicios if s.codigo == cod), None)
    if not serv:
        print("❌ El servicio no existe")
        return
    if any(m.cedula_cliente == ced and m.codigo_servicio == cod for m in matriculas):
        print("❌ Ya está matriculado en este servicio")
        return
    if sum(1 for m in matriculas if m.codigo_servicio == cod) >= serv.cupo_max:
        print("❌ Servicio sin cupos disponibles")
        return
        
    matriculas.append(Matricula(ced, cod))
    guardar()
    print("✅ Matriculado exitosamente")

def reportes():
    if permiso(Rol.ADMINISTRADOR):
        print("\n--- REPORTES ADMINISTRADOR ---")
        for s in servicios:
            oc = sum(1 for m in matriculas if m.codigo_servicio == s.codigo)
            print(f"{s.codigo} {s.nombre}: {oc}/{s.cupo_max} Disponibles: {s.cupo_max - oc}")
    elif permiso(Rol.ENTRENADOR):
        print("\n--- REPORTES ENTRENADOR ---")
        for s in servicios:
            oc = sum(1 for m in matriculas if m.codigo_servicio == s.codigo)
            print(f"{s.nombre}: {oc} clientes Libres: {s.cupo_max - oc}")
    else:
        print("❌ Los clientes no tienen permiso para ver reportes")

def main():
    cargar()
    if not login(): 
        return
    while True:
        print(f"\n--- FORTECH ({usuario_actual.rol.value}) ---")
        op = input("1. Reg Cliente | 2. Crear Serv | 3. Reg Entrenador | 4. Matricular | 5. Listar Serv | 6. Reportes | 0. Salir: ").strip()
        if op == "0":
            guardar()
            print("👋 Sesión finalizada y datos guardados.")
            break
        elif op == "1":
            registrar_cliente()
        elif op == "2":
            crear_servicio()
        elif op == "3":
            registrar_entrenador()
        elif op == "4":
            matricular()
        elif op == "5":
            print("\n--- LISTA DE SERVICIOS ---")
            for s in servicios:
                oc = sum(1 for m in matriculas if m.codigo_servicio == s.codigo)
                print(f"{s.codigo} - {s.nombre} ({oc}/{s.cupo_max})")
        elif op == "6":
            reportes()

if __name__ == "__main__":
    main()