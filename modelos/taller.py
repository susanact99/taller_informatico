
from modelos.cliente import Cliente
from modelos.reparacion import Reparacion
from modelos.tecnico import Tecnico


class Taller:
    def __init__(self):
        self.clientes = []
        self.tecnicos = []
        self.reparaciones = []

#1 Alta cliente
    def alta_cliente(self, nuevo: Cliente):
        for cliente in self.clientes:
            if cliente.id == nuevo.id:
                raise ValueError("El cliente ya existe")

        self.clientes.append(nuevo)

    def buscar_cliente(self, identificador: str):
        for cliente in self.clientes:
            if str(cliente.id) == str(identificador):
                return cliente
        return None

    def buscar_clientes_por_nombre(self, nombre: str) -> list:
        resultados = []

        for cliente in self.clientes:
            if nombre.lower() in cliente.nombre.lower():
                resultados.append(cliente)

        return resultados

    def listar_clientes(self) -> list:
        return self.clientes

    # TECNICOS

    def alta_tecnico(self, nuevo: Tecnico):
        for tecnico in self.tecnicos:
            if tecnico.id == nuevo.id:
                raise ValueError("El técnico ya existe")

        self.tecnicos.append(nuevo)

    def buscar_tecnico(self, identificador: str):
        for tecnico in self.tecnicos:
            if str(tecnico.id) == str(identificador):
                return tecnico
        return None

    def listar_tecnicos(self) -> list:
        return self.tecnicos

    # REPARACIONES

    def alta_reparacion(self, nuevo: Reparacion):
        for reparacion in self.reparaciones:
            if reparacion.id == nuevo.id:
                raise ValueError("La reparación ya existe")

        cliente = self.buscar_cliente(nuevo.cliente.id)

        if cliente is None:
            raise ValueError("El cliente no está registrado")

        nuevo.cliente = cliente

        if nuevo.tecnico is not None:
            tecnico = self.buscar_tecnico(nuevo.tecnico.id)

            if tecnico is None:
                raise ValueError("El técnico no está registrado")

            nuevo.tecnico = tecnico

        self.reparaciones.append(nuevo)

    def buscar_reparacion(self, identificador: str):
        for reparacion in self.reparaciones:
            if reparacion.id == identificador:
                return reparacion
        return None

    def listar_reparaciones(self) -> list:
        return self.reparaciones

    def asignar_tecnico(self, reparacion_id: str, tecnico_id: str):
        reparacion = self.buscar_reparacion(reparacion_id)
        tecnico = self.buscar_tecnico(tecnico_id)

        if reparacion is None:
            raise ValueError("La reparación no existe")

        if tecnico is None:
            raise ValueError("El técnico no está registrado")

        reparacion.tecnico = tecnico

    def cambiar_estado(self, reparacion_id: str, estado: str):
        reparacion = self.buscar_reparacion(reparacion_id)

        if reparacion is None:
            raise ValueError("La reparación no existe")

        if estado in Reparacion.ESTADOS_VALIDOS:
            reparacion.estado = estado
        else:
            raise ValueError("El estado no no es válido")

    def modificar_coste(self, reparacion_id: str, coste: float):
        reparacion = self.buscar_reparacion(reparacion_id)

        if reparacion is None:
            raise ValueError("La reparación no existe")

        reparacion.coste = coste

    def filtrar_reparaciones(self, estado: str) -> list:
        resultados = []

        for reparacion in self.reparaciones:
            if reparacion.estado == estado:
                resultados.append(reparacion)

        return resultados


    def facturacion_total(self) -> float:
        total = 0

        for reparacion in self.reparaciones:
            if reparacion.estado == "finalizada":
                total += reparacion.coste_con_IVA()

        return round(total, 2)


    def estadisticas(self) -> dict:
        pendientes = 0
        en_proceso = 0
        finalizadas = 0
        clientes_con_reparaciones = set()

        for reparacion in self.reparaciones:
            if reparacion.estado == "pendiente":
                pendientes += 1
            elif reparacion.estado == "en proceso":
                en_proceso += 1
            elif reparacion.estado == "finalizada":
                finalizadas += 1

            clientes_con_reparaciones.add(reparacion.cliente.id)

        return {
            "total_reparaciones": len(self.reparaciones),
            "pendientes": pendientes,
            "en_proceso": en_proceso,
            "finalizadas": finalizadas,
            "clientes_con_reparaciones": len(clientes_con_reparaciones)
        }
