#!/usr/bin/env python3

class Plant:
    """ Representa una planta con nombre, altura, edad y tasa crecimiento """
    def __init__(self, name: str, 
                height: float,
                days: int,
                growth_rate: float
                ) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate

    def grow(self) -> None:
        """ Incrementa la altura de la planta, segun su tasa de crecimiento"""
        """ Se redondea el decimal a 1 """
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        """ Incrementa la edad de la planta 1 dia """
        self.days = self.days + 1

    def show(self) -> None:
        """ Muestra la informacion actual de la planta """
        print(f"{self.name}: {self.height}cm, {self.days} days old. ")


def simulate_week(name) -> None:
    """
    Simula el crecimiento de una planta en 7 dias
    Guarda la altura inicial
    Hace crecer y envejecer la planta cada dia
    Imprime el estado diario
    Calcula y muestra el crecimiento total en los 7 dias
    """
    initial_height = name.height

    for day in range(7):
        name.age()
        name.grow()
        print(f"=== Day {day + 1} ===")
        name.show()

    # Calculo el total del crecimiento con round y 1 para el decimal
    total_growth = round(name.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm ")


def garden() -> None:
    """ Funcion para crear una planta y simular el crecimiento de la semana"""
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30, 0.8)
    rose.show()
    simulate_week(rose)


if __name__ == "__main__":
    garden()
