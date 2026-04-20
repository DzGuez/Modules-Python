#!/usr/bin/env python3

# Modifico la clase de antes para llamar la edad days
# Agrego el argumento tasa de crecimiento y lo estancio
class Plant:
    def __init__(self, name, height, days, growth_rate):
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate

    # Def el metodo de estancia crecer y sumo la altura actual + el crecimiento
    # Ademas agrego round y 1 al final para manejar decimal y solo ponga 1
    def grow(self):
        self.height = round(self.height + self.growth_rate, 1)

    # Defino el metodo de estancia edad para ir +1 en cada dia que pasa
    def age(self):
        self.days = self.days + 1

    # Muestra la informacion de la planta como yo la quiero ver
    def show(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old. ")


# Simulador de la semana, necesito la altura inicial, para el resumen
def simulate_week(name):
    initial_height = name.height

    for day in range(7):
        name.age()
        name.grow()
        print(f"=== Day {day + 1} ===")
        name.show()

    # Calculo el total del crecimiento con round y 1 para el decimal
    total_growth = round(name.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm ")


def garden():
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30, 0.8)
    rose.show()
    simulate_week(rose)


if __name__ == "__main__":
    garden()
