import json
import os
from Cliente import Cliente
from Entrenador import Entrenador
from servicio import Servicio
from Matricula import Matricula
from usuarios import Usuario, Rol, usuarios_sistema

clientes = []
entrenadores = []
servicios = []
matriculas = []

def cargar():
    global clientes, entrenadores, servicios, matriculas
    
    if os.path.exists("clientes.json"):
        with open("clientes.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            clientes.clear()
            clientes.extend([Cliente.from_dict(d) for d in data])
            
    if os.path.exists("entrenadores.json"):
        with open("entrenadores.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            entrenadores.clear()
            entrenadores.extend([Entrenador.from_dict(d) for d in data])
            
    if os.path.exists("servicios.json"):
        with open("servicios.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            servicios.clear()
            servicios.extend([Servicio.from_dict(d) for d in data])
            
    if os.path.exists("matriculas.json"):
        with open("matriculas.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            matriculas.clear()
            matriculas.extend([Matricula.from_dict(d) for d in data])

    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            usuarios_sistema.clear()
            usuarios_sistema.extend([Usuario.from_dict(d) for d in data])

def guardar():
    with open("clientes.json", "w", encoding="utf-8") as f:
        json.dump([c.to_dict() for c in clientes], f, indent=4)
        
    with open("entrenadores.json", "w", encoding="utf-8") as f:
        json.dump([e.to_dict() for e in entrenadores], f, indent=4)
        
    with open("servicios.json", "w", encoding="utf-8") as f:
        json.dump([s.to_dict() for s in servicios], f, indent=4)
        
    with open("matriculas.json", "w", encoding="utf-8") as f:
        json.dump([m.to_dict() for m in matriculas], f, indent=4)

    with open("usuarios.json", "w", encoding="utf-8") as f:
        json.dump([u.to_dict() for u in usuarios_sistema], f, indent=4)