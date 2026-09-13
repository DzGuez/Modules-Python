#!/usr/bin/env python3

from abc import ABC, abstractmethod
from .exceptions import InvalidStrategyError
from ex0 import Creature
from ex1 import HealCapability, TransformCapability


class BattleStrategy(ABC):
    """ Estrategia abstracta de batalla, la cual define como actua
    una Creature y si es compatible para avanzar"""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """ Verifica si creature es compatible con la estrategia"""
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """ Ejecuta las acciones de esta estrategia sobre creature
        Y lanza InvalidStrategyError si no es compatible"""
        ...


class NormalStrategy(BattleStrategy):
    """ Clase para verificar y actuar en estrategia normal"""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                    f"Invalid Creature '{creature.name}' "
                    f"for this normal strategy"
            )

        print(creature.attack())


class DefensiveStrategy(BattleStrategy):
    """ Clase para verificar y actuar en estrategia defensiva"""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(
                    f"Invalid Creature '{creature.name}' "
                    f"for this defensive strategy"
            )

        print(creature.attack())
        print(creature.heal())


class AggressiveStrategy(BattleStrategy):
    """ Clase para verificar y actuar en estrategia agresiva"""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                    f"Invalid Creature '{creature.name}' "
                    f"for this aggressive strategy"
            )

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
