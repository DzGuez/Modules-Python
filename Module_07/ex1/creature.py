#!/usr/bin/env python3

from .capability import HealCapability, TransformCapability
from ex0 import Creature, CreatureFactory

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
    
    def attack
    def transform
    def revert


class Morphagon
