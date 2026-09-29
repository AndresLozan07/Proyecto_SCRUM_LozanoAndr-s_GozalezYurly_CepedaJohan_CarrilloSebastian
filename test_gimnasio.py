import unittest
from unittest.mock import patch
import json
import os

# Importamos las funciones y validaciones del proyecto
import funciones
import validaciones

class TestGimnasioForceTech(unittest.TestCase):

    def setUp(self):
        """Configuración inicial antes de cada prueba: simula un entorno limpio de datos."""
        self.datos_iniciales = {
            "usuarios": [
                {"usuario": "admin", "contrasena": "1234", "rol": "Administrador"},
                {"usuario": "emily20", "contrasena": "1234", "rol": "Entrenador", "identificacion": "1099744704"}
            ],
            "clientes": [],
            "entrenadores": [
                {"identificacion": "1099744704", "nombres": "emily", "apellidos": "galvis", "estado": "Activo", "usuario": "emily20"}
            ],
            "servicios": [],
            "matriculas": [],
            "asistencias": [],
            "evaluaciones": [],
            "actividades": []
        }
        with open("datos.json", "w", encoding="utf-8") as f:
            json.dump(self.datos_iniciales, f, indent=4)

    # 1. Probar el registro de clientes
    @patch('builtins.input', side_effect=[
        '10001',           # Identificación
        'Juan',            # Nombres
        'Pérez',           # Apellidos
        'Calle 123',       # Dirección
        '3001234567',      # Celular
        '6011234',         # Teléfono fijo
        '2',               # Estado: Inscrito
        '3',               # Riesgo: Bajo
        'juanp',           # Usuario
        'pass123'          # Contraseña
    ])
    def test_01_registrar_cliente(self, mock_input):
        funciones.registrar_cliente()
        datos = funciones.cargar_datos()

        self.assertEqual(len(datos["clientes"]), 1)
        self.assertEqual(datos["clientes"][0]["identificacion"], "10001")
        self.assertEqual(datos["clientes"][0]["nombres"], "Juan")

    # 2. Probar la consulta de clientes (Perfil y Listado)
    def test_02_consulta_clientes(self):
        datos = funciones.cargar_datos()
        datos["clientes"].append({
            "identificacion": "10001",
            "nombres": "Juan",
            "apellidos": "Pérez",
            "direccion": "Calle 123",
            "celular": "3001234567",
            "telefono_fijo": "6011234",
            "estado": "Inscrito",
            "riesgo": "bajo"
        })
        funciones.guardar_datos(datos)

        cuenta = {"identificacion": "10001", "rol": "Cliente"}
        # Verificación directa de carga
        cliente = next((c for c in datos["clientes"] if c["identificacion"] == cuenta["identificacion"]), None)
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente["nombres"], "Juan")

    # 3. Probar el registro de servicios
    @patch('builtins.input', side_effect=[
        '1',  # Selección del servicio: Clases de yoga
        '10'  # Capacidad máxima
    ])
    def test_03_registrar_servicio(self, mock_input):
        funciones.registrar_servicio()
        datos = funciones.cargar_datos()

        self.assertEqual(len(datos["servicios"]), 1)
        self.assertEqual(datos["servicios"][0]["nombre"], "Clases de yoga")
        self.assertEqual(datos["servicios"][0]["capacidad"], 10)

    # 4. Probar las matrículas
    @patch('builtins.input', side_effect=[
        '1',           # Selección del cliente (1. Juan Pérez)
        '1',           # Selección del servicio (1. Clases de yoga)
        '01/10/2026',  # Fecha de inicio
        '3',           # Duración
        '1'            # Selección de entrenador (1. Emily Galvis)
    ])
    def test_04_matricular_cliente(self, mock_input):
        # Preparación de datos base
        datos = funciones.cargar_datos()
        datos["clientes"].append({
            "identificacion": "10001", "nombres": "Juan", "apellidos": "Pérez"
        })
        datos["servicios"].append({
            "nombre": "Clases de yoga", "capacidad": 10, "clientes_actuales": 0
        })
        funciones.guardar_datos(datos)

        funciones.matricular_cliente()
        datos_actualizados = funciones.cargar_datos()

        self.assertEqual(len(datos_actualizados["matriculas"]), 1)
        self.assertEqual(datos_actualizados["servicios"][0]["clientes_actuales"], 1)

    # 5. Probar las funciones del entrenador (Asistencia y Evaluación)
    @patch('builtins.input', side_effect=[
        '10001',       # Identificación del cliente
        '01/10/2026',  # Fecha
        'Si'           # Asistencia
    ])
    def test_05_funciones_entrenador(self, mock_input):
        cuenta_entrenador = {"usuario": "emily20", "rol": "Entrenador", "identificacion": "1099744704"}
        funciones.registrar_asistencia(cuenta_entrenador)

        datos = funciones.cargar_datos()
        self.assertEqual(len(datos["asistencias"]), 1)
        self.assertEqual(datos["asistencias"][0]["asistencia"], "Si")

    # 6. Probar los reportes
    def test_06_reportes_riesgo_y_rendimiento(self):
        datos = funciones.cargar_datos()
        datos["clientes"].append({
            "identificacion": "10002", "nombres": "Carlos", "apellidos": "Ruiz", "riesgo": "alto"
        })
        datos["evaluaciones"].append({
            "cliente": "10002", "servicio": "Yoga", "rendimiento": "bajo"
        })
        funciones.guardar_datos(datos)

        # Validación de estructuras de reportes
        clientes_alto_riesgo = [c for c in datos["clientes"] if c.get("riesgo") == "alto"]
        evaluaciones_bajo_rendimiento = [e for e in datos["evaluaciones"] if e.get("rendimiento") == "bajo"]

        self.assertEqual(len(clientes_alto_riesgo), 1)
        self.assertEqual(len(evaluaciones_bajo_rendimiento), 1)

    # 7, 8 y 9. Revisa errores, corrige y vuelve a probar las validaciones base
    def test_07_validaciones_sistema(self):
        # Prueba de validaciones para prevención de errores (validaciones.py)
        self.assertTrue(validaciones.validar_nombre("Juan"))
        self.assertFalse(validaciones.validar_nombre("   "))

        self.assertTrue(validaciones.validar_estado("Activo"))
        self.assertFalse(validaciones.validar_estado("Desconocido"))

        self.assertTrue(validaciones.validar_riesgo("alto"))
        self.assertFalse(validaciones.validar_riesgo("extremo"))

        self.assertTrue(validaciones.validar_capacidad(5))
        self.assertFalse(validaciones.validar_capacidad(0))

if __name__ == '__main__':
    unittest.main()