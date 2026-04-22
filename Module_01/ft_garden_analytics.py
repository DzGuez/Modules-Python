#!/usr/bin/env python3

class Plant:

    class Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(f"Stats:  grow: {self.grow_calls}")
            print(f"Stats:  age: {self.age_calls}")
            print(f"Stats:  show: {self.show_calls}")

    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days
        self.stats = Plant.Stats()

    @staticmethod
    def is_older_than_a_year(days):
        return days > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self, amount):
        self.height = round(self.height + amount, 1)
        self.stats.grow_calls += 1

    def age(self):
        self.days = self.days + 1
        self.stats.age_calls += 1

    def show(self):
        self.stats.show_calls += 1
        print(f"{self.name}: {self.height}cm, {self.days} days old")


class Flower(Plant):
    def __init__(self, name, height, days, color):
        super().__init__(name, height, days)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beatifully! ")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):

    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self.shade_calls = 0

        def display(self):
            print(f"Stats:  grow: {self.grow_calls}")
            print(f"Stats:  age: {self.age_calls}")
            print(f"Stats:  show: {self.show_calls}")
            print(f"Shade produced: {self.shade_calls}")

    def __init__(self, name, height, days, trunk_diameter):
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter
        self.stats = Tree.Stats()

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide.")
        self.stats.shade_calls += 1

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, days, harvest_season):
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, amount):
        super().grow(amount)

    def age(self):
        super().age()
        self.nutritional_value = self.nutritional_value + 1

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name, height, days, color, seed_count):
        super().__init__(name, height, days, color)
        self.seed_count = seed_count

    def show(self):
        super().show()
        if self.bloomed:
            print(f"Seeds produced: {self.seed_count}")


def display_stats(plant):
    print(f"[statistics for {plant.name}]")
    plant.stats.display()


def garden():
    print("=== Garden statistics ===")

    # static method
    print("===== Check year old")
    print(f"Is 30 days more than a year? ->{Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? ->{Plant.is_older_than_a_year(400)}")

    # Flower
    print()
    print("===== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_stats(rose)

    # Tree
    print()
    print("===== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)

    # Seed
    print()
    print("===== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age()
    sunflower.days += 19
    sunflower.bloom()
    sunflower.seed_count = 42
    sunflower.show()
    display_stats(sunflower)

    # Anonymous
    print()
    print("===== Anonymous")
    aloe = Plant.anonymous()
    aloe.show()
    display_stats(aloe)


if __name__ == "__main__":
    garden()
