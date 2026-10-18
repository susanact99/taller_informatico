class Persona:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self) -> str:
        return f'{self.id} {self.nombre}'

    def __repr__(self) -> str:
        return f'Persona: {self.id} {self.nombre}'

    def descripcion(self) -> str:
        return f"{self.id} - {self.nombre}"