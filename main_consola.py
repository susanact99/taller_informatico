
from modelos.cliente import Cliente
from modelos.tecnico import Tecnico
from modelos.reparacion import Reparacion
from persistencia import actualizar_taller, guardar_taller


def mostrar_menu():
    print("\n GESTIÓN DEL TALLER INFORMÁTICO:")
    print("1. Dar de alta un cliente")
    print("2. Dar de alta un técnico")
    print("3. Dar de alta una reparación")
    print("4. Listar clientes")
    print("5. Buscar clientes por nombre")
    print("6. Listar técnicos")
    print("7. Listar reparaciones")
    print("8. Asignar técnico a una reparación")
    print("9. Cambiar estado de una reparación")
    print("10. Modificar coste de una reparación")
    print("11. Filtrar reparaciones por estado")
    print("12. Consultar facturación")
    print("13. Consultar estadísticas")
    print("0. Guardar y salir")

def pedir_coste():
    while True:
        try:
            coste = float(input("Coste sin IVA: "))

            if coste < 0:
                print("El coste no puede ser negativo.")
                continue

        except ValueError:
            print("Introduce un número válido.")
        else:
            return coste


def alta_cliente(taller):
    print("\n ALTA DE CLIENTE ")

    identificador = input("ID del cliente: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo electrónico: ").strip()
    telefono = input("Teléfono: ").strip()

    if not identificador or not nombre or not correo or not telefono:
        print("Todos los campos son obligatorios.")
        return

    cliente = Cliente(identificador, nombre, correo, telefono)

    try:
        taller.alta_cliente(cliente)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        guardar_taller(taller)
        print("Cliente registrado correctamente.")


def alta_tecnico(taller):
    print("\n ALTA DE TÉCNICO ")

    identificador = input("ID del técnico: ").strip()
    nombre = input("Nombre: ").strip()
    especialidad = input("Especialidad: ").strip()

    if not identificador or not nombre or not especialidad:
        print("Todos los campos son obligatorios.")
        return

    tecnico = Tecnico(identificador, nombre, especialidad)

    try:
        taller.alta_tecnico(tecnico)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        guardar_taller(taller)
        print("Técnico registrado.")


def alta_reparacion(taller):
    print("\n ALTA DE REPARACIÓN ")

    if not taller.clientes:
        print("No existen clientes registrados en el taller.")
        return

    identificador = input("ID de la reparación: ").strip()
    cliente_id = input("ID del cliente: ").strip()

    if not identificador or not cliente_id:
        print("Los identificadores son obligatorios.")
        return

    cliente = taller.buscar_cliente(cliente_id)

    if cliente is None:
        print("No existe ningún cliente con ese ID registrado en el taller.")
        return

    equipo = input("Equipo: ").strip()
    descripcion = input("Descripción de la avería: ").strip()

    if not equipo or not descripcion:
        print("El equipo y la descripción son obligatorios.")
        return

    tecnico = None

    if taller.tecnicos:
        respuesta = input(
            "¿Quieres asignar un técnico ahora? (s/n): "
        ).strip().lower()

        if respuesta == "s":
            tecnico_id = input("ID del técnico: ").strip()
            tecnico = taller.buscar_tecnico(tecnico_id)

            if tecnico is None:
                print("No existe ningún técnico con ese ID en el taller.")
                return

        elif respuesta != "n":
            print("Respuesta no válida.")
            return

    coste = pedir_coste()

    try:
        reparacion = Reparacion(
            id=identificador,
            cliente=cliente,
            equipo=equipo,
            descripcion=descripcion,
            tecnico=tecnico,
            estado="pendiente",
            coste_sin_IVA=coste
        )

        taller.alta_reparacion(reparacion)

    except ValueError as e:
        print(f"Error: {e}")
    else:
        guardar_taller(taller)
        print("Reparación registrada correctamente.")


def mostrar_clientes(taller):
    print("\n  CLIENTES  ")

    if not taller.clientes:
        print("No hay clientes registrados.")
        return

    for cliente in taller.listar_clientes():
        print(cliente)


