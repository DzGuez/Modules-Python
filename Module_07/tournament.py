#!/usr/bin/env python3

from ex2 import BattleStrategy
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2 import InvalidStrategyError
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import FlameFactory, AquaFactory
from ex0 import CreatureFactory


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    """ Funcion de batalla para recorrer en la lista los posibles combates"""

    for i, par1 in enumerate(opponents):
        for j in range(i + 1, len(opponents)):
            par2 = opponents[j]
            factory1, strategy1 = par1
            factory2, strategy2 = par2

            print("\n* Battle *")
            creature1 = factory1.create_base()
            creature2 = factory2.create_base()
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    """ Ejecuta los 3 escenarios de batalla"""

    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    trans_factory = TransformCreatureFactory()

    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    # Torneo 0
    tournament_0 = [
            (flame_factory, normal),
            (heal_factory, defensive),
    ]
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(tournament_0)} opponents involved")
    battle(tournament_0)
    print()

    # Torneo 1
    tournament_1 = [
            (flame_factory, aggressive),
            (heal_factory, defensive),
    ]
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(tournament_1)} opponents involved")
    battle(tournament_1)
    print()

    # Torneo 2
    tournament_2 = [
            (aqua_factory, normal),
            (heal_factory, defensive),
            (trans_factory, aggressive),
    ]
    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print(f"{len(tournament_2)} opponents involved")
    battle(tournament_2)
    print()


if __name__ == "__main__":
    main()
