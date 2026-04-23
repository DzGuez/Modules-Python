#!/usr/bin/env python3

class Plant:
    """ Representa una planta con nombre, altura y edad """
    def __init__(self, name: str, height: float, days: int) -> None:
        """
        Inicializa la planta, esta vez con validacion de valores negativos
        Si la altura o la edad son negativos, se imprime mensaje de error
        Y se asigna 0.0 / 0 como valor por defecto. Se redondea a 1 decimal
        """
        self._name = name

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height: float = round(0.0, 1)
        else:
            self._height = round(height, 1)

        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._days: int = 0
        else:
            self._days = days

    def get_height(self) -> float:
        """ Retorna la altura actual de la planta """
        return self._height

    def get_age(self) -> int:
        """ Retorna la edad actual de la planta """
        return self._days

    def set_height(self, height: float) -> None:
        """ 
        Actualiza e imprime la altura de la planta si el valor es valido.
        Redondea a 1 decimal
        """
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update reject")
        else:
            self._height = round(height, 1)
            print(f"Height updated: {self._height}cm")

    def set_age(self, days: int) -> None:
        """ Actualiza e imprime la altura de la planta si el valor es valido"""
        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = days
            print(f"Age updated: {self._days} days")

    def show(self) -> None:
        """ Muestra la informacion actual de la planta """
        print(f"{self._name}: {self._height}cm, {self._days} days old")


def garden() -> None:
    """
    Demostracion del sistema de validacion de la planta
    Funcion para crear varias plantas en un formato de lista
    Y luego iterar sobre la lista pero solo mostramos la primera planta
    Luego aplicamos validaciones validad e invalidas y se muestra el resultado
    """
    print("=== Garden Security System ===")

    plants: list[Plant] = [
        Plant("Rose", 15.0, 10),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]
    for i in range(1):
        print("Plant created: ", end="")
        plants[i].show()

    print()
    plants[0].set_height(25)
    plants[0].set_age(30)
    print()
    plants[0].set_height(-42)
    plants[0].set_age(-42)
    print()

    print("Current state: ", end="")
    plants[0].show()


if __name__ == "__main__":
    garden()
