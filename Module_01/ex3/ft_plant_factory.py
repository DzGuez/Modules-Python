#!/usr/bin/env python3

class Plant:
    """ Representa una planta con nombre, altura y edad """
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self) -> None:
        """ Se redondea la altura de la planta en 1 decimal"""
        self.height = round(self.height, 1)

    def age(self) -> None:
        """ Incrementa la edad de la planta 1 dia """
        self.days = self.days + 1

    def show(self) -> None:
        """ Muestra la informacion actual de la planta """
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def garden() -> None:
    """ Funcion para crear varias plantas en un formato de lista """
    """ Y luego iterar sobre la lista para mostrar cada planta creada """
    plants: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    garden()
