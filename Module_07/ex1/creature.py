#!/usr/bin/env python3

from .capability import HealCapability, TransformCapability
from ex0 import Creature


class Sproutling(Creature, HealCapability):
    """ Clase Sproutling que hereda de creatura y curacion"""

    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"


class Bloomelle(Creature, HealCapability):
    """ Clase Bloomelle que hereda de creatura y curacion"""

    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"


class Shiftling(Creature, TransformCapability):
    """ Clase Shiftling que hereda de creatura y transformacion"""

    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self._status:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        self._status = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self._status = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    """ Clase Morphagon que hereda de creatura y transformacion"""

    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self._status:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self._status = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._status = False
        return f"{self.name} stabilizes its form."
