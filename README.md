# 🏋️ Gimnasio Force Tech

Sistema de gestión para gimnasio desarrollado en **Python**, como proyecto académico bajo la metodología **SCRUM**.

La aplicación permite administrar clientes, entrenadores, servicios y matrículas, además de realizar seguimiento al progreso de los clientes mediante registros de asistencia, evaluaciones y actividades.

---

## 📌 Descripción del proyecto

**Force Tech** es una aplicación de consola diseñada para apoyar la gestión administrativa y operativa de un gimnasio.

El sistema implementa diferentes funcionalidades dependiendo del rol del usuario:

* **Administrador**
* **Entrenador**
* **Cliente**

Cada rol dispone de un menú y diferentes opciones de acuerdo con sus responsabilidades dentro del gimnasio.

---

## 👥 Equipo de trabajo

| Integrante               | Rol dentro del proyecto |
| ------------------------ | ----------------------- |
| **Andrés Felipe Lozano** | Scrum Master            |
| **Yurly Gonzalez**       | Product Owner           |
| **Sebastián Carrillo**   | Development Team        |
| **Johan Cepeda**         | Development Team        |

El proyecto fue desarrollado de manera colaborativa utilizando **Git y GitHub**, mediante ramas, commits y Pull Requests.

---

## 🎯 Objetivo

Desarrollar un sistema que permita gestionar de manera organizada la información y los procesos principales de un gimnasio, facilitando el registro de usuarios, la administración de servicios, las matrículas y el seguimiento del progreso de los clientes.

---

# ⚙️ Funcionalidades

## 🔐 Inicio de sesión

El sistema cuenta con autenticación mediante:

* Usuario
* Contraseña
* Rol

Al iniciar sesión, el sistema identifica el tipo de usuario y muestra automáticamente el menú correspondiente.

---

## 👤 Rol Cliente

El cliente puede:

* Consultar su perfil.
* Consultar sus servicios matriculados.
* Registrar actividades realizadas.
* Consultar su progreso.
* Consultar registros de asistencia.
* Consultar evaluaciones de rendimiento y condición física.
* Cerrar sesión.

### Información del perfil

El perfil del cliente puede incluir:

* Número de identificación.
* Nombres.
* Apellidos.
* Dirección.
* Número de celular.
* Teléfono fijo.
* Estado.
* Nivel de riesgo.

---

## 🏋️ Rol Entrenador

El entrenador puede:

* Consultar los clientes que tiene asignados.
* Registrar la asistencia de los clientes.
* Registrar evaluaciones.
* Cerrar sesión.

### Evaluaciones

Las evaluaciones permiten registrar información como:

* Cliente.
* Servicio.
* Fecha.
* Rendimiento.
* Condición física.

---

## 👨‍💼 Rol Administrador

El administrador cuenta con las principales funciones de gestión del sistema:

* Registrar clientes.
* Registrar entrenadores.
* Registrar servicios.
* Matricular clientes.
* Listar clientes.
* Listar servicios.
* Listar entrenadores activos.
* Consultar clientes con riesgo alto.
* Consultar clientes con bajo rendimiento.
* Mostrar el progreso de los clientes.
* Cerrar sesión.

---

# 📝 Gestión de clientes

Durante el registro de un cliente se solicita información como:

* Identificación.
* Nombres.
* Apellidos.
* Dirección.
* Celular.
* Teléfono fijo.
* Estado.
* Nivel de riesgo.
* Usuario.
* Contraseña.

El sistema verifica que la identificación y el nombre de usuario no estén registrados previamente.

### Estados disponibles

* En proceso de inscripción
* Inscrito
* Activo
* Inactivo

### Niveles de riesgo

* Alto
* Medio
* Bajo

---

# 🏃 Gestión de servicios

El administrador puede registrar diferentes servicios del gimnasio:

* Clases de yoga.
* Clases de pilates.
* Entrenamiento personalizado.
* Acceso a la piscina.
* Uso del gimnasio general.

Cada servicio registra:

* Nombre.
* Capacidad máxima.
* Número de clientes actuales.

El sistema controla la capacidad disponible antes de realizar una matrícula.

---

# 📋 Matrículas

