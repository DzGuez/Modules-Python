#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, days):
        self._name = name

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = round(0.0, 1)
        else:
            self._height = round(height, 1)

        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._days = 0
        else:
            self._days = days

    def get_height(self):
        return self._height

    def get_age(self):
        return self._days

    def set_height(self, height):
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update reject")
        else:
            self._height = round(height, 1)
            print(f"Height updated: {self._height}cm")

    def set_age(self, days):
        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = days
            print(f"Age updated: {self._days} days")

    def show(self):
        print(f"{self._name}: {self._height}cm, {self._days} days old")


def garden():
    print("=== Garden Security System ===")
    plants = [
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

    print(
        f"Current state: {plants[0]._name}: "
        f"{float(plants[0]._height)}cm, {plants[0]._days} days old")


if __name__ == "__main__":
    garden()
