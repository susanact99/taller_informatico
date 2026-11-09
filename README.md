# TallerInformatico

## Descripción del proyecto

TallerInformatico es una aplicación de escritorio desarrollada en Python con PySide6 para gestionar un taller informático.

La aplicación permite administrar clientes, técnicos y reparaciones, así como consultar la facturación y las estadísticas del taller. Los datos se almacenan en archivos JSON para conservar la información entre ejecuciones.

## Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **PySide6:** desarrollo de la interfaz gráfica.
- **Qt Designer:** diseño de las ventanas y diálogos.
- **JSON:** almacenamiento y persistencia de los datos.

## Funcionalidades

### Gestión de clientes
- Añadir nuevos clientes.
- Listar los clientes registrados.
- Buscar clientes por nombre.
- Validar los datos introducidos.

### Gestión de técnicos
- Añadir técnicos.
- Listar técnicos registrados.
- Buscar técnicos por nombre.

### Gestión de reparaciones
- Registrar nuevas reparaciones.
- Consultar todas las reparaciones.
- Asignar técnicos a las reparaciones.
- Modificar el coste de una reparación.
- Cambiar el estado de una reparación.
- Filtrar reparaciones por estado, cliente o técnico.

Los estados disponibles son:
- Pendiente.
- En proceso.
- Finalizada.

### Facturación
La aplicación calcula la facturación total del taller teniendo en cuenta únicamente las reparaciones finalizadas.

El cálculo incluye el IVA del 21 %.

### Estadísticas
Se pueden consultar las siguientes estadísticas:
- Número total de reparaciones.
- Reparaciones pendientes.
- Reparaciones en proceso.
- Reparaciones finalizadas.
- Número de clientes con reparaciones registradas.

### Persistencia de datos
La información se almacena en archivos JSON:

- `clientes.json`
- `tecnicos.json`
- `reparaciones.json`

Los datos se cargan al iniciar la aplicación y se guardan después de realizar modificaciones.

## Estructura del proyecto

```text
TallerInformatico/
│
├── controlador/
│   └── controlador.py
│
├── datos/
│   ├── clientes.json
│   ├── tecnicos.json
│   └── reparaciones.json
│
├── modelos/
│   ├── persona.py
│   ├── cliente.py
│   ├── tecnico.py
│   ├── reparacion.py
│   └── taller.py
│
├── vista/
│   ├── ventana_principal.py
│   ├── ventana_principal.ui
│   ├── dialogo_agregar_cliente.py
│   ├── dialogo_agregar_cliente.ui
│   ├── dialogo_agregar_tecnico.py
│   ├── dialogo_agregar_tecnico.ui
│   ├── dialogo_aniadir_reparacion.py
│   ├── dialogo_aniadir_reparacion.ui
│   ├── dialogo_asignar_tecnico.py
│   ├── dialogo_asignar_tecnico.ui
│   ├── dialogo_cambiar_estado.py
│   ├── dialogo_cambiar_estado.ui
│   └── dialogo_modificar_coste.py
│
├── persistencia.py
├── main.py
└── README.md
```

## Instalación y ejecución

### 1. Requisitos previos

Es necesario tener instalado Python y pip.

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

En Windows:

```bash
.venv\Scripts\activate
```

### 4. Instalar PySide6

```bash
python -m pip install PySide6
```

### 5. Ejecutar la aplicación

```bash
python main.py
```

## Autor

Susana Calzadilla

Proyecto desarrollado como parte del Ciclo Formativo de Grado Superior de Desarrollo de Aplicaciones Multiplataforma (DAM).