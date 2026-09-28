from enum import Enum

class Rol(Enum):
    ADMINISTRADOR = "ADMINISTRADOR"
    ENTRENADOR = "ENTRENADOR"
    CLIENTE = "CLIENTE"

class Usuario:
    def __init__(self, username, password, rol):
        self.username = username
        self.password = password
        self.rol = rol

usuarios_sistema = [
    Usuario("admin", "admin123", Rol.ADMINISTRADOR),
    Usuario("carlos", "123", Rol.ENTRENADOR),
    Usuario("juan", "123", Rol.CLIENTE)
]

usuario_actual = None

def login():
    global usuario_actual
    print("\n🔐 LOGIN FORTECH")
    u = input("Usuario: ").strip()
    p = input("Contraseña: ").strip()
    for user in usuarios_sistema:
        if user.username == u and user.password == p:
            usuario_actual = user
            print(f"✅ Bienvenido {user.username} [{user.rol.value}]")
            return True
    print("❌ Credenciales incorrectas")
    return False

def permiso(*roles):
    return usuario_actual and usuario_actual.rol in roles