#!/usr/bin/env python3

class Plant:
    """ Representa una planta con nombre, altura y edad """
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self, amount: float) -> None:
        """ Incrementa la altura de la planta en (cantidad) dada """
        self.height = round(self.height + amount, 1)

    def age(self) -> None:
        """ Incrementa la edad de la planta 1 dia """
        self.days = self.days + 1

    def show(self) -> None:
        """ Muestra la informacion actual de la planta """
        print(f"{self.name}: {self.height}cm, {self.days} days old")


class Flower(Plant):
    """ Planta con un nuevo atributo y un estado para florecer = False """
    def __init__(self, name: str,
                height: float,
                days: int,
                color: str
                ) -> None:
        super().__init__(name, height, days)
        self.color: str = color
        self.bloomed: bool = False

    def bloom(self) -> None:
        """ Marca la flor como florecida es decir cambia a estado True """
        self.bloomed = True

    def show(self) -> None:
        """ Imprime el estado de la flor 
        Incluyendo el color, el mensaje de si ya florecio segun corresponda"""
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully! ")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    """ Representa un arbol con atributos del padre, y diametro del tronco"""
    def __init__(self, name: str,
                height: float,
                days: int,
                trunk_diameter: float
                ) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        """ Imprime las dimensiones se sombra que produce el arbol"""
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide.")

    def show(self):
        """ Imprime el estado actual del arbol y el diametro del tronco"""
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    """ Representa vegetal con atributos del padre, y valor nutricional"""
    def __init__(self, name: str,
                height: float,
                days: int,
                harvest_season: str
                ) -> None:
        super().__init__(name, height, days)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def grow(self, amount: float) -> None:
        """ Incrementa la altura del vegetal en (cantidad) dada"""
        super().grow(amount)

    def age(self) -> None:
        """ Incrementa la edad del vegetal y suma 1 al valor nutricional"""
        super().age()
        self.nutritional_value = self.nutritional_value + 1

    def show(self) -> None:
        """ Imprime el estado del vegetal"""
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def garden() -> None:
    """ Demuestra el uso de las subclases mencionadas
    Creo instancias de cada tipo, muestro el estado inicial
    Luego ejecuto los metodos especificos y muestro el resultado"""
    print("=== Garden Plant Types ===")

    print("===== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("===== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("===== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(2.1)
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    garden()