def buscar_clientes_por_nombre(taller):
    nombre = input(
        "Introduce el nombre o parte del nombre: "
    ).strip()

    resultados = taller.buscar_clientes_por_nombre(nombre)

    if resultados:
        for cliente in resultados:
            print(cliente)
    else:
        print("No se encontraron clientes.")


def mostrar_tecnicos(taller):
    print("\n  TÉCNICOS ")

    if not taller.tecnicos:
        print("No hay técnicos registrados.")
        return

    for tecnico in taller.listar_tecnicos():
        print(tecnico)


def mostrar_reparaciones(taller):
    print("\n REPARACIONES ")

    if not taller.reparaciones:
        print("No hay reparaciones registradas.")
        return

    for reparacion in taller.listar_reparaciones():
        print(reparacion)


def asignar_tecnico(taller):
    reparacion_id = input("ID de la reparación: ").strip()
    tecnico_id = input("ID del técnico: ").strip()

    try:
        taller.asignar_tecnico(reparacion_id, tecnico_id)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        guardar_taller(taller)
        print("Técnico asignado correctamente.")


def cambiar_estado(taller):
    reparacion_id = input("ID de la reparación: ").strip()

    print("Estados: pendiente, en proceso, finalizada")
    estado = input("Nuevo estado: ").strip().lower()

    try:
        taller.cambiar_estado(reparacion_id, estado)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        guardar_taller(taller)
        print("Estado actualizado correctamente.")


def modificar_coste(taller):
    reparacion_id = input("ID de la reparación: ").strip()
    coste = pedir_coste()

    try:
        taller.modificar_coste(reparacion_id, coste)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        guardar_taller(taller)
        print("Coste actualizado correctamente.")


def filtrar_reparaciones(taller):
    print("Estados: pendiente, en proceso, finalizada")
    estado = input("Estado que quieres consultar: ").strip().lower()

    if estado not in Reparacion.ESTADOS_VALIDOS:
        print("Estado no válido.")
        return

    resultados = taller.filtrar_reparaciones(estado)

    if resultados:
        for reparacion in resultados:
            print(reparacion)
    else:
        print("No hay reparaciones con ese estado.")


def mostrar_facturacion(taller):
    total = taller.facturacion_total()
    print(
        "\nFacturación total de reparaciones finalizadas "
        f"(IVA incluido): {total:.2f} €"
    )

def mostrar_estadisticas(taller):
    datos = taller.estadisticas()

    print("\n ESTADÍSTICAS ")
    print(f"Total de reparaciones: {datos['total_reparaciones']}")
    print(f"Pendientes: {datos['pendientes']}")
    print(f"En proceso: {datos['en_proceso']}")
    print(f"Finalizadas: {datos['finalizadas']}")
    print(
        "Clientes distintos con reparaciones: "
        f"{datos['clientes_con_reparaciones']}"
    )

def main():
    try:
        taller = actualizar_taller()
    except (ValueError, KeyError, OSError) as error:
        print(f"Error al cargar los datos: {error}")
        return

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        try:
            match opcion:
                case "1":
                    alta_cliente(taller)
                case "2":
                    alta_tecnico(taller)
                case "3":
                    alta_reparacion(taller)
                case "4":
                    mostrar_clientes(taller)
                case "5":
                    buscar_clientes_por_nombre(taller)
                case "6":
                    mostrar_tecnicos(taller)
                case "7":
                    mostrar_reparaciones(taller)
                case "8":
                    asignar_tecnico(taller)
                case "9":
                    cambiar_estado(taller)
                case "10":
                    modificar_coste(taller)
                case "11":
                    filtrar_reparaciones(taller)
                case "12":
                    mostrar_facturacion(taller)
                case "13":
                    mostrar_estadisticas(taller)
                case "0":
                    guardar_taller(taller)
                    print("Datos guardados. Hasta pronto.")
                    break

                case _:
                    print("Opción no válida.")

        except OSError as error:
            print(f"Error al guardar los datos: {error}")


if __name__ == "__main__":
    main()
