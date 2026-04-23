#!/usr/bin/env python3

class Plant:
    """ Representa una planta con nombre, altura y edad """
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        """ Muestra la informacion de la planta en pantalla """
        print(f"{self.name}: {self.height}cm, {self.age} days old. ")


def garden() -> None:
    """ Nueva funcion para crear nuevas plantas y mostrar su informacion"""
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    Plant.show(rose)
    Plant.show(sunflower)
    Plant.show(cactus)


if __name__ == "__main__":
    garden()
