#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    def grow(self):
        self.height = round(self.height, 1)

    def age(self):
        self.days = self.days + 1

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def garden():
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    print("=== Plant Factory Output ===")
    for i in range(len(plants)):
        print("Created: ", end="")
        plants[i].show()


if __name__ == "__main__":
    garden()
