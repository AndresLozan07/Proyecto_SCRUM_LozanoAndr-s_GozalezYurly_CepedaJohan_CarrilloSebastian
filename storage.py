import json, os
from cliente import Cliente
from entrenador import Entrenador
from servicio import Servicio
from matricula import Matricula
from usuarios import usuarios_sistema, Rol, Usuario

clientes, entrenadores, servicios, matriculas = [], [], [], []

def guardar():
    json.dump([c.to_dict() for c in clientes], open("clientes.json","w"), indent=4)
    json.dump([e.to_dict() for e in entrenadores], open("entrenadores.json","w"), indent=4)
    json.dump([s.to_dict() for s in servicios], open("servicios.json","w"), indent=4)
    json.dump([m.to_dict() for m in matriculas], open("matriculas.json","w"), indent=4)
    json.dump([{"username":u.username,"password":u.password,"rol":u.rol.value} for u in usuarios_sistema], open("usuarios.json","w"), indent=4)

def cargar():
    global clientes, entrenadores, servicios, matriculas, usuarios_sistema
    if os.path.exists("clientes.json"): clientes = [Cliente.from_dict(d) for d in json.load(open("clientes.json"))]
    if os.path.exists("entrenadores.json"): entrenadores = [Entrenador.from_dict(d) for d in json.load(open("entrenadores.json"))]
    if os.path.exists("servicios.json"): servicios = [Servicio.from_dict(d) for d in json.load(open("servicios.json"))]
    if os.path.exists("matriculas.json"): matriculas = [Matricula.from_dict(d) for d in json.load(open("matriculas.json"))]
    if os.path.exists("usuarios.json"):
        usuarios_sistema[:] = [Usuario(d["username"], d["password"], Rol(d["rol"])) for d in json.load(open("usuarios.json"))]