La matrícula relaciona:

* Cliente.
* Servicio.
* Fecha de inicio.
* Duración.
* Entrenador.

Cuando se realiza una matrícula, el sistema actualiza automáticamente la cantidad de clientes actuales del servicio.

---

# 📊 Seguimiento del progreso

Una de las funcionalidades principales del sistema es el seguimiento del progreso del cliente.

El sistema permite almacenar:

### Asistencias

* Cliente.
* Fecha.
* Registro de asistencia.

### Evaluaciones

* Cliente.
* Servicio.
* Fecha.
* Rendimiento.
* Condición física.

### Actividades

* Cliente.
* Fecha.
* Actividad realizada.

Con esta información es posible consultar el progreso y detectar clientes que presentan bajo rendimiento.

---

# 💾 Persistencia de datos

La aplicación utiliza archivos **JSON** para almacenar la información del sistema.

Los datos se centralizan en:

```text
datos.json
```

La información almacenada incluye:

```text
usuarios
clientes
entrenadores
servicios
matriculas
asistencias
evaluaciones
actividades
```

El archivo se carga al iniciar las operaciones y se actualiza después de realizar modificaciones.

---

## 🗂️ Estructura del proyecto

```text
Proyecto_SCRUM/
│
├── main.py
├── funciones.py
├── validaciones.py
├── datos.json
└── README.md
```

### `main.py`

Es el punto de entrada de la aplicación.

Se encarga de mostrar el menú inicial, permitir el inicio de sesión y dirigir al usuario al menú correspondiente según su rol.

### `funciones.py`

Contiene la lógica principal de la aplicación, incluyendo:

* Carga y almacenamiento de datos.
* Inicio de sesión.
* Registro de clientes.
* Registro de entrenadores.
* Registro de servicios.
* Matrículas.
* Gestión de perfiles.
* Actividades.
* Asistencias.
* Evaluaciones.
* Consulta de progreso.
* Menús de Cliente, Entrenador y Administrador.

### `datos.json`

Archivo utilizado para almacenar la información persistente de la aplicación.

### `Validaciones`

Contiene las funciones encargadas de validar y controlar los datos ingresados por el usuario para garantizar que la información registrada sea correcta.

### `README.md`

Documento de información del proyecto.

---

# 🛠️ Tecnologías utilizadas

* **Python**
* **JSON**
* **Git**
* **GitHub**
* **Visual Studio Code**
* **SCRUM**

---

# 🚀 Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/AndresLozan07/Proyecto_SCRUM_LozanoAndr-s_GozalezYurly_CepedaJohan_CarrilloSebastian.git
```

## 2. Ingresar a la carpeta

```bash
cd Proyecto_SCRUM_LozanoAndr-s_GozalezYurly_CepedaJohan_CarrilloSebastian
```

## 3. Ejecutar el programa

```bash
python main.py
```

---

# 🔄 Metodología SCRUM

El desarrollo del proyecto se realizó aplicando conceptos de la metodología **SCRUM**, incluyendo:

* Product Backlog.
* Sprint.
* Distribución de tareas.
* Seguimiento diario de avances.
* Trabajo colaborativo.
* Control de versiones.
* Uso de ramas.
* Pull Requests.
* Integración de cambios.

El repositorio de GitHub permite evidenciar la evolución del proyecto mediante commits y contribuciones realizadas durante el desarrollo.

---


# 📚 Propósito académico

Este proyecto permite aplicar conocimientos relacionados con:

* Programación en Python.
* Funciones.
* Estructuras de control.
* Manejo de archivos JSON.
* Modularización.
* Validación de datos.
* Manejo de información.
* Trabajo colaborativo con Git y GitHub.
* Metodología SCRUM.

---

# ⚠️ Nota de seguridad

El archivo `datos.json` utilizado durante las pruebas puede contener usuarios y contraseñas de prueba.

Para una implementación real, las credenciales no deberían almacenarse de esta manera ni publicarse directamente en un repositorio público.

---

## 📄 Estado del proyecto

**Proyecto académico finalizado.**

Desarrollado por el equipo de:

**Andrés Felipe Lozano · Yurly Gonzalez · Sebastián Carrillo · Johan Cepeda**
