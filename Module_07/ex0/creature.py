#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Creature(ABC):
    """ Clase abstracta que representa una carta para Creature"""

    def __init__(self, name: str, type_creature: str) -> None:
        self.name = name
        self.type_creature = type_creature

    def describe(self) -> str:
        return f"{self.name} is a {self.type_creature} type Creature"

    @abstractmethod
    def attack(self) -> str:
        ...


class Flameling(Creature):
    """ Clase Flameling que representa la creatura de fuego"""

    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    """ Clase Pyrodon que representa la creatura de fuego/volador"""

    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    """ Clase Aquabub que representa la creatura de agua"""

    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    """ Clase Torragon que representa otra creatura de agua"""

    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
