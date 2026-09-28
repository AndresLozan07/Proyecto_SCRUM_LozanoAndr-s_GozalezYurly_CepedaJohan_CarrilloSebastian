from enum import Enum

class Rol(Enum):
    ADMINISTRADOR = "ADMINISTRADOR"
    ENTRENADOR = "ENTRENADOR"
    CLIENTE = "CLIENTE"

class Usuario:
    def __init__(self, username, password, rol):
        self.username = username
        self.password = password
        self.rol = rol if isinstance(rol, Rol) else Rol(rol)

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "rol": self.rol.value
        }

    @staticmethod
    def from_dict(data):
        return Usuario(data["username"], data["password"], Rol(data["rol"]))

# Usuarios por defecto según la configuración del proyecto
usuarios_sistema = [
    Usuario("admin", "admin123", Rol.ADMINISTRADOR),
    Usuario("carlos", "123", Rol.ENTRENADOR),
    Usuario("juan", "123", Rol.CLIENTE)
]

usuario_actual = None

def login():
    global usuario_actual
    print("\n=== INICIO DE SESIÓN ===")
    usr = input("Usuario: ").strip()
    pwd = input("Contraseña: ").strip()
    
    for u in usuarios_sistema:
        if u.username == usr and u.password == pwd:
            usuario_actual = u
            print(f"✅ Bienvenido, {u.username} ({u.rol.value})")
            return True
            
    print("❌ Credenciales incorrectas")
    return False

def permiso(*roles_permitidos):
    if usuario_actual and usuario_actual.rol in roles_permitidos:
        return True
    return False