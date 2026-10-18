# Taller Informático

## 1. ¿Qué hace el programa?

Este programa sirve para gestionar un taller de reparación de ordenadores.

Permite:
- Añadir clientes y técnicos.
- Registrar reparaciones.
- Buscar clientes por nombre.
- Asignar técnicos a las reparaciones.
- Cambiar el estado de una reparación.
- Modificar el coste de una reparación.
- Calcular el precio con IVA.
- Consultar la facturación y las estadísticas.

Los datos se guardan en archivos JSON para no perderlos al cerrar el programa.

## 2. ¿Cómo ejecutar el programa?

1. Abrir el proyecto en el editor de código.
2. Abrir la terminal y ejecutar: python main.py

## 3. ¿Cómo está organizado?

- main.py: contiene el menú principal, solicita los datos al usuario y coordina las operaciones.

- persistencia.py: carga y guarda la información de clientes, técnicos y reparaciones en archivos JSON.

- modelos/persona.py: define la clase base Persona.

- modelos/cliente.py: define la clase Cliente, que hereda de Persona.

- modelos/tecnico.py: define la clase Tecnico, que hereda de Persona.

- modelos/reparacion.py: define la clase Reparacion, con el estado, el coste y el cálculo del IVA.

- modelos/taller.py: contiene la lógica de gestión de clientes, técnicos y reparaciones.

- datos/clientes.json: almacena los clientes.

- datos/tecnicos.json: almacena los técnicos.

- datos/reparaciones.json: almacena las reparaciones.

## 4. Decisiones tomadas

- He utilizado clases para organizar el código.
- He separado el menú de las clases y del guardado de datos.
- He utilizado archivos JSON para guardar la información sin necesitar una base de datos.
- He añadido comprobaciones para evitar clientes, técnicos y reparaciones con identificadores repetidos.
- He comprobado que los costes no sean negativos.
- He utilizado un IVA del 21 %.

## 5. Conceptos de Python

### Mutabilidad e inmutabilidad

- **Mutable:** una lista puede cambiar. Por ejemplo, self.clientes.append(nuevo) añade un cliente a la lista.
- **Inmutable:** una cadena de texto no se puede modificar directamente. Por ejemplo, nombre.strip() devuelve un texto sin espacios al principio y al final.

### Variables locales y globales

- **Variable local:** existe dentro de una función. Por ejemplo, identificador dentro de una función.
- **Variable global del módulo:** se define fuera de las funciones y puede utilizarse en otras partes del mismo archivo. Por ejemplo, ARCHIVO_CLIENTES en persistencia.py.

### Diferencia entre print() y return

- print() muestra información por pantalla.
- return devuelve un resultado para poder utilizarlo después.

Por ejemplo, buscar_cliente() devuelve el cliente encontrado y print() muestra mensajes al usuario.


