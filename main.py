from storage import clientes, entrenadores, servicios, matriculas, guardar, cargar, usuarios_sistema
from cliente import Cliente
from entrenador import Entrenador
from servicio import Servicio
from matricula import Matricula
from usuarios import login, permiso, Rol, Usuario, usuario_actual, usuarios_sistema as users

def registrar_cliente():
    if not permiso(Rol.ADMINISTRADOR, Rol.ENTRENADOR): print("❌ Solo ADMIN y ENTRENADOR"); return
    cedula = input("Cédula: ").strip(); nombre = input("Nombre: ").strip(); email = input("Email: ").strip(); edad = input("Edad: ").strip(); tel = input("Tel 10 digitos: ").strip()
    if not cedula or not nombre or not email or not edad or not tel: print("❌ Todos obligatorios"); return
    if not cedula.isdigit() or any(c.cedula == cedula for c in clientes): print("❌ Cédula inválida o repetida"); return
    if len(nombre)<3 or "@" not in email: print("❌ Nombre o Email inválido"); return
    if not edad.isdigit() or int(edad)<14: print("❌ Edad mínima 14"); return
    clientes.append(Cliente(cedula,nombre,email,int(edad),tel))
    users.append(Usuario(cedula,cedula,Rol.CLIENTE)); guardar(); print(f"✅ Cliente creado Usuario:{cedula} Pass:{cedula}")

def registrar_entrenador():
    if not permiso(Rol.ADMINISTRADOR): print("❌ Solo ADMIN"); return
    ced=input("Cédula: "); nom=input("Nombre: "); esp=input("Especialidad Yoga/Pilates/Crossfit: "); email=input("Email: ")
    if not ced or not nom or not esp: print("❌ Obligatorios"); return
    if any(e.cedula==ced for e in entrenadores): print("❌ Cédula repetida"); return
    entrenadores.append(Entrenador(ced,nom,esp,email)); users.append(Usuario(nom.lower(),"123",Rol.ENTRENADOR)); guardar(); print("✅ Entrenador creado")

def crear_servicio():
    if not permiso(Rol.ADMINISTRADOR): print("❌ Solo ADMIN"); return
    cod=input("Código: "); nom=input("Nombre: "); cupo=input("Cupo 1-50: "); ced_ent=input("Cédula entrenador: "); hor=input("Horario: ")
    if not cod or not nom or not cupo: print("❌ Obligatorios"); return
    if any(s.codigo==cod for s in servicios): print("❌ Código ya existe"); return
    if not cupo.isdigit() or not (1<=int(cupo)<=50): print("❌ Cupo 1-50"); return
    servicios.append(Servicio(cod,nom,int(cupo),ced_ent,hor)); guardar(); print("✅ Servicio creado")

def matricular():
    ced = users[0].username if False else (usuario_actual.username if permiso(Rol.CLIENTE) and usuario_actual.username.isdigit() else input("Cédula cliente: ").strip())
    cod = input("Código servicio: ").strip()
    if not any(c.cedula==ced for c in clientes): print("❌ Cliente no existe"); return
    serv = next((s for s in servicios if s.codigo==cod), None)
    if not serv: print("❌ Servicio no existe"); return
    if any(m.cedula_cliente==ced and m.codigo_servicio==cod for m in matriculas): print("❌ Ya matriculado"); return
    if sum(1 for m in matriculas if m.codigo_servicio==cod) >= serv.cupo_max: print("❌ Servicio lleno"); return
    matriculas.append(Matricula(ced,cod)); guardar(); print("✅ Matriculado")

def reportes():
    if permiso(Rol.ADMINISTRADOR):
        for s in servicios:
            oc=sum(1 for m in matriculas if m.codigo_servicio==s.codigo)
            print(f"{s.codigo} {s.nombre}: {oc}/{s.cupo_max} Disp:{s.cupo_max-oc}")
    elif permiso(Rol.ENTRENADOR):
        for s in servicios:
            oc=sum(1 for m in matriculas if m.codigo_servicio==s.codigo)
            print(f"{s.nombre}: {oc} clientes Libres:{s.cupo_max-oc}")
    else: print("❌ Clientes no ven reportes")

def main():
    cargar()
    if not login(): return
    while True:
        print(f"\n--- FORTECH {usuario_actual.rol.value} ---")
        op=input("1.Reg Cliente 2.Crear Serv 3.Reg Entrenador 4.Matricular 5.Listar Serv 6.Reportes 0.Salir: ")
        if op=="0": guardar(); break
        if op=="1": registrar_cliente()
        if op=="2": crear_servicio()
        if op=="3": registrar_entrenador()
        if op=="4": matricular()
        if op=="5":
            for s in servicios:
                oc=sum(1 for m in matriculas if m.codigo_servicio==s.codigo)
                print(f"{s.codigo} {s.nombre} {oc}/{s.cupo_max}")
        if op=="6": reportes()

if __name__ == "__main__":
    main()