from modelos.persona import Persona


class Tecnico(Persona):
    def __init__(self, id: str, nombre: str, especialidad: str) -> None:
        super().__init__(id, nombre)
        self.especialidad = especialidad

    def __str__(self):
        return f"{super().__str__()} {self.especialidad}"

    def descripcion(self) -> str:
        return f"Técnico: {self.nombre} - {self.especialidad}"