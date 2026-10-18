from modelos.persona import Persona


class Cliente(Persona):
    def __init__(self, id: str, nombre: str, correo: str, telefono: str) -> None:
        super().__init__(id, nombre)
        self.correo = correo
        self.telefono = telefono

    def __str__(self) -> str:
        return f"Cliente: {self.id} {self.nombre} {self.correo} {self.telefono}"

    def __repr__(self):
        return f"Cliente {self.id} {self.nombre}"

    def descripcion(self) -> str:
        return f"Cliente: {self.nombre} - {self.correo}"



