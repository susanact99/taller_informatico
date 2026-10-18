
from modelos.cliente import Cliente
from modelos.tecnico import Tecnico


class Reparacion:
    IVA = 0.21
    ESTADOS_VALIDOS = ("pendiente", "en proceso", "finalizada")

    def __init__(
        self,
        id: str,
        cliente: Cliente,
        equipo: str,
        descripcion: str,
        tecnico: Tecnico = None,
        estado: str = "pendiente",
        coste_sin_IVA: float = 0.0
    ) -> None:
        self.id = id
        self.cliente = cliente
        self.equipo = equipo
        self.descripcion = descripcion
        self.tecnico = tecnico
        self.estado = estado
        self.coste = coste_sin_IVA

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, nuevo: str) -> None:
        if nuevo not in self.ESTADOS_VALIDOS:
            raise ValueError("Estado no válido")
        self._estado = nuevo

    @property
    def coste(self) -> float:
        return self._coste

    @coste.setter
    def coste(self, nuevo: float) -> None:
        if nuevo < 0:
            raise ValueError("El coste no puede ser negativo")
        self._coste = nuevo

    def coste_con_IVA(self) -> float:
        return round(self.coste * (1 + self.IVA), 2)

    def __str__(self) -> str:
        if self.tecnico is None:
            nombre_tecnico = "Sin asignar"
        else:
            nombre_tecnico = self.tecnico.nombre

        return (
            f"Reparación: {self.id} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Equipo: {self.equipo} | "
            f"Avería: {self.descripcion} | "
            f"Técnico: {nombre_tecnico} | "
            f"Estado: {self.estado} | "
            f"Coste sin IVA: {self.coste:.2f} € | "
            f"Coste con IVA: {self.coste_con_IVA():.2f} €"
        )

    def __repr__(self) -> str:
        return f"Reparacion(id={self.id!r}, cliente={self.cliente.id!r})"
