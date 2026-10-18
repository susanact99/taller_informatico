
from pathlib import Path
import json

from modelos.cliente import Cliente
from modelos.tecnico import Tecnico
from modelos.reparacion import Reparacion
from modelos.taller import Taller

CARPETA_DATOS = Path(__file__).parent / "datos"

ARCHIVO_CLIENTES = CARPETA_DATOS / "clientes.json"
ARCHIVO_REPARACIONES = CARPETA_DATOS / "reparaciones.json"
ARCHIVO_TECNICOS = CARPETA_DATOS / "tecnicos.json"

def cargar_datos(ruta: Path) -> list:
    if not ruta.exists():
        with ruta.open("w", encoding="utf-8") as archivo:
            json.dump([], archivo, indent=4, ensure_ascii=False)

    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Error al leer el archivo {ruta.name}"
        ) from error

    if not isinstance(datos, list):
        raise ValueError(
            f"El archivo {ruta.name} no contiene una lista"
        )

    return datos


def actualizar_taller() -> Taller:
    taller = Taller()

    # Cargar clientes
    clientes_datos = cargar_datos(ARCHIVO_CLIENTES)

    for dato in clientes_datos:
        cliente = Cliente(
            str(dato["id"]),
            dato["nombre"],
            dato["correo"],
            dato["telefono"]
        )

        taller.alta_cliente(cliente)

    # Cargar técnicos
    tecnicos_datos = cargar_datos(ARCHIVO_TECNICOS)

    for dato in tecnicos_datos:
        tecnico = Tecnico(
            str(dato["id"]),
            dato["nombre"],
            dato["especialidad"]
        )

        taller.alta_tecnico(tecnico)

    reparaciones_datos = cargar_datos(ARCHIVO_REPARACIONES)

    for dato in reparaciones_datos:
        cliente_id = str(dato["cliente_id"])
        cliente = taller.buscar_cliente(cliente_id)

        if cliente is None:
            raise ValueError(
                f"El cliente con ID {cliente_id} no existe."
            )

        tecnico_id = dato.get("tecnico_id")
        tecnico = None

        if tecnico_id is not None:
            tecnico = taller.buscar_tecnico(str(tecnico_id))

            if tecnico is None:
                raise ValueError(
                    f"El técnico con ID {tecnico_id} no existe."
                )

        reparacion = Reparacion(
            id=str(dato["id"]),
            cliente=cliente,
            equipo=dato["equipo"],
            descripcion=dato["descripcion"],
            tecnico=tecnico,
            estado=dato["estado"],
            coste_sin_IVA=float(dato["coste"])
        )

        taller.alta_reparacion(reparacion)

    return taller

def guardar_taller(taller: Taller) -> None:
    clientes_datos = []

    for cliente in taller.clientes:
        clientes_datos.append({
            "id": cliente.id,
            "nombre": cliente.nombre,
            "correo": cliente.correo,
            "telefono": cliente.telefono
        })

    tecnicos_datos = []

    for tecnico in taller.tecnicos:
        tecnicos_datos.append({
            "id": tecnico.id,
            "nombre": tecnico.nombre,
            "especialidad": tecnico.especialidad
        })

    reparaciones_datos = []

    for reparacion in taller.reparaciones:
        reparaciones_datos.append({
            "id": reparacion.id,
            "cliente_id": reparacion.cliente.id,
            "tecnico_id": (
                reparacion.tecnico.id
                if reparacion.tecnico is not None
                else None
            ),
            "equipo": reparacion.equipo,
            "descripcion": reparacion.descripcion,
            "estado": reparacion.estado,
            "coste": reparacion.coste
        })

    with ARCHIVO_CLIENTES.open("w", encoding="utf-8") as archivo:
        json.dump(clientes_datos, archivo, indent=4, ensure_ascii=False)

    with ARCHIVO_TECNICOS.open("w", encoding="utf-8") as archivo:
        json.dump(tecnicos_datos, archivo, indent=4, ensure_ascii=False)

    with ARCHIVO_REPARACIONES.open("w", encoding="utf-8") as archivo:
        json.dump(
            reparaciones_datos,
            archivo,
            indent=4,
            ensure_ascii=False
        )
