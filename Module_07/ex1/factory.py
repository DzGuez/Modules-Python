#!/usr/bin/env python3

from ex0 import CreatureFactory
from .creature import Sproutling, Bloomelle, Shiftling, Morphagon


class TransformCreatureFactory(CreatureFactory):
    """ Fabrica que transforma una creatura. """

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()


class HealingCreatureFactory(CreatureFactory):
    """ Fabrica que cura una creatura. """

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()